#create an empty list
my_list=[]
#append a list in the empty list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#insert value of 15 i9n the second position in the string
my_list.insert(1,15)
#extend my list with another list(50,60,70)
my_list.extend([50,60,70])
#deleting the last item on my list
del my_list[-1]
#s0rting my list in ascendcing order
my_list.sort()
print("sortred list in ascending order:",my_list)
#find and print the index of value of 30 in my list
index_of_30=my_list.index(30)
print("my updatedlist:",my_list)