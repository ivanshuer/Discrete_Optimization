#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
import knapsack_lib as klib
Item = namedtuple("Item", ['index', 'value', 'weight'])
import pdb

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    #for item in items:
    #    if weight + item.weight <= capacity:
    #        taken[item.index] = 1
    #        value += item.value
    #        weight += item.weight
    
    # prepare the solution in the specified output format
    pdb.set_trace()
    #value = klib.knapsack_dm_status(items, item_count, capacity)

    #total_value = 0
    #for i in range(len(items)):
    #    total_value = total_value + items[i].value

    #items = sorted(items, key=lambda x: x.ratio, reverse=True)

    #klib.branch_greedy(0, total_value, capacity, value, items, item_count, taken)
    status = klib.knapsack_dm_status(items, item_count, capacity)
    value = int(status[capacity, item_count])
    taken = klib.find_optimal_solution_sequence_dm(status, taken, items, item_count, capacity)

    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
    #if len(sys.argv) > 0:
        file_location = sys.argv[1].strip()
        #file_location = './data/ks_4_0'
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

