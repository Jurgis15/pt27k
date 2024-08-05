# print("hello world!")
# name = "Code Academy"
# print(name)
# print(name[5:12])


# greeting = "hello, my name is"
# name = "Tom"
# completed_greeting = f"{greeting} {name}"
# print(completed_greeting)

# if name != "":
#   print("Name was not entered")


# name = "Tom"

# if name == "":
#     print("Nice to see you ")
# else:
#     print("welcome, user")


# Leiskite naudotojui įvesti vardą, pavardę ir amžių. Išspausdinkite, ar naudotojas gali patekti į internetinį kazino, ar ne. 21 metai
# yra amžiaus riba.


name = input("Enter you name: ")
surname = input("Enter you surname: ")
age = int(input("enter your age"))



age_limit = 21
if age >= age_limit:
    print("user is alloved to play")
else:
    print("you are not alloved to play") 