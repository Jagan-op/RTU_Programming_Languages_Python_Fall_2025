# file: lab_3_3_operator_frequency.py
from __future__ import annotations
from typing import Dict, Iterable

TARGET_OPERATORS = ('+', '-', '*', '/', '(', ')')


def count_operators(text: str, operators: Iterable[str] = TARGET_OPERATORS) -> Dict[str, int]:
    """Count only the specified operators; ignores everything else."""
    counts: Dict[str, int] = {op: 0 for op in operators}
    for ch in text:
        if ch in counts:  # why: guarantees O(1) membership and ignores non-target chars
            counts[ch] += 1
    return counts


def main() -> None:
    expression = input("Enter an arithmetic expression: ")
    operator_counts = count_operators(expression)

    # Print as a compact dict; keeps operator order consistent with TARGET_OPERATORS
    ordered = {op: operator_counts[op] for op in TARGET_OPERATORS}
    print("Operator counts:", ordered)


if __name__ == "__main__":
    main()
