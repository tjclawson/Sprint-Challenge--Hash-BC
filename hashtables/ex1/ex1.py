#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    w_index = 0
    for weight in weights:
        hash_table_insert(ht, weight, w_index)
        w_index += 1

    y_index = 0
    for weight in weights:
        target = limit - weight
        get_target = hash_table_retrieve(ht, target)
        if get_target:
            if weight > get_target:
                answer = (get_target, y_index)
                return answer
            else:
                answer = (y_index, get_target)
                return answer
        y_index += 1

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
