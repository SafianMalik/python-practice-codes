mylist_one=[]
mylist_two=["ali","noor","zoya"]
firt_name=input("Please enter your first name: ")
second_name=input("Please enter your second name: ")
mylist_one.append(firt_name)
mylist_one.append(second_name)
print(mylist_one)
mylist_one.extend(mylist_two)
mylist_two.extend(mylist_one)
print(mylist_two)
mylist_one.extend(mylist_two)