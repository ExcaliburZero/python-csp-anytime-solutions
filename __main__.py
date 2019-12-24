from typing import Dict, List

import argparse
import datetime
import multiprocessing
import queue
import sys

import constraint

Solution = Dict[str, int]


def main(argv: List[str]):
    parser = argparse.ArgumentParser()

    parser.add_argument("method", type=str)
    parser.add_argument("--min", type=int, default=0)
    parser.add_argument("--max", type=int, default=3000)

    args = parser.parse_args(argv)

    problem = create_problem(args.min, args.max)

    time_before = datetime.datetime.now()
    if args.method == "all_solutions":
        solutions = calculate_all_solutions(problem)
    elif args.method == "until_ctrl_c":
        solutions = calculate_solutions_until_sigint(problem)
    else:
        assert False
    time_after = datetime.datetime.now()

    runtime = time_after - time_before

    print("Runtime:", runtime)

    print("Solutions found ({}): {}".format(len(solutions), solutions))


def create_problem(min_value: int, max_value: int) -> constraint.Problem:
    """
    Creates a simple problem that, with a large enough input domain, should run for a while and waste
    some CPU cycles.
    """
    problem = constraint.Problem()
    problem.addVariable("a", range(min_value, max_value))
    problem.addVariable("b", range(min_value, max_value))

    problem.addConstraint(lambda a, b: a == b * 10, ("a", "b"))

    return problem


def calculate_all_solutions(problem: constraint.Problem) -> List[Solution]:
    """
    Solves for all of the solutions to the given problem in one go.
    """
    return problem.getSolutions()


def calculate_solutions_until_sigint(problem: constraint.Problem) -> List[Solution]:
    """
    Calculates solutions to the CSP until the user gives a keyboard interrupt (Ctrl + c) or all
    solutions have been calculated and reports back the solutions that were calculated.

    This is implemented by creating a separate process to calculate the solutions, recording the
    found solutions in a muliprocessing queue, and stopping the process early if a keyboard
    interrupt is recieved.

    A multiprocess lock is also used to prevent some possible race conditions that could occur if
    we terminate the process while a soltuion is in the middle of being added to the queue.
    """
    queue_lock = multiprocessing.Lock()
    solution_queue: multiprocessing.Queue[Solution] = multiprocessing.Queue()

    process = multiprocessing.Process(
        target=calculate_solutions_and_store, args=(problem, solution_queue, queue_lock)
    )

    process.start()
    try:
        process.join()
    except KeyboardInterrupt:
        try:
            queue_lock.acquire()
            process.terminate()
        finally:
            queue_lock.release()

    return multiprocess_queue_to_list(solution_queue)


def calculate_solutions_and_store(
    problem: constraint.Problem,
    solution_queue: "multiprocessing.Queue[Solution]",
    queue_lock: "multiprocessing.synchronize.Lock",
) -> None:
    """
    Uses the getSolutionIter interface to find solutions to the given problem one by one and add
    them to the given multiprocess queue.
    """
    solution_iter = problem.getSolutionIter()
    while True:
        try:
            new_solution = next(solution_iter)
            try:
                queue_lock.acquire()
                solution_queue.put(new_solution)
            finally:
                queue_lock.release()
        except StopIteration:
            break


def multiprocess_queue_to_list(multiprocess_queue: multiprocessing.Queue) -> List:
    """
    Reads all of the items from the given multiprocess queue and returns them as a list.

    Assumes that no new items will be added to the queue after this method starts.
    """
    items = []
    while True:
        try:
            items.append(multiprocess_queue.get(block=False))
        except queue.Empty:
            break

    return items


if __name__ == "__main__":
    main(sys.argv[1:])
