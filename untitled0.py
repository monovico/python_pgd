grocerylist = []

print("what do you need")

item = input().lower()

while (item != "nothing"):
    grocerylist.append(item)
    item = input("what else do you need?").lower()
    
print ("you need to buy")
for item in grocerylist:
    print (item)
    
while (grocerylist != []):
    grocerylist.remove(item)
    item = input("what have you bought?").lower()
    
print("you've got everything you you need")