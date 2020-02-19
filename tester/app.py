import sys
import argparse as argp

from tester.runner import run_test
from tester.config import (
    TEST_TYPES,
    TEST_LEVELS
)


def main(args):

    test_type = args.type if args.type else TEST_TYPES[0]
    test_level = args.level if args.level else TEST_LEVELS[0]
    run_test(test_type, test_level)


if __name__ == '__main__':

    parser = argp.ArgumentParser(description="Testing client.")
    parser.add_argument('-t', '--type', type=str, help='testing type.')
    parser.add_argument('-l', '--level', type=str, help='testing level.')

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()

    main(parser.parse_args())