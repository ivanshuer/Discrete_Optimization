import numpy as np

def knapsack_dm_status(items, item_count, capacity):

    status = np.zeros((capacity + 1, item_count + 1))

    for j in range(1, item_count + 1):
        for k in range(capacity + 1):
            if items[j - 1].weight <= k:
                status[k, j] = max(status[k, j - 1], status[k - items[j - 1].weight, j - 1] + items[j - 1].value)
            else:
                status[k, j] = status[k, j - 1]

    return status

def find_optimal_solution_sequence_dm(status, taken, items, item_count, capacity):

    j = item_count
    k = capacity

    while(k > 0 and j > 0):
        if not status[k, j] == status[k, j - 1]:
            taken[j - 1] = 1
            k = k - items[j - 1].weight
        j = j - 1

    return taken