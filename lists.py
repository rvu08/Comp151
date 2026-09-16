courses_to_take = ["comp151", "comp143", "math130", "math120", "math151"]
print(f"starting list of classes: {courses_to_take}")
courses_to_take.insert(2, "comp152")
print(courses_to_take)
courses_to_take[-4] = "cyber210"
print(courses_to_take)
my_course = input("what upper level course will you take?")
#courses_to_take.insert(6, my_course)
courses_to_take.append(my_course)
print(courses_to_take)
courses_to_take.remove("comp151")
print(courses_to_take)
courses_to_take.pop(4)
print(courses_to_take)