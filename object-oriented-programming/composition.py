class Employee:
    obj_type = "Employee"

    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Employee Name: {self.name} and Employee ID: {self.emp_id}")


class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def display_info(self):
        print(f"Department Name: {self.name}")
        print("Employees:")
        for employee in self.employees:
            employee.display_info()


# Example 2 Author and Books

class Author:
    def __init__(self, name):
        self.name = name

    def write(self):
        print(f"{self.name} is writing.")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author.name}")


# Example3

class Room:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print(f"This is the {self.name} room.")


class House:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def describe(self):
        print("House description:")
        for room in self.rooms:
            room.describe()


if __name__ == "__main__":

    # ##Example 1
    print("\n")
    print('***** Example 1: The Department class  is composed of multiple Employee class *****')
    # (or a Department object has an Employee object)
    employee1 = Employee("John Doe", 1)
    employee2 = Employee("Jane Smith", 2)
    department = Department("Engineering", [employee1, employee2])
    department.display_info()

    # ### Example 2: Book class is composed of an Author class (or a Book has an Author relationship)

    print("\n")
    print('***** Example 2: Book class is composed of an Author class *****')
    author = Author("John Doe")
    book = Book("Python Programming", author)
    book.display_info()
    book.author.write()

    # ##A House is composed of multiple Room
    print("\n")
    print('***** Example 3: House is composed of multiple Room *****')
    living_room = Room("Living Room")
    kitchen = Room("Kitchen")
    bedroom = Room("Bedroom")

    my_house = House()
    my_house.add_room(living_room)
    my_house.add_room(kitchen)
    my_house.add_room(bedroom)

    my_house.describe()
