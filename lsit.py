lucky_numbers=[4,6,7]

friends=["naaz" , "nazrin" ,"karen"]
friends.extend(lucky_numbers)
print(friends)
friends.insert(1,"annu")
friends.insert(2,"yasmin")
friends[1]="omair"
print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])#1 and after all

print(friends[1:3])# 1 and 2 
print(friends.index("nazrin"))#index of nazrin
print(friends.count("naaz")) #show how many naaz 
luck_numbers.sort()#sort asc order
friends2=friends.copy()
print(friends2)
