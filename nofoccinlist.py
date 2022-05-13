def countnum(lst,x):
    count =0
    for ele in lst:
      if ele==x:
         count+=1
    return count

lst=[8,9,4,7,6,10,8,5,8]
x=8
print("{0} has occured {1} times".format(x,countnum(lst,x)))
