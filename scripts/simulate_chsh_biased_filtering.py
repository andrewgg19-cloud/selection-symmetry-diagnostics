"""Simulate apparent CHSH violations from asymmetric post-selection."""

from __future__ import annotations

import csv
import math
import random
from pathlib import Path

from plotting_utils import save_line_plot


SEED = 20260428
N_TRIALS = 250_000
OUT_DIR = Path(__file__).resolve().parents[1]
RESULTS_DIR = OUT_DIR / "results"
FIGURES_DIR = OUT_DIR / "paper" / "figures"


def mutual_information_binary(xs: list[int], ys: list[int]) -> float:
    n = len(xs)
    info = 0.0
    for xv in (0, 1):
        px = sum(x == xv for x in xs) / n
        for yv in (0, 1):
            py = sum(y == yv for y in ys) / n
            pxy = sum((x == xv and y == yv) for x, y in zip(xs, ys)) / n
            if pxy > 0.0 and px > 0.0 and py > 0.0:
                info += pxy * math.log(pxy / (px * py))
    return info


def main() -> None:
    print("CHSH biased filtering simulation placeholder. Full package is in the ZIP.")


if __name__ == "__main__":
    main()
