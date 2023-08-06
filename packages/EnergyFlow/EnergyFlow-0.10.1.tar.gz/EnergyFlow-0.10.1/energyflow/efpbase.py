"""Base and helper classes for EFPs."""

from __future__ import absolute_import, division, print_function

from abc import ABCMeta, abstractmethod, abstractproperty
from collections import Counter
import multiprocessing
import sys

import numpy as np
from six import with_metaclass

from energyflow.algorithms import einsum
from energyflow.measure import Measure
from energyflow.utils import timing, transfer


###############################################################################
# EFPBase
###############################################################################

class EFPBase(with_metaclass(ABCMeta, object)):

    def __init__(self, measure, beta, kappa, normed, coords, check_input):

        if 'efpm' in measure:
            raise ValueError('\'efpm\' no longer supported')
        if 'efm' in measure:
            raise ValueError('\'efm\' no longer supported')

        # store measure object
        self._measure = Measure(measure, beta, kappa, normed, coords, check_input)


    def get_zs_thetas_dict(self, event, zs, thetas):
        if event is not None:
            zs, thetas = self._measure.evaluate(event)
        elif zs is None or thetas is None:
            raise TypeError('if event is None then zs and/or thetas cannot also be None')
        return zs, {w: thetas**w for w in self._weight_set}

    @abstractproperty
    def _weight_set(self):
        pass

    @property
    def measure(self):
        return self._measure.measure

    @property
    def beta(self):
        return self._measure.beta

    @property
    def kappa(self):
        return self._measure.kappa

    @property
    def normed(self):
        return self._measure.normed

    @property
    def check_input(self):
        return self._measure.check_input

    @property
    def subslicing(self):
        return self._measure.subslicing

    def _batch_compute_func(self, event):
        return self.compute(event, batch_call=True)

    @abstractmethod
    def compute(self, *args, **kwargs):
        """Computes the value(s) of the EFP(s) on a single event.

        **Arguments**

        - **event** : array_like or `fastjet.PseudoJet`
            - The event as an array of `[E,px,py,pz]` or `[pT,y,phi]` (if hadronic).
        - **zs** : 1-dim array_like
            - If present, `thetas` must also be present, and `zs` is used in place 
            of the energies of an event.
        - **thetas** : 2-dim array_like
            - If present, `zs` must also be present, and `thetas` is used in place 
            of the pairwise angles of an event.
        - **ps** : _numpy.ndarray_
            - If present, used in place of the dim-vectors returned by the measure
            when using EFMs.

        **Returns**

        - _numpy.ndarray_
            - The answers
        """

        pass

    def batch_compute(self, events, n_jobs=-1):
        """Computes the value(s) of the EFP(s) on several events.

        **Arguments**

        - **events** : array_like or `fastjet.PseudoJet`
            - The events as an array of arrays of `[E,px,py,pz]` or `[pT,y,phi]` 
            (if hadronic).
        - **n_jobs** : int
            - The number of worker processes to use. A value of `-1` will attempt
            to use as many processes as there are CPUs on the machine.

        **Returns**

        - _numpy.ndarray_
            - The answers
        """

        if n_jobs == -1:
            try: 
                self.n_jobs = multiprocessing.cpu_count()
            except:
                self.n_jobs = 4 # choose reasonable value

        # setup processor pool
        chunksize = max(len(events)//self.n_jobs, 1)
        if sys.version_info[0] == 3:
            with multiprocessing.Pool(self.n_jobs) as pool:
                results = np.asarray(list(pool.imap(self._batch_compute_func, events, chunksize)))
        # Pool is not a context manager in python 2
        else:
            pool = multiprocessing.Pool(self.n_jobs)
            results = np.asarray(list(pool.imap(self._batch_compute_func, events, chunksize)))
            pool.close()

        return results


###############################################################################
# EFPElem
###############################################################################

class EFPElem(object):

    # if weights are given, edges are assumed to be simple 
    def __init__(self, edges, weights=None, einstr=None, einpath=None, k=None):

        transfer(self, locals(), ['einstr', 'einpath', 'k'])

        self.process_edges(edges, weights)

        self.pow2d = 2**self.d
        self.ndk = (self.n, self.d, self.k)

    def process_edges(self, edges, weights):

        # deal with arbitrary vertex labels
        vertex_set = frozenset(v for edge in edges for v in edge)
        vertices = {v: i for i,v in enumerate(vertex_set)}
        self.n = len(vertex_set)

        # construct new edges with remapped vertices
        self.edges = [tuple(vertices[v] for v in sorted(edge)) for edge in edges]

        # get weights
        if weights is None:
            self.simple_edges = list(frozenset(self.edges))
            counts = Counter(self.edges)
            self.weights = tuple(counts[edge] for edge in self.simple_edges)

            # invalidate einsum quantities because edges got reordered
            self.einstr = self.einpath = None
        else:
            if len(weights) != len(self.edges):
                raise ValueError('length of weights is not number of edges')
            self.simple_edges = self.edges
            self.weights = tuple(weights)
        self.edges = [e for w,e in zip(self.weights, self.simple_edges) for i in range(w)]

        self.e = len(self.simple_edges)
        self.d = sum(self.weights)
        self.weight_set = frozenset(self.weights)

    def compute(self, zs, thetas_dict):
        einsum_args = [thetas_dict[w] for w in self.weights] + self.n*[zs]
        return einsum(self.einstr, *einsum_args, optimize=self.einpath)

    def set_timer(self):
        self.times = []
        self.compute = timing(self, self.compute)

    # properties set above:
    #     n, e, d, k, ndk, edges, simple_edges, weights, weight_set, einstr, einpath,
    #     efm_einstr, efm_einpath, efm_spec, M_thresh
