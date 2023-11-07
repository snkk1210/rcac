import os
import sys
import argparse

module_path = os.path.abspath("../src/rcac/app.py")
sys.path.append(os.path.dirname(module_path))

import app

parser = argparse.ArgumentParser(
    usage='Specify the type in -t as arguments. Check the help ( -h ) section for details.',
    description='Check the cost of your AWS account.'
    )
parser.add_argument('-t', '--type', required=True, help='Specify the type (1: Notify to Slack or 2: Notify to stdout)')
args = parser.parse_args()

if __name__ == '__main__':
    if args.type == "1":
        app.lambda_handler(" ", " ")
    elif args.type == "2":
        cost_amount = app.retrieve_cost_today()
        print("USD: %s" % (cost_amount))
    else:
        print('Invalid argument.')
        sys.exit(1)