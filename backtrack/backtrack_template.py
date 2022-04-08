def is_valid(state):
    # check it is valid contdition
    return True


def get_candidates(state):
    return []


def search(state, solutions):
    if is_valid(state):
        solutions.append(state.copy())
        return

    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)


def solve():
    solutions = []
    state = set()
    search(state, solutions)
    return solutions
