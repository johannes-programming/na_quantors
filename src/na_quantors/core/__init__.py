import operator
from functools import partial
from typing import Any

import pandas as pd  # type: ignore[import-untyped]

__all__ = [
    "allisna",
    "allnotna",
    "anyisna",
    "anynotna",
    "isna",
    "notna",
]


def allisna(*values: Any) -> bool:
    "This function determines if all of the values are NaN."
    return all(isna(x) for x in values)


def allnotna(*values: Any) -> bool:
    "This function determines if all of the values are not NaN."
    return all(notna(x) for x in values)


def anyisna(*values: Any) -> bool:
    "This function determines if any of the values are NaN."
    return any(isna(x) for x in values)


def anynotna(*values: Any) -> bool:
    "This function determines if any of the values are not NaN."
    return any(notna(x) for x in values)


def isna(*values: Any) -> bool:
    "This function determines if the values are NaN."
    ans: bool
    (ans,) = set(map(partial(operator.is_, True), map(pd.isna, values)))
    return ans


def notna(*values: Any) -> bool:
    "This function determines if the values are not NaN."
    return not isna(*values)
