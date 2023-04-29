value_list = [3, 2, 9, 11, 7]

def my_function(arr):
    size = len(arr)
    hash_table = [None] * size
    for val in arr:
        key = hash_function(val, size)
        while hash_table[key] is not None:
            key = (key + 1) % size
        hash_table[key] = val
    return hash_table

def hash_function(v, m):
    return v % m

def insert(hash_table, key, value):
    size = len(hash_table)
    i = hash_function(key, size)
    while hash_table[i] is not None:
        i = (i + 1) % size
    hash_table[i] = value
    return hash_table

def search(hash_table, key):
    size = len(hash_table)
    i = hash_function(key, size)
    while hash_table[i] is not None:
        if hash_table[i] == key:
            return hash_table[i]
        i = (i + 1) % size
    return None

def update(hash_table, key, value):
    size = len(hash_table)
    i = hash_function(key, size)
    while hash_table[i] is not None:
        if hash_table[i] == key:
            hash_table[i] = value
            return hash_table
        i = (i + 1) % size
    return None

def delete(hash_table, key):
    size = len(hash_table)
    i = hash_function(key, size)
    while hash_table[i] is not None:
        if hash_table[i] == key:
            hash_table[i] = None
            return hash_table
        i = (i + 1) % size
    return None

hash_table = my_function(value_list)
print("Choice number 1: Construct the whole hash table using \nChoice number 2: Add a new element to the hash table \nChoice number 3: Update a value of a certain key \nChoice number 4: Delete an element from the hash table \nChoice number 5: Search for an element in the hash table \nChoice number 6: Print all elements with their keys of the hash table:")

choice = int(input('Enter your choice: '))

if choice == 1:
    print(hash_table)

elif choice == 2:
    key = int(input("Enter a key: "))
    value = int(input("Enter a value: "))
    print(insert(hash_table, key, value))

elif choice == 3:
    key = int(input("Enter a key: "))
    value = int(input("Enter a new value: "))
    print(update(hash_table, key, value))

elif choice == 4:
    key = int(input("Enter a key: "))
    print(delete(hash_table, key))

elif choice == 5:
    key = int(input("Enter a key: "))
    result = search(hash_table, key)
    if result is not None:
        print(result)
    else:
        print("Key not found")

elif choice == 6:
    for i, val in enumerate(hash_table):
        if val is not None:
            print(f"Key: {i}, Value: {val}")