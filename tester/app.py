import sys
import argparse as argp

from tester.utils.report import Reporter
from tester.utils.runner import run_test
from tester.config import (
    TEST_GROUPS,
    TEST_LEVELS
)


def main(args):

    group = args.group if args.group else TEST_GROUPS[0]
    if group not in TEST_GROUPS:
        Reporter.error('Undefined testing group')

    level = args.level if args.level else TEST_LEVELS[0]
    if level not in TEST_LEVELS:
        Reporter.error('Undefined testing level')

    run_test(group.lower(), level.lower())


if __name__ == '__main__':

    parser = argp.ArgumentParser(description="Testing client.")
    parser.add_argument('-g', '--group', type=str, help='testing group.')
    parser.add_argument('-l', '--level', type=str, help='testing level.')

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()

    main(parser.parse_args())
