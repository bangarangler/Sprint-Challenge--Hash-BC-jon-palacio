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
    if len(weights) < 2:
        print("weights less than 2")
        return None

    elif len(weights) == 2:
        if weights[0] + weights[1] == limit:
            return [1, 0]

    else:
        for item in range(len(weights)):
            if ht.storage is not None:
                hash_table_insert(ht, weights[item], item)

        for i in range(1, limit + 1):
            minimum = i
            maximum = limit - i
            print(f"min: {minimum} : max: {maximum}")
            minTest = hash_table_retrieve(ht, minimum)
            print(f"HashTable Minimum: {minTest}")
            if minTest is not None:
                test = hash_table_remove(ht, minimum)
                # print(test, "testing")
                maxTest = hash_table_retrieve(ht, maximum)
                print(f"HashTable Maximum : {maxTest}")
                if maxTest is not None:
                    return [maxTest, minTest]

    # print(ht.storage)
weights_3 = [4, 6, 10, 15, 16]
weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


# print(get_indices_of_item_weights([1], 1, 1))
# print(get_indices_of_item_weights(weights_3, 5, 21))
print(get_indices_of_item_weights(weights_4, 9, 7))


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
