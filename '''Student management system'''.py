'''Student management system'''

 

class Student:

    '''' Student objects have attributes like name, phone, address, and a list of the classes

    they are enrolled in. There are also getter functions for each, as well as functions to display

    all of their information'''

 

    def __init__(self, name, age, phone, classes):

        '''The init function is called automatically when the object is created'''

 

        #Assign name to the new student

 

        self._name = name

        self._phone = phone

        self._age = age

        self._classes = classes

        self._enrolled = True

        students.append(self)

        


    def get_name(self):

        '''Return of the name of the student'''

        return self._name

   

    def get_phone(self):

        '''Return of the name of the student'''

        return self._phone

   

    def get_age(self):

        '''Return of the name of the student'''

        return self._age

   

    def get_classes(self):

        '''Return of the name of the student'''

        return self._classes

 

        #Add the new student to the students list

    def get_enrolled(self):

        return self._enrolled

    def unenrol(self):
        
        self._enrolled = False

    def display_my_info(self):

        print("=" * 30)
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Phone: {self._phone}")
        print(f"Classes: ", end=" ")
        for c in self._classes:
            print(c, end=" ")

        print()
        print("=" * 30)

 

#list of all students

 

students = []

 

#Create students

Student("Tom Kerry", 17, "02041764093", ["DIGI, MATH"])

Student("Leanne Mcphail", 17, "0275295280", ["DIGI, BIOL"])

def search():
    ''' User searches for student '''

    name_search = input("Enter name to search for: ")

    for s in students:
        if name_search.lower()+" " in  s.get_name().lower() or " "+name_search.lower() in s.get_name().lower():
            s.display_my_info()

def display_all():
    ''' Display names of all students '''

    for s in students:
        s.display_my_info()

 
def add_student():
    print("Enter new student details")
    print("-"*20)
    name = input("Name: ")
    enter_age = True
    while enter_age:
        try: 
            age = int(input("Age: "))
            enter_age = False
        except ValueError: 
            print("Enter an Integer")
    phone = input("Phone: ")
    student_classes = []
    enter_class = True 
    while enter_class:
        new_class = input("Class code(end to stop): ")
        if new_class == "end":
            enter_class = False
        else: 
            student_classes.append(new_class)

    Student(name, age, phone, student_classes)






display_all ()

 