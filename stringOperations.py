# # # # # # i = "My name is yahya."
# # # # # # #indexing
# # # # # # print(i[0])

# # # # # # #slicing
# # # # # # i = "My name is yahya."
# # # # # # print(i[0:7])
# # # # # # print(i[::8])
# # # # # # print(i[0:10:3]) #start:stop:step

# # # # # #concadination
# # # # # # name = "yahya"
# # # # # # gender = "male"
# # # # # # print(name + " " + gender)
# # # # # # print((name + " " + gender + " ") * 10) #multipliyer

# # # # # #sting meyhods
# # # # # # i = "my name is yahya"
# # # # # # print(i.upper())
# # # # # # print(i.lower())
# # # # # # print(i.title())
# # # # # # print(i.capitalize())
# # # # # # print(i.swapcase())

# # # # # #searching and checking
# # # # # i = "my name is yahya"
# # # # # print(i.find("yahya"))
# # # # # print(i.count("yahya"))
# # # # # print(i.startswith("yahya"))
# # # # # print(i.endswith("yahya"))

# # # # # #replace
# # # # # i = "my name is yahya"
# # # # # print(i.replace("yahya" , "sam"))
# # # # # print(len(i))

# # # # j = "  Hello world  "
# # # # print(j.strip())
# # # # print(j.lstrip())
# # # # print(j.rstrip())

# # # #spliting and joining
# # # sent = "my5name is yahya"
# # # word = sent.split()
# # # print(word)

# # # joined = "4".join(word)
# # # print(joined)

# # # print(sent.split("5"))

# # # #type checking
# # x = "235"
# # y = "yahya"

# # print(x.isdigit())
# # print(y.isalpha())
# # print("python67".isalnum())
# # print(" ".isspace())

#palindrome checker
# x = input("Enter any word check its palindrome:  ")
# y = x[::-1]

# print(y)

# if (y == x):
#     print("the word is palindrome")

# else :
#     print("its not a palindrome word")

#initial checker

x = input("Enter any fucking sentance or word: ")
y = x.split()
z = ""

for m in y :

    z += m[0].upper() + "."

print(z)
