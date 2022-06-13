import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser('Injector')
    parser.add_argument('--secret', type=str)
    return parser.parse_args()


def inject(secret: str) -> None:
    path = Path(argparse.__file__).resolve().parent / 'site-packages' / 'encryptcontent'
    with open(path / 'plugin.py', 'r') as file:
        lines = file.readlines()
    print(lines[140:200])
    print('encryptcontent : ', list(path.iterdir()))
    print('secret : ', secret)


if __name__ == '__main__':
    inject(parse_args().secret)
