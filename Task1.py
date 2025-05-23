try:
    dictionary= {'Alice': 85}
    name=input("Enter the student's name: ")
    Name= name.capitalize()
    print(Name,"'s marks",dictionary[Name])
except KeyError:
    print("Student not found")

