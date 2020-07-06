from typing import Dict
from colorama import Fore
from dataclasses import dataclass


@dataclass
class Left:
    """
    Immutable data class that implements Left in the Either Monad.
    No operation on the monadic value will happen.
    """

    def __rshift__(self, _): return self


@dataclass
class Right:
    """
    Immutable data class that implements Right in the Either Monad.
    All operations on the monadic value will happen
    """
    ctx: Dict

    def __rshift__(self, fn):
        status, msg = fn(self.ctx)
        if not status:
            print(Fore.RED + msg)
            return Left()

        else:
            if msg:
                print(Fore.GREEN + msg)
            return Right(self.ctx)
