my_dic = {}

def my_fuction(arr):
    list = my_dic
    for i in range(len(arr)):
        key = arr[i]%len(arr)
        my_dic[key] = arr[i]
    return list

print(my_fuction([1,2,3]))    

