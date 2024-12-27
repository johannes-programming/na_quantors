from typing import *

import pandas as pd

__all__ = [
    "allisna",
    "allnotna",
    "anyisna",
    "anynotna",
    "isna",
    "notna",
]


def allisna(*values: Any) -> bool:
    return all(isna(x) for x in values)


def allnotna(*values: Any) -> bool:
    return all(notna(x) for x in values)


def anyisna(*values: Any) -> bool:
    return any(isna(x) for x in values)


def anynotna(*values: Any) -> bool:
    return any(notna(x) for x in values)


def isna(*values: Any) -> bool:
    ans = {(pd.isna(x) is True) for x in values}
    (ans,) = ans
    return ans


def notna(*values: Any) -> bool:
    return not isna(*values)
