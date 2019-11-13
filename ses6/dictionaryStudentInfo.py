my_dict={}
grades={'Ana':'B','John':'A+','Denise':'A','Katy':'A'}

# print(grades)
# # print(grades["John"])
# # print(grades['Sylvan'])
# grades['Sylvan']='A'
# print(grades)
# print('John' in grades)
# print('Daniel' in grades)
# del(grades['Ana'])
# print(grades)
print(grades.keys())
print(grades.values())
print(grades.items())
for name in grades.keys():
    print(name)
print()
for grade in grades.values():
    print(grade)
print()
for item in grades.items():
    print(item)
print()
for name,grade in grades.items():
    print(name,grade)
