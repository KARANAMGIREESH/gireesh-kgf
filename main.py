def RemoveIthWord(lst, word, N):
    newList = []
    count = 0

    for i in lst:
        if (i == word):
            count = count + 1
            if (count != N):
                newList.append(i)
        else:
            newList.append(i)

    lst = newList
    if count == 0:
        print("Item not found")
    else:
        print("Updated list is: ", lst)
    return newList

# Driver code
list = ["geeks", "for", "geeks"]
word = "geeks"
N = 2

RemoveIthWord(list, word, N)
