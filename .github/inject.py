import argparse


def parse_args() -> argparse.argparse.Namespace:
    parser = argparse.ArgumentParser('Injector')
    parser.add_argument('--path', type=str)
    return parser.parse_args()


def inject(path: str) -> None:
    print(path)


if __name__ == '__main__':
    inject(parse_args().path)
