#!/usr/bin/env python
# Copyright (c) 2014-2018 Michael Hirsch, Ph.D.

"""
Input/output: default units are METERS and DEGREES.
boolean deg=True means degrees

Most functions accept Numpy arrays of any shape

see tests/Test.py for example uses.
"""
from copy import deepcopy
from datetime import datetime
from typing import Tuple, List, Union
import numpy as np
from numpy import sin, cos, tan, sqrt, radians, arctan2, hypot, degrees, pi
from .timeconv import str2dt  # noqa: F401
from .azelradec import radec2azel, azel2radec  # noqa: F401
from .eci import eci2ecef, ecef2eci
from .datetime2hourangle import datetime2sidereal  # noqa: F401


class EarthEllipsoid:
    """generate reference ellipsoid"""

    def __init__(self, model: str='wgs84') -> None:
        if model == 'wgs84':
            """https://en.wikipedia.org/wiki/World_Geodetic_System#WGS84"""
            self.a = 6378137.  # semi-major axis [m]
            self.f = 1 / 298.2572235630  # flattening
            self.b = self.a * (1 - self.f)  # semi-minor axis
        elif model == 'grs80':
            """https://en.wikipedia.org/wiki/GRS_80"""
            self.a = 6378137.  # semi-major axis [m]
            self.f = 1 / 298.257222100882711243  # flattening
            self.b = self.a * (1 - self.f)  # semi-minor axis


def lookAtSpheroid(lat0: float, lon0: float, h0: float, az: float, tilt: float,
                   ell: EarthEllipsoid=None, deg: bool=True) -> Tuple[float, float, float]:
    """
    Calculates line-of-sight intersection with Earth (or other ellipsoid) surface from above surface / orbit

    Args:
        lat0, lon0: latitude and longitude of starting point
        h0: altitude of starting point in meters
        az: azimuth angle of line-of-sight, clockwise from North
        tilt: tilt angle of line-of-sight with respect to local vertical (nadir = 0)
    Returns:
        lat, lon: latitude and longitude where the line-of-sight intersects with the Earth ellipsoid
        d: slant range in meters from the starting point to the intersect point
        Values will be NaN if the line of sight does not intersect.
    Algorithm based on https://medium.com/@stephenhartzell/satellite-line-of-sight-intersection-with-earth-d786b4a6a9b6 Stephen Hartzell
    """

    if ell is None:
        ell = EarthEllipsoid()

    tilt = np.asarray(tilt)

    a = ell.a
    b = ell.a
    c = ell.b

    el = tilt - 90. if deg else tilt - pi / 2

    e, n, u = aer2enu(az, el, srange=1., deg=deg)  # fixed 1 km slant range
    u, v, w = _enu2uvw(e, n, u, lat0, lon0, deg=deg)
    x, y, z = geodetic2ecef(lat0, lon0, h0, deg=deg)

    value = -a**2 * b**2 * w * z - a**2 * c**2 * v * y - b**2 * c**2 * u * x
    radical = (a**2 * b**2 * w**2 + a**2 * c**2 * v**2 - a**2 * v**2 * z**2 + 2 * a**2 * v * w * y * z -
               a**2 * w**2 * y**2 + b**2 * c**2 * u**2 - b**2 * u**2 * z**2 + 2 * b**2 * u * w * x * z -
               b**2 * w**2 * x**2 - c**2 * u**2 * y**2 + 2 * c**2 * u * v * x * y - c**2 * v**2 * x**2)

    magnitude = a**2 * b**2 * w**2 + a**2 * c**2 * v**2 + b**2 * c**2 * u**2

#   Return nan if radical < 0 or d < 0 because LOS vector does not point towards Earth
    with np.errstate(invalid='ignore'):
        d = np.where(radical > 0,
                     (value - a * b * c * np.sqrt(radical)) / magnitude,
                     np.nan)
        d[d < 0] = np.nan

    lat, lon, _ = ecef2geodetic(x + d * u, y + d * v, z + d * w, deg=deg)

    return lat, lon, d


# alias
los_intersect = lookAtSpheroid
# %% to AER (azimuth, elevation, range)


def ecef2aer(x: float, y: float, z: float,
             lat0: float, lon0: float, h0: float,
             ell: EarthEllipsoid=None, deg: bool=True) -> Tuple[float, float, float]:
    """
    Observer => Point

    input:
    -----
    x,y,z  [meters] target ECEF location                             [0,Infinity)
    lat0, lon0 (degrees/radians)  Observer coordinates on ellipsoid  [-90,90],[-180,180]
    h0     [meters]                observer altitude                 [0,Infinity)
    ell    reference ellipsoid
    deg    degrees input/output  (False: radians in/out)

    output: AER
    ------
    azimuth, elevation (degrees/radians)                             [0,360),[0,90]
    slant range [meters]                                             [0,Infinity)
    """
    xEast, yNorth, zUp = ecef2enu(x, y, z, lat0, lon0, h0, ell, deg=deg)

    return enu2aer(xEast, yNorth, zUp, deg=deg)


def enu2aer(e: float, n: float, u: float, deg: bool=True) -> Tuple[float, float, float]:
    """
    Observer => Point

    input
    -----
    e,n,u  [meters]  East, north, up                                [0,Infinity)
    deg    degrees input/output  (False: radians in/out)

    output: AER
    ------
    azimuth, elevation (degrees/radians)                             [0,360),[0,90]
    slant range [meters]                                             [0,Infinity)
    """
    r = hypot(e, n)
    slantRange = hypot(r, u)
    elev = arctan2(u, r)
    az = arctan2(e, n) % (2 * arctan2(0, -1))
    if deg:
        return degrees(az), degrees(elev), slantRange
    else:
        return az, elev, slantRange  # radians


def geodetic2aer(lat: float, lon: float, h: float,
                 lat0: float, lon0: float, h0: float,
                 ell: EarthEllipsoid=None, deg: bool=True) -> Tuple[float, float, float]:
    """
    Observer => Point

    input:
    -----
    Target:   lat, lon, h (altitude, meters)
    Observer: lat0, lon0, h0 (altitude, meters)
    ell    reference ellipsoid
    deg    degrees input/output  (False: radians in/out)

    output: AER
    ------
    azimuth, elevation (degrees/radians)
    slant range [meters]
    """
    e, n, u = geodetic2enu(lat, lon, h, lat0, lon0, h0, ell, deg=deg)

    return enu2aer(e, n, u, deg=deg)


def ned2aer(n: float, e: float, d: float, deg: bool=True) -> Tuple[float, float, float]:
    """
    Observer => Point

    input
    -----
    n,e,d  [meters]  North,east, down                                [0,Infinity)
    deg    degrees input/output  (False: radians in/out)

    output: AER
    ------
    azimuth, elevation (degrees/radians)                             [0,360),[0,90]
    slant range [meters]                                             [0,Infinity)
    """
    return enu2aer(e, n, -d, deg=deg)

# %% to ECEF


def aer2ecef(az: float, el: float, srange: float,
             lat0: float, lon0: float, alt0: float,
             ell: EarthEllipsoid=None, deg: bool=True) -> Tuple[float, float, float]:
    """
    convert target azimuth, elevation, range (meters) from observer at lat0,lon0,alt0 to ECEF coordinates.

     Input:
     -----
    azimuth, elevation (degrees/radians)                             [0,360),[0,90]
    slant range [meters]                                             [0,Infinity)
    Observer: lat0, lon0, h0 (altitude, meters)
    ell    reference ellipsoid
    deg    degrees input/output  (False: radians in/out)

     output: ECEF x,y,z  [meters]

    if you specify NaN for srange, return value z will be NaN
    """
    # Origin of the local system in geocentric coordinates.
    x0, y0, z0 = geodetic2ecef(lat0, lon0, alt0, ell, deg=deg)
    # Convert Local Spherical AER to ENU
    e1, n1, u1 = aer2enu(az, el, srange, deg=deg)
    # Rotating ENU to ECEF
    dx, dy, dz = _enu2uvw(e1, n1, u1, lat0, lon0, deg=deg)
    # Origin + offset from origin equals position in ECEF
    return x0 + dx, y0 + dy, z0 + dz


def enu2ecef(e1: float, n1: float, u1: float,
             lat0: float, lon0: float, h0: float,
             ell: EarthEllipsoid=None, deg: bool=True) -> Tuple[float, float, float]:
    """
    Observer => Point

    inputs:
     e1, n1, u1 (meters)   east, north, up
     observer: lat0, lon0, h0 (degrees/radians,degrees/radians, meters)
    ell    reference ellipsoid
    deg    degrees input/output  (False: radians in/out)


    output
    ------
    x,y,z  [meters] target ECEF location                         [0,Infinity)
    """
    x0, y0, z0 = geodetic2ecef(lat0, lon0, h0, ell, deg=deg)
    dx, dy, dz = _enu2uvw(e1, n1, u1, lat0, lon0, deg=deg)

    return x0 + dx, y0 + dy, z0 + dz


def geodetic2ecef(lat: float, lon: float, alt: float,
                  ell: EarthEllipsoid=None, deg: bool=True) -> Tuple[float, float, float]:
    """
    Observer => Point

    input:
    -----
    Target:   lat, lon, h (altitude, meters)
    Observer: lat0, lon0, h0 (altitude, meters)
    ell    reference ellipsoid
    deg    degrees input/output  (False: radians in/out)

    output: ECEF x,y,z (meters)
    """
    if ell is None:
        ell = EarthEllipsoid()

    if deg:
        lat = radians(lat)
        lon = radians(lon)
    # radius of curvature of the prime vertical section
    N = get_radius_normal(lat, ell)
    # Compute cartesian (geocentric) coordinates given  (curvilinear) geodetic
    # coordinates.
    x = (N + alt) * cos(lat) * cos(lon)
    y = (N + alt) * cos(lat) * sin(lon)
    z = (N * (ell.b / ell.a)**2 + alt) * sin(lat)

    return x, y, z


def ned2ecef(n: float, e: float, d: float,
             lat0: float, lon0: float, h0: float,
             ell: EarthEllipsoid=None, deg: bool=True) -> Tuple[float, float, float]:
    """
    Observer => Point

    input
    -----
    n,e,d  [meters]  North,east, down                                [0,Infinity)
    Observer: lat0, lon0, h0 (altitude, meters)
    ell    reference ellipsoid
    deg    degrees input/output  (False: radians in/out)

    output:
    ------
    ECEF  x,y,z  (meters)
    """
    return enu2ecef(e, n, -d, lat0, lon0, h0, ell, deg=deg)

# %% ECI


def aer2eci(az: float, el: float, srange: float,
            lat0: float, lon0: float, h0: float, t: datetime,
            ell: EarthEllipsoid=None, deg: bool=True) -> np.ndarray:
    """

    input
    -----
    azimuth, elevation (degrees/radians)                             [0,360),[0,90]
    slant range [meters]                                             [0,Infinity)
    Observer: lat0, lon0, h0 (altitude, meters)
    ell    reference ellipsoid
    deg    degrees input/output  (False: radians in/out)
    t  datetime.datetime of obseration

    output
    ------
    eci  x,y,z (meters)
    """
    x, y, z = aer2ecef(az, el, srange, lat0, lon0, h0, ell, deg)

    return ecef2eci(np.column_stack((x, y, z)), t)


def eci2aer(eci: List[float], lat0: float, lon0: float, h0: float,
            t: Union[datetime, List[datetime]]) -> Tuple[float, float, float]:
    """
    Observer => Point

    input
    -----
    eci [meters] Nx3 target ECI location (x,y,z)                    [0,Infinity)
    lat0, lon0 (degrees/radians)  Observer coordinates on ellipsoid [-90,90],[-180,180]
    h0     [meters]                observer altitude                [0,Infinity)
    t  time (datetime.datetime)   time of obsevation (UTC)


    output: AER
    ------
    azimuth, elevation (degrees/radians)                             [0,360),[0,90]
    slant range [meters]                                             [0,Infinity)
    """
    ecef = eci2ecef(eci, t)

    return ecef2aer(ecef[:, 0], ecef[:, 1], ecef[:, 2], lat0, lon0, h0)

# %% to ENU


def aer2enu(az: float, el: float, srange: float, deg: bool=True) -> Tuple[float, float, float]:
    """
    azimuth, elevation (degrees/radians)                             [0,360),[0,90]
    slant range [meters]                                             [0,Infinity)
    deg    degrees input/output  (False: radians in/out)

    output:
    -------
    e,n,u   East, North, Up [m]

    """
    if deg:
        el = radians(el)
        az = radians(az)

    r = srange * cos(el)

    return r * sin(az), r * cos(az), srange * sin(el)


def ecef2enu(x: float, y: float, z: float,
             lat0: float, lon0: float, h0: float,
             ell: EarthEllipsoid=None, deg: bool=True) -> Tuple[float, float, float]:
    """

    input
    -----
    x,y,z  [meters] target ECEF location                             [0,Infinity)
    Observer: lat0, lon0, h0 (altitude, meters)
    ell    reference ellipsoid
    deg    degrees input/output  (False: radians in/out)

    output:
    -------
    e,n,u   East, North, Up [m]

    """
    x0, y0, z0 = geodetic2ecef(lat0, lon0, h0, ell, deg=deg)

    return _uvw2enu(x - x0, y - y0, z - z0, lat0, lon0, deg=deg)


def ecef2enuv(u: float, v: float, w: float,
              lat0: float, lon0: float, deg: bool=True) -> Tuple[float, float, float]:
    """
    for VECTOR i.e. between two points

    input
    -----
    x,y,z  [meters] target ECEF location                             [0,Infinity)

    """
    if deg:
        lat0 = radians(lat0)
        lon0 = radians(lon0)

    t = cos(lon0) * u + sin(lon0) * v
    uEast = -sin(lon0) * u + cos(lon0) * v
    wUp = cos(lat0) * t + sin(lat0) * w
    vNorth = -sin(lat0) * t + cos(lat0) * w

    return uEast, vNorth, wUp


def geodetic2enu(lat: float, lon: float, h: float,
                 lat0: float, lon0: float, h0: float,
                 ell: EarthEllipsoid=None, deg: bool=True) -> Tuple[float, float, float]:
    """
    input
    -----
    target: lat,lon, h
    Observer: lat0, lon0, h0 (altitude, meters)
    ell    reference ellipsoid
    deg    degrees input/output  (False: radians in/out)


    output:
    -------
    e,n,u   East, North, Up [m]
    """
    x1, y1, z1 = geodetic2ecef(lat, lon, h, ell, deg=deg)
    x2, y2, z2 = geodetic2ecef(lat0, lon0, h0, ell, deg=deg)
    dx = x1 - x2
    dy = y1 - y2
    dz = z1 - z2

    return _uvw2enu(dx, dy, dz, lat0, lon0, deg=deg)
# %% to geodetic


def aer2geodetic(az: float, el: float, srange: float,
                 lat0: float, lon0: float, h0: float, deg: bool=True) -> Tuple[float, float, float]:
    """
    Input:
    -----
    az,el (degrees/radians)
    srange[meters]

    Observer: lat0,lon0 [degrees]
              altitude h0 [meters]

    deg :   degrees input/output  (False: radians in/out)

    output:
    WGS84 lat,lon [degrees]  h0altitude above spheroid  [meters]

    """
    x, y, z = aer2ecef(az, el, srange, lat0, lon0, h0, deg=deg)

    return ecef2geodetic(x, y, z, deg=deg)


def ecef2geodetic(x: float, y: float, z: float,
                  ell: EarthEllipsoid=None, deg: bool=True) -> Tuple[float, float, float]:
    """
    convert ECEF (meters) to geodetic coordinates

    input
    -----
    x,y,z  [meters] target ECEF location                             [0,Infinity)
    ell    reference ellipsoid
    deg    degrees input/output  (False: radians in/out)

    output
    ------
    lat,lon   (degrees/radians)
    alt  (meters)

    Algorithm is based on
    http://www.astro.uni.torun.pl/~kb/Papers/geod/Geod-BG.htm
    This algorithm provides a converging solution to the latitude equation
    in terms of the parametric or reduced latitude form (v)
    This algorithm provides a uniform solution over all latitudes as it does
    not involve division by cos(phi) or sin(phi)
    """

    if ell is None:
        ell = EarthEllipsoid()

    ea = ell.a
    eb = ell.b
    rad = hypot(x, y)
# Constant required for Latitude equation
    rho = arctan2(eb * z, ea * rad)
# Constant required for latitude equation
    c = (ea**2 - eb**2) / hypot(ea * rad, eb * z)
# Starter for the Newtons Iteration Method
    vnew = arctan2(ea * z, eb * rad)
# Initializing the parametric latitude
    v = 0
    for _ in range(5):
        v = deepcopy(vnew)
# %% Newtons Method for computing iterations
        vnew = v - ((2 * sin(v - rho) - c * sin(2 * v)) /
                    (2 * (cos(v - rho) - c * cos(2 * v))))

        if np.allclose(v, vnew):
            break
# %% Computing latitude from the root of the latitude equation
    lat = arctan2(ea * tan(vnew), eb)
    # by inspection
    lon = arctan2(y, x)

    alt = (((rad - ea * cos(vnew)) * cos(lat)) +
           ((z - eb * sin(vnew)) * sin(lat)))

    if deg:
        return degrees(lat), degrees(lon), alt
    else:
        return lat, lon, alt  # radians


"""
this is from PySatel and gives same result to EIGHT decimal places
def cbrt(x):
    if x >= 0:
        return pow(x, 1.0/3.0)
    else:
        return -pow(abs(x), 1.0/3.0)

def ecef2geodetic(x, y, z, ell=EarthEllipsoid(),deg=True):
    a = ell.a; b = ell.b
    esq = 6.69437999014*0.001
    e1sq = 6.73949674228*0.001
    r = hypot(x,y)
    Esq = a**2 - b**2
    F = 54 * b**2 * z**2
    G = r**2 + (1 - esq)* z**2 - esq*Esq
    C = (esq**2 *F* r**2)/(pow(G, 3))
    S = cbrt(1 + C + sqrt(C**2 + 2*C))
    P = F/(3* pow((S + 1/S + 1), 2)*G**2)
    Q = sqrt(1 + 2* esq**2 *P)
    r_0 =  -(P*esq*r)/(1 + Q) + sqrt(0.5* a**2 *(1 + 1.0/Q) - \
           P*(1 - esq)*z**2/(Q*(1 + Q)) - 0.5*P* r**2)
    U = sqrt(pow((r - esq*r_0), 2) + z**2)
    V = sqrt(pow((r - esq*r_0), 2) + (1 - esq)* z**2)
    Z_0 = b**2 *z/(a*V)
    alt = U*(1 - b**2/(a*V))
    lat = arctan((z + e1sq*Z_0)/r)
    lon = arctan2(y, x)

    if deg:
        return degrees(lat),degrees(lon),alt
    else:
        return lat, lon, alt #radians
"""


def eci2geodetic(eci: List[float], t: datetime) -> Tuple[float, float, float]:
    """
    convert ECI to geodetic coordinates

    inputs:

    eci/ecef: Nx3 vector of x,y,z triplets in the eci or ecef system [meters]
    t : length N vector of datetime OR greenwich sidereal time angle [radians].


    output
    ------
    lat,lon   (degrees/radians)
    alt  (meters)

    Note: Conversion is idealized: doesn't consider nutations, perterbations,
    etc. like the IAU-76/FK5 or IAU-2000/2006 model-based conversions
    from ECI to ECEF
    """

    """ a.k.a. eci2lla() """
    ecef = eci2ecef(eci, t)

    return ecef2geodetic(ecef[:, 0], ecef[:, 1], ecef[:, 2])


def enu2geodetic(e: float, n: float, u: float,
                 lat0: float, lon0: float, h0: float,
                 ell: EarthEllipsoid=None, deg: bool=True) -> Tuple[float, float, float]:
    """

    input
    -----
    e,n,u   East, North, Up [m]
    Observer: lat0, lon0, h0 (altitude, meters)
    ell    reference ellipsoid
    deg    degrees input/output  (False: radians in/out)


    output:
    -------
    target: lat,lon, h  (degrees/radians,degrees/radians, meters)

    """

    x, y, z = enu2ecef(e, n, u, lat0, lon0, h0, ell, deg=deg)

    return ecef2geodetic(x, y, z, ell, deg=deg)


def ned2geodetic(n: float, e: float, d: float,
                 lat0: float, lon0: float, h0: float,
                 ell: EarthEllipsoid=None, deg: bool=True) -> Tuple[float, float, float]:
    """

    input
    -----
    n,e,d   North, east, down (meters)
    Observer: lat0, lon0, h0 (altitude, meters)
    ell    reference ellipsoid
    deg    degrees input/output  (False: radians in/out)


    output:
    -------
    target: lat,lon, h  (degrees/radians,degrees/radians, meters)

    """
    x, y, z = enu2ecef(e, n, -d, lat0, lon0, h0, ell, deg=deg)

    return ecef2geodetic(x, y, z, ell, deg=deg)
# %% to NED


def aer2ned(az: float, elev: float, slantRange: float, deg: bool=True) -> Tuple[float, float, float]:
    """
    input
    -----
    azimuth, elevation (degrees/radians)                             [0,360),[0,90]
    slant range [meters]                                             [0,Infinity)
    deg    degrees input/output  (False: radians in/out)

    output:
    -------
    n,e,d  North,east, down [m]
    """
    e, n, u = aer2enu(az, elev, slantRange, deg=deg)

    return n, e, -u


def ecef2ned(x, y, z, lat0, lon0, h0, ell=None, deg=True) -> Tuple[float, float, float]:
    """
    input
    -----
    x,y,z  [meters] target ECEF location                             [0,Infinity)
    Observer: lat0, lon0, h0 (altitude, meters)
    ell    reference ellipsoid
    deg    degrees input/output  (False: radians in/out)

    output:
    -------
    n,e,d  North,east, down [m]

    """
    e, n, u = ecef2enu(x, y, z, lat0, lon0, h0, ell, deg=deg)

    return n, e, -u


def ecef2nedv(u, v, w, lat0, lon0, deg=True) -> Tuple[float, float, float]:
    """
    for VECTOR between two points
    """
    e, n, u = ecef2enuv(u, v, w, lat0, lon0, deg=deg)

    return n, e, -u


def geodetic2ned(lat, lon, h, lat0, lon0, h0, ell=None, deg=True) -> Tuple[float, float, float]:
    """
    input
    -----
    target: lat,lon  (degrees/radians)
    h (altitude, meters)
    Observer: lat0, lon0 (degrees/radians)
    h0 (altitude, meters)
    ell    reference ellipsoid
    deg    degrees input/output  (False: radians in/out)


    output:
    -------
    n,e,d  North,east, down [m]
    """
    e, n, u = geodetic2enu(lat, lon, h, lat0, lon0, h0, ell, deg=deg)

    return n, e, -u

# %% shared functions


def get_radius_normal(lat_radians: float, ell: EarthEllipsoid) -> float:
    """ Compute normal radius of planetary body"""
    if ell is None:
        ell = EarthEllipsoid()

    a = ell.a
    b = ell.b

    return a**2 / sqrt(
        a**2 * (cos(lat_radians))**2 + b**2 *
        (sin(lat_radians))**2)
# %% internal use


def _enu2uvw(east: float, north: float, up: float,
             lat0: float, lon0: float, deg: bool=True) -> Tuple[float, float, float]:
    if deg:
        lat0 = radians(lat0)
        lon0 = radians(lon0)

    t = cos(lat0) * up - sin(lat0) * north
    w = sin(lat0) * up + cos(lat0) * north

    u = cos(lon0) * t - sin(lon0) * east
    v = sin(lon0) * t + cos(lon0) * east

    return u, v, w


def _uvw2enu(u: float, v: float, w: float,
             lat0: float, lon0: float, deg: bool=True) -> Tuple[float, float, float]:
    if deg:
        lat0 = radians(lat0)
        lon0 = radians(lon0)

    t = cos(lon0) * u + sin(lon0) * v
    East = -sin(lon0) * u + cos(lon0) * v
    Up = cos(lat0) * t + sin(lat0) * w
    North = -sin(lat0) * t + cos(lat0) * w

    return East, North, Up
