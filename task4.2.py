# value_list = [3,2,9,11,7]

# def my_fuction(arr):
#     my_dic = {}
#     for i in range(len(arr)):
#         key = arr[i]%len(arr)
#         my_dic[key] = arr[i]
#     return my_dic

# def hash_key(v,m):
#     h = v % ms
#     return h

# choice = int(input('Choice number 1: Construct the whole hash table \n Choice number 2: Add a new element to the hash table \n Choice number 3: Update a value of a certain key \n Choice number 4: Delete an element from the hash table \n Choice number 5: Search for an element in the hash table \n Choice number 6: print All elements with their keys of the hash table  \n enter your choice :'))
# if choice == 1:
#     print(my_fuction(value_list))

# elif choice == 2:
#     value = int(input(' enter your new value :'))
#     value_list.append(value)
#     print(value_list)

# elif choice == 3 :
#     pass

# elif choice == 4 :
#     value_list.pop()
#     print(value_list)

# elif choice == 5 :
#     value = input('enter your value :')
#     value_list.search(value)    

# elif choice == 6:
#     print(my_fuction(value_list))
value_list = [3, 2, 9, 11, 7]

def my_fucntion(arr):
    my_dic = {}
    for i in range(len(arr)):
        key = arr[i]%len(arr)
        my_dic[key] = arr[i]
    return my_dic

# returns hash key    
def hash_function(v, m):
    return v % m

# add new element
def insert(hash_table, key, value):
    index = hash_function(key, len(hash_table))
    hash_table[index] = value
    return hash_table

# search for an  element
def search(hash_table, key):
    index = hash_function(key, len(hash_table))
    return hash_table[index]

# update a value of certain key 
def update(hash_table, key, value):
    index = hash_function(key, len(hash_table))
    hash_table[index] = value
    return hash_table

# delete an element
def delete(hash_table, key):
    index = hash_function(key, len(hash_table))
    hash_table[index] = None
    return hash_table

# print all elements
# def print_all(hash_table):
#     for i in range(len(hash_table)):
#         if hash_table[i] is not None:
#             print(f"Key: {i}, Value: {hash_table[i]}")


hash_table = my_fucntion(value_list)
print("Choice number 1: Construct the whole hash table using  \n Choice number 2: Add a new element to the hash table \n Choice number 3: Update a value of a certain key \n Choice number 4: Delete an element from the hash table \n Choice number 5: Search for an element in the hash table \n Choice number 6: print All elements with their keys of the hash table :")
 
choice = int(input(' enter your choice :'))

if choice == 1:
    print(my_fucntion(value_list))

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
    # print_all(hash_table)
    print(my_fucntion(value_list))
