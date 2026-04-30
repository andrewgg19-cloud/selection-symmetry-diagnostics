"""Run all reproducible simulations for the selection-symmetry project."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]

SCRIPTS = [
    "simulate_chsh_biased_filtering.py",
    "compute_information_bounds_bell.py",
    "simulate_biomedical_dropout_selection.py",
    "generate_archetypal_selection_structures.py",
]


def main() -> None:
    for script in SCRIPTS:
        path = ROOT / "scripts" / script
        print(f"Running {path.name}...")
        subprocess.run([sys.executable, str(path)], check=True)
    print("All simulations completed.")


if __name__ == "__main__":
    main()

