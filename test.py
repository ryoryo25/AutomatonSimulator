import time
from alphabet import Alphabet

p = "p"
q = "q"
r = "r"
state_to_index = {p: 0, q: 1, r: 2}

def simulate(string_input):
    sigma = {'0': 0, '1': 1}
    Q = [p, q, r]
    trans = [[p, q],
             [p, r],
             [p, r]]
    p0 = p
    F = [r]

    current_state = p0
    for char in string_input:
        print(current_state)
        next_state = trans[state_to_index[current_state]][sigma[char]]
        current_state = next_state
        time.sleep(0.5)

    if current_state in F:
        print(current_state, ": ACCEPTED!!")
    else:
        print(current_state, ": REJECTED!!")

simulate(input("> "))