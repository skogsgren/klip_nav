from tui import App
from utils import SortedClippings
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="klip-nav", description="TUI for kindle clippings"
    )
    parser.add_argument("clippings_file")
    args = parser.parse_args()
    runit = App(
        clippings=SortedClippings(args.clippings_file),
        filename=args.clippings_file,
    )
