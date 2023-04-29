def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    ed = [[0 for x in range(n+1)] for x in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                ed[i][j] = j
            elif j == 0:
                ed[i][j] = i
            elif str1[i-1] == str2[j-1]:
                ed[i][j] = ed[i-1][j-1]
            else:
                ed[i][j] = 1 + min(ed[i][j-1], ed[i-1][j], ed[i-1][j-1])
                
    # Backtracking to find the operations
    i, j = m, n
    operations = []
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            operations.append(("No operation", str1[i-1]))
            i -= 1
            j -= 1
        elif ed[i][j] == ed[i-1][j-1] + 1:
            operations.append(("Substitute", str2[j-1]))
            i -= 1
            j -= 1
        elif ed[i][j] == ed[i-1][j] + 1:
            operations.append(("Delete", str1[i-1]))
            i -= 1
        elif ed[i][j] == ed[i][j-1] + 1:
            operations.append(("Insert", str2[j-1]))
            j -= 1
    
    while i > 0:
        operations.append(("Delete", str1[i-1]))
        i -= 1
        
    while j > 0:
        operations.append(("Insert", str2[j-1]))
        j -= 1
    # to show operations in the right order    
    operations.reverse()
    return ed[m][n], operations

# Test the function
str1 = input('enter first string :')
str2 = input('enter second string :')
distance, operations = edit_distance(str1, str2)
print("Edit distance between", str1, "and", str2, "is", distance)
print("Operations:")
for operation in operations:
    print(operation[0], operation[1])


