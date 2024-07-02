# #1---------list() metotları
# list_methods = []
# for method in dir(list):
#     if method.startswith("__"): # __ ile baslayan mothodları almadık
#         continue
#     list_methods.append(method)
#
# #2------kume() metotları
# set_methods = []
# for method in dir(set):
#     if method.startswith("__"):
#         continue
#     set_methods.append(method)
#
# #3------string() metotları
# string_methods = []
# for method in dir(str):
#     if method.startswith("__"):
#         continue
#     string_methods.append(method)
#
#
# #4------tuple() metotları
# tuple_methods = []
# for method in dir(tuple):
#     if method.startswith("__"):
#         continue
#     tuple_methods.append(method)
#
# #5------sozluk() metotları
# dict_methods = []
# for method in dir(dict):
#     if method.startswith("__"):
#         continue
#     dict_methods.append(method)

#Metodları yukarıdaki gibi de alabilirdik fakat asagıdaki yazım daha kısadır
list_methods = [method for method in dir(list) if not method.startswith("__")]
set_methods = [method for method in dir(set) if not method.startswith("__")]
string_methods = [method for method in dir(str) if not method.startswith("__")]
tuple_methods = [method for method in dir(tuple) if not method.startswith("__")]
dict_methods = [method for method in dir(dict) if not method.startswith("__")]

names = ["List Methods", "Set Methods", "String Methods", "Tuple Methods", "Dict Methods"]
headers = [list_methods, set_methods, string_methods, tuple_methods, dict_methods]

max_len = max(len(class_) for class_ in headers)
column_width = 30

with open("Methods.txt", "w") as f:
    for header in names:
        print(header.ljust(column_width), end="")
        f.write(header.ljust(column_width))
    print()
    f.write("\n")

    for i in range(max_len):
        for class_ in headers:
            if i < len(class_):
                method = class_[i]
            else:
                method = "-------"
            print(method.ljust(column_width), end="")
            f.write(method.ljust(column_width))
        print()
        f.write("\n")
