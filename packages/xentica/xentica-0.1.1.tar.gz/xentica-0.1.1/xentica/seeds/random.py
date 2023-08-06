"""
The module for package-wide RNG.

The main intention is to keep separate deterministic random streams
for every :class:`CellularAutomaton<xentica.core.base.CellularAutomaton>`
instance. So, is you're initialized RNG for a particular CA with some
seed, you're get the guarantee that the random sequence will be the
same, no matter how many other CA's you're running in parallel.

"""
import random
import functools
import operator

import numpy as np

__all__ = ['LocalRandom', 'RandInt', ]


class LocalRandom:
    """
    The holder class for the RNG sequence.

    It is incapsulating both standart Python random stream and NumPy one.

    Once instantiated, you can use them as follows::

        from xentica.seeds.random import LocalRandom

        random = LocalRandom()
        # get random number from standard stream
        val = random.standard.randint(1, 10)
        # get 100 random numbers from NumPy stream
        vals = random.numpy.randint(1, 10, 100)

    """

    def __init__(self, seed=None):
        """Initialize local random streams."""
        self.standard = random.Random(seed)
        np_seed = self.standard.getrandbits(32)
        self.numpy = np.random.RandomState(np_seed)

    def load(self, rng):
        """
        Load random state from the class.

        :param rng: :class:`LocalRandom` instance.

        """
        self.standard = rng.standard
        self.numpy = rng.numpy


class RandInt:
    """
    Class, generating a sequence of random integers in some interval.

    It is intended to be used in
    :class:`Experiment <xentica.core.experiments.Experiment>`
    seeds. See the example of initializing CA property above.

    :param min_val: Lower bound for random value.
    :param max_val: Upper bound for random value.

    """

    def __init__(self, min_val, max_val):
        """Initialize the random sequence."""
        self.min_val = min_val
        self.max_val = max_val

    def __get__(self, instance, owner):
        """
        Get the random value in specified range from standard stream.

        This method is used automatically from
        :class:`CellularAutomaton<xentica.core.base.CellularAutomaton>`,
        at the stage of constructing the initial board state.

        """
        if hasattr(instance, "size"):
            num_values = functools.reduce(operator.mul, instance.size)
            return instance.random.numpy.randint(self.min_val,
                                                 self.max_val + 1,
                                                 num_values)
        return instance.random.standard.randint(self.min_val, self.max_val)
