my_dict = {"name": "Alice","age": 25, "city": "New york"}
print(my_dict)
print(my_dict["name"])
print(my_dict.get("name"))

if "city" in my_dict:
	print(" City is the dictionary. ")
del my_dict["city"] # delete a key-value pair
print(my_dict)

print(my_dict.get("name"))
print(my_dict.get("salary", "not available"))

#to print the dictionary keys alone
for key in my_dict:
	print(key)

#to ptint the values
for value in my_dict.values():
	print(value)

#itrate through key-values pairs
for key, values in my_dict.items():
	print(f"{key}:{value}")



#dictionary comprehension 
squared = {x:x**2 for x in range(1,6)}
print(squared)

squared = {x:x**2 for x in range(1,10) if x %2 == 0 }
print(squared)


#zip function [if joiint 2 function]
# adding keys dynamically from list 


keys =["name","age","city"]
values = ["Alice",25,"new york"]
for key,values in zip(keys, values):
	my_dict[key]= value
print(my_dict)


def zipdata(keys , data):
	return {(keys,data) for keys,data in zip(keys, data)}
		
def zipdata2(keys , data):
	my_box = {}
	for keys,data in zip(keys, data):
		my_box[keys] = data



malik=[ "game", "house", "plane"]
price = [23, 45, 54]
print(zipdata(malik, price))
print(zipdata2(malik, price))


#Add and updating a dictionay  

my_dict = {"Name":"Alice", "age":25}
new_data={"City":"New York", "Age":26}

for key,value in new_data.items():
	my_dict[key] = value
print(my_dict)

#adding a single key-value pairs to a nested Dictonary 

nested_dict = {
"person1":{"name":"Alice","age":25},"person2":{"name":"Bob","age":30}
}
nested_dict["person1"]["city"] = "New York"

print(nested_dict)

#adding multiple pairs using update()

new_data = {"city":"los Angeles","profession":"engineer"}
nested_dict["person2"].update(new_data)

print(nested_dict)



input{"Alice":25,"bob":30,"charlie":35}
output:25{25:"alice",30:"bob"}



