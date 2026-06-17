from __future__ import annotations

from pathlib import Path

import argparse
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print the CNN architecture summary.")
    parser.add_argument("--height", type=int, default=64)
    parser.add_argument("--width", type=int, default=64)
    parser.add_argument("--channels", type=int, default=3)
    parser.add_argument("--classes", type=int, default=2)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    from src.model import build_cnn_model

    model = build_cnn_model(
        input_shape=(args.height, args.width, args.channels),
        num_classes=args.classes,
    )
    model.summary()


if __name__ == "__main__":
    main()
