from .solver import Solver
import os, sys, argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
        help='The file in which a string format of a Soduku problem is contained')
    details = parser.add_mutually_exclusive_group()
    details.add_argument('-t', '--time', action='store_true', help='Print cost time')
    # parser.add_argument('-v', '--verbose', action='store_true', help='Give some detail infomation')
    args = parser.parse_args()
    if args.file:
        with open(os.path.join(os.getcwd(), args.file), 'r') as f:
            problem = f.read()
    else:
        print('Please type the problem in:')
        problem = sys.stdin.read()

    process = Solver.solve(Solver.load(problem))
    process.draw()
    if args.time:
        print('Cost: {}s'.format(process['cost']))
        
    return 0

if __name__ == '__main__':
    main()