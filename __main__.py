from typing import Dict, List

import argparse
import datetime
import sys

import constraint

def main(argv: List[str]):
    parser = argparse.ArgumentParser()

    parser.add_argument("--min", type=int, default=0)
    parser.add_argument("--max", type=int, default=1000)

    args = parser.parse_args(argv)

    problem = create_problem(args.min, args.max)

    time_before = datetime.datetime.now()
    solutions = calculate_all_solutions(problem)
    time_after = datetime.datetime.now()

    runtime = time_after - time_before

    print("Runtime:", runtime)

    print("Solutions found:", solutions)

def create_problem(min_value: int, max_value: int) -> constraint.Problem:
    problem = constraint.Problem()
    problem.addVariable("a", range(min_value, max_value))
    problem.addVariable("b", range(min_value, max_value))

    problem.addConstraint(lambda a, b: a == b * 10, ("a", "b"))

    return problem

def calculate_all_solutions(problem: constraint.Problem) -> List[Dict[str, int]]:
    return problem.getSolutions()

if __name__ == "__main__":
    main(sys.argv[1:])