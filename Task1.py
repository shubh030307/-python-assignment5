try:
    dictionary= {'Alice': 85}
    name=input("Enter the student's name(with first letter capital): ")
    print(name,"'s marks",dictionary[name])
except KeyError:
    print("Student not found")

