# # # # #lists 
# # # # nums = [1,2,3,4,5]
# for x in nums:
#     print(x)
# # # # nums.append(24)
# # # # nums.extend([10,20,30])
# # # # nums.insert(1,90)
# # # # nums.remove(10)
# # # # l = nums.pop()
# # # # print(nums)
# # # # print(nums.count(5))
# # # # print(nums.index(90))
# # # # nums.sort
# # # # print(nums)
# # # # nums.sort(reverse=True)
# # # # print(nums)
# # # # nums.clear()
# # # # print(nums)

# # # #tuples
# # # nums = (10,)
# # # print(type(nums))
# # # immutable

# # #unpacking of tuples
# # num = (4,5,6,7)

# # a,b,c,d = num
# # print(num)
# # print(a)
# # print(b)
# # print(c)
# # print(d)

# #sets
# a = set()
# a = {3,3,7,4,"yahya"}
# a.add(9)
# # a.discard(3) #saveremove
# # a.remove(9) #breaks code if not found
# a.pop()
# print(a)
# print("yahya" in a)
# print("yahya" not in  a)

# b = ["yahya","sam","yahya","mohammad"]
# c = list(set(b))  #random order
# print(c)

#dictionary

users = {"u1":{"name":"yahya","gender":"male"},
         "u2":{"name":"yahya","gender":"male"},
         "u3":{"name":"yahya","gender":"male"}
         }

print(users)

for key, value in users.items():
    print(key ,value)

    for value in users.values():
        print(value["name"])

    for keys in users.keys():
        print(keys)    

for key , value in users.items():
    print(key ,value["name"], value["gender"])