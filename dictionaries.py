students=[{"name":"Dennis","admNo":1422,"course":"Python"},{"name":"Jay","admNo":1523,"course":"IT"},{"name":"Vicky","admNo":1489,"course":"Astronomy"}]
name=""
for student in students:

    if student["admNo"] > 1500:
        name=student["name"]
print(name," please register next year.")
