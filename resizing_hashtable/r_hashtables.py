

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.og_capacity = capacity
        self.count = 0
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = ((hash << 5) + hash) + ord(x)
    return (hash % max) & 0xFFFFFFFF


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)

    if hash_table.storage[index] is None:
        hash_table.storage[index] = LinkedPair(key, value)

    else:
        new_pair = LinkedPair(key, value)
        new_pair.next = hash_table.storage[index]
        hash_table.storage[index] = new_pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)

    if hash_table.storage[index] is not None:
        curr = hash_table.storage[index]
        if curr.key == key:
            hash_table.storage[index] = curr.next
        else:
            while curr is not None:
                if curr.next.key == key:
                    curr.next = curr.next.next
                curr = curr.next
    else:
        print(f"no value for key \"{key}\"")


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)

    if hash_table.storage[index] is None:
        return None
    else:
        curr = hash_table.storage[index]
        if curr.key == key:
            return curr.value
        else:
            while curr is not None:
                if curr.next.key == key:
                    return curr.next.value
                curr = curr.next

            return None


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    double = [None] * hash_table.capacity

    hash_table.storage = [*hash_table.storage, *double]
    hash_table.capacity = 2 * hash_table.capacity
    return hash_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
