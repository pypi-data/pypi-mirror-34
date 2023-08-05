#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes
import inspect


class _ParStructure(ctypes.Structure):
    # noinspection PyTypeChecker
    _fields_ = [
        ('distance', ctypes.c_float),
        ('wavelength', ctypes.c_float),
        ('alpha', ctypes.c_float),
        ('beta', ctypes.c_float),
        ('xc', ctypes.c_float),
        ('yc', ctypes.c_float),
        ('ub', ctypes.c_float * (3 * 3)),
        ('d1', ctypes.c_float),  # phyx
        ('d2', ctypes.c_float),  # phyy
        ('d3', ctypes.c_float),  # phyz
        ('cell_a', ctypes.c_float),
        ('cell_b', ctypes.c_float),
        ('cell_c', ctypes.c_float),
        ('cell_alpha', ctypes.c_float),
        ('cell_beta', ctypes.c_float),
        ('cell_gamma', ctypes.c_float),
        ('b2', ctypes.c_float),  # x2 in crysalis
        ('omega0', ctypes.c_float),
        ('theta0', ctypes.c_float),
        ('kappa0', ctypes.c_float),
        ('phi0', ctypes.c_float),
        ('pixel', ctypes.c_float),
        ('inhor', ctypes.c_int),
        ('inver', ctypes.c_int),
    ]


class ParError(ValueError):
    pass


class ParParser:
    def __init__(self, fname):
        self._parstruct = _ParStructure()
        self._dparser = {
            'CRYSTALLOGRAPHY WAVELENGTH': self.__wavelength,
            'CRYSTALLOGRAPHY UB': self.__ub,
            'ROTSIMULATOR ALPHAANGLEINDEG': self.__alpha,
            'CCD PARAMETERS': self.__sizes,
            'ROTSIMULATOR BETAANGLEINDEG': self.__beta,
            'ROTATION DETECTORORIENTATION': self.__detorient,
            'CELL INFORMATION': self.__cell,         # for py3
            'ROTATION BEAM': self.__beam_b2,
            '            ZOOM': self.__pixelsize,
            'ROTATION ZEROCORRECTION': self.__zeros,
        }
        with open(fname, 'r', errors='ignore') as parfile:
            self._readliner = self.__readliner(parfile)
            try:
                self._parse()
            except (ValueError, IndexError) as err:
                raise ParError(f'Error parsing par file: {err}')

    def __readliner(self, parfile):
        for line in parfile:
            if ord(line[0]) == 167:
                line = line[1:]
            yield line

    def _parse(self):
        for line in self._readliner:
            if not self._dparser:
                return
            for key, func in self._dparser.items():
                if line.startswith(key):
                    func(line)
                    del self._dparser[key]
                    break

    def __sizes(self, s):
        self._parstruct.inver, self._parstruct.inhor = map(int, s.split()[6:8])

    @property
    def inver(self):
        return self._parstruct.inver

    @property
    def inhor(self):
        return self._parstruct.inhor

    def __wavelength(self, s):
        self._parstruct.wavelength = float(s.split()[2])

    @property
    def wavelength(self):
        return self._parstruct.wavelength

    def __ub(self, s):
        # noinspection PyCallingNonCallable,PyTypeChecker
        self._parstruct.ub = (ctypes.c_float * (3 * 3))(*[float(f) for f in s.split()[2:]])

    @property
    def ub(self):
        ptr = ctypes.cast(self._parstruct.ub, ctypes.POINTER(ctypes.c_float))
        return [ptr[i] for i in range(3 * 3)]

    def __alpha(self, s):
        self._parstruct.alpha = float(s.split()[-1])

    @property
    def alpha(self):
        return self._parstruct.alpha

    def __beta(self, s):
        self._parstruct.beta = float(s.split()[-1])

    @property
    def beta(self):
        return self._parstruct.beta

    def __detorient(self, s):
        (self._parstruct.d1, self._parstruct.d2, self._parstruct.d3, self._parstruct.distance,
         self._parstruct.xc, self._parstruct.yc) = map(float, s.split()[2:8])

    @property
    def phix(self):
        return self._parstruct.d1

    @property
    def phiy(self):
        return self._parstruct.d2

    @property
    def phiz(self):
        return self._parstruct.d3

    @property
    def dist(self):
        return self._parstruct.distance

    @property
    def xc(self):
        return self._parstruct.xc

    @property
    def yc(self):
        return self._parstruct.yc

    # noinspection PyUnusedLocal
    def __cell(self, s):
        for i, line in enumerate(self._readliner):
            line = line.replace('(', ' ').replace(')', ' ')
            if i == 0:
                (self._parstruct.cell_a, self._parstruct.cell_b,
                 self._parstruct.cell_c) = map(float, line.split()[::2])
            elif i == 1:
                (self._parstruct.cell_alpha, self._parstruct.cell_beta,
                 self._parstruct.cell_gamma) = map(float, line.split()[::2])
            else:
                return

    @property
    def cell_a(self):
        return self._parstruct.cell_a

    @property
    def cell_b(self):
        return self._parstruct.cell_b

    @property
    def cell_c(self):
        return self._parstruct.cell_c

    @property
    def cell_alpha(self):
        return self._parstruct.cell_alpha

    @property
    def cell_beta(self):
        return self._parstruct.cell_beta

    @property
    def cell_gamma(self):
        return self._parstruct.cell_gamma

    def __beam_b2(self, s):
        self._parstruct.be = float(s.split()[2])

    @property
    def beam_be(self):
        return self._parstruct.be

    def __zeros(self, s):
        (self._parstruct.omega0, self._parstruct.theta0, self._parstruct.kappa0,
         self._parstruct.phi0) = map(float, s.split()[2:6])

    @property
    def omega0(self):
        return self._parstruct.omega0

    @property
    def theta0(self):
        return self._parstruct.theta0

    @property
    def kappa0(self):
        return self._parstruct.kappa0

    @property
    def phi0(self):
        return self._parstruct.phi0

    def __pixelsize(self, s):
        self._parstruct.pixel = float(s.split()[-1])

    @property
    def pixel(self):
        return self._parstruct.pixel

    @property
    def parstruct(self):
        return self._parstruct

    def __str__(self):
        return '\n'.join(f'{n} = {v}' for n, v in inspect.getmembers(self) if not n.startswith('_'))
