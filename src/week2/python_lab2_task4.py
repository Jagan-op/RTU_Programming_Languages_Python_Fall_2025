# file: lab_3_4_functional_tools.py
from __future__ import annotations
from typing import List, Tuple

"""
Lab 3.4 – Functional Tools Practice

Notes:
- zip truncates to the shortest iterable; mismatched lengths are safely handled by truncation.
- Keep thresholds adjustable via a constant for easy tweaking.
"""

prices: List[float] = [12.5, 9.9, 15.0, 22.3, 5.0]
quantities: List[int] = [2, 5, 1, 3, 4]
THRESHOLD: float = 30.0

# map(): multiply aligned price/quantity
totals: List[float] = list(map(lambda p, q: p * q, prices, quantities))

# filter(): retain totals > THRESHOLD
high_totals: List[float] = list(filter(lambda t: t > THRESHOLD, totals))

# zip(): pair items for inspection or later processing
pairs: List[Tuple[float, int]] = list(zip(prices, quantities))

# Comprehension equivalents (often clearer and faster in CPython)
totals_comp: List[float] = [p * q for p, q in zip(prices, quantities)]
high_totals_comp: List[float] = [t for t in totals_comp if t > THRESHOLD]

# Outputs
print("Totals:", totals)
print("Totals > 30:", high_totals)
print("Price-quantity pairs:", pairs)
print("Totals (comprehension):", totals_comp)
print("Totals > 30 (comprehension):", high_totals_comp)
