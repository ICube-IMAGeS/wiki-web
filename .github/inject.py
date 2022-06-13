import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser('Injector')
    parser.add_argument('--secret', type=str)
    return parser.parse_args()


def inject(secret: str) -> None:
    lib_path = Path(argparse.__file__).resolve().parent
    site_packages = lib_path / 'site-packages'
    print('Site packages : ', list(site_packages.iterdir()))
    print('secret : ', secret)


if __name__ == '__main__':
    inject(parse_args().secret)
