students=[{"name":"Dennis","age":23,"Course":"Python"},{"name":"Mufasa","age":22,"Course":"IT"},{"name":"Vicky","age":21,"Course":"IT"}]
old=0
name=""
for student in students:
    # print(student["name"],"is taking ",student["Course"])

    if student["age"]>old:
        old=student["age"]
        name=student["name"]

print(name," is the eldest and is",old," years old.")

