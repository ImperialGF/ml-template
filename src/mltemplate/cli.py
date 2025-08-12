import argparse
import json

from .core import summarize_csv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Путь к CSV-файлу")
    args = parser.parse_args()
    print(json.dumps(summarize_csv(args.path), ensure_ascii=False))


if __name__ == "__main__":
    main()
