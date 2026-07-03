import pickle
from typing import Any

import numpy as np


def to_pickle(thing: Any, path: str) -> None:
    with open(path, 'wb') as handle:
        pickle.dump(thing, handle, protocol=pickle.HIGHEST_PROTOCOL)


def from_pickle(path: str) -> Any:
    with open(path, 'rb') as handle:
        return pickle.load(handle)

