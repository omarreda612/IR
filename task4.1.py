# def hash(value, size):
#     sum = 0
#     for i in range(len(value)):
#         sum = sum + ord(value[i])

#     return sum%size
# print(hash('ali', 1))
# another solution

# def my_fuction(arr):
#     list = my_dic = {}
#     for i in range(len(arr)):
#         key = arr[i]%len(arr)
#         my_dic[key] = arr[i]
#     return list

# print(my_fuction([1,2,3]))    

def hash_function(v, m):
    return v % m

print(hash_function(2,7))

# def list_to_dict(lst, size):
#     d = {}
#     for value in lst:
#         key = value % size
#         d[key] = value
#     return d

# lst = [3, 2, 9, 11, 7]
# size = 5
# d = list_to_dict(lst,size)
# print(d)