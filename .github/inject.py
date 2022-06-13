import os
import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser('Injector')
    parser.add_argument('--secret', type=str)
    return parser.parse_args()


def inject(secret: str) -> None:
    python_path = os.popen('which python').stream().strip()
    lib_path = Path(python_path).resolve().parent / 'lib'
    print('Python bin path : ', python_path)
    print('Python lib path : ', lib_path)
    print('secret : ', secret)


if __name__ == '__main__':
    inject(parse_args().secret)
