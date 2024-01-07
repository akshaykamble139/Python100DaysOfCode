# FileNotFound
# try:
#     file = open("a_file.txt")
#     dict = {"key" : "value"}
#     g = dict["key"]
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError

#KeyError
# dict = {"key" : "value"}
# g = dict["new_key"]

# IndexError
# list = [8,9,0]
# h = list[3]

# TypeError
# text = "abs"
# print(text + 5)

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 metres")
bmi = weight / (height ** 2)
print(bmi)