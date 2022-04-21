import itertools
import time
from pprint import pprint

best_permutations = []
calculated_cost = 0
matrix = []

def lines_to_string(number_total_lines):
    """
    Convert the total number of lines to a string containing all the indexes starting by 1.\n
    @params\n \tnumber_total_lines: The total number of lines.
    """
    string = ""
    for i in range(number_total_lines):
        string += str(i+1) + " "
    return string


def lines_to_tuple(number_total_lines):
    """
    Convert the total number of lines to a tuple containing all the indexes starting by 1.\n
    @params\n \tnumber_total_lines: The total number of lines.
    """
    tuple = ()
    for i in range(number_total_lines):
        tuple += (i+1,)
    return tuple
   
def validate_cost(ref, calculated_cost):
    """
    Validate the cost of the permutations.\n
    @params\n \tcalculated_cost: The cost of the permutations.
    """
    if best_permutations == []:
        best_permutations.append(dict(reference=ref, cost=calculated_cost))
    elif calculated_cost == best_permutations[0]['cost'] and ref not in best_permutations:
        best_permutations.append(dict(reference=ref, cost=calculated_cost))
    elif calculated_cost < best_permutations[0]['cost']:
        best_permutations.clear()
        best_permutations.append(dict(reference=ref, cost=calculated_cost))


def main():

    init = time.time()

    number_total_lines = 0
    calculated_cost = 0
    with open('tsp_data\\tsp2_1248.txt', 'r') as file:
        for line in file:
            matrix.append(line.split())
            number_total_lines += 1

    permutations = itertools.permutations(
        lines_to_tuple(number_total_lines), number_total_lines)

    for permutation in permutations:
        for i in range(number_total_lines):
            if i == number_total_lines - 1:
                calculated_cost += int(matrix[0][len(matrix[0])-1])
            else:
                calculated_cost += int(matrix[int(permutation[i]) - 1][int(permutation[i+1]) - 1])

        validate_cost(permutation, calculated_cost)

    end = time.time()
    print("Execution time: %.2f seconds" % (end - init))
    pprint(f'Best Permutations with their cost:{best_permutations}', indent=4)

if __name__ == '__main__':
    main()
