# Simple Hospital Management System

## Overview
This hospital management system is a Python program designed to help manage patient and doctor rosters, manage visits and inventory in a hospital environment. It includes features for planning visits, managing information about patients and doctors, and managing the inventory of medical tools and equipment. You should be able to run this program on any code editing sotfware like Visual Studio Code, PyCharm. Well, this course work has been done using PyCharm because it offered the easiest way of operating with files, as well as PyCharm recognised Git, so they easily got paired. As a result, I could commit my changes via PyCharm, not even having to open Git Bash.

Using this program is quite easy - as it was the point of my work. Unfortunately, I've had issues with this work even though I was trying to do stuff in the easiest way possible. Perhaps that is why, as a user, you have to be careful while operating with data file "pyData.txt". Sometimes, this file may lead to misbehavior in the results, as will be shown in a screenshot a little bit later. But other than that, everything else is relatively easy to comprehend. All you have to do is call necessary methods, functions with correspinding data. Without further ado, let's dive into it.

## Features
- **Appointment Scheduling:** Schedule appointments between patients and doctors.
- **Patient and Doctor Management:** Add, view, and manage patient and doctor information.
- **Inventory Management:** Add, view, update, and search items in the hospital's inventory.

## Object-Oriented Programming (OOP) Pillars
1. **Encapsulation**
2. **Inheritance**
3. **Abstraction**
4. **Polymorphism**

## Design patterns
1. **„Factory method“**
2. **„Observer pattern“**

## Why these patterns?
- **„Factory method“:** When you need to create/add a person, that is, a patient, a doctor, it is very easy to do this using the Factory method. I liked this method and it is wonderful, because when creating a person, it is not necessary to create an object for the corresponding class and assign all the information - everything is much simpler. Based on the type of person (patient or doctor), Factory creates a person with the information assigned to it.
- **„Observer pattern“:** A model that, most likely, was not shown during the lectures, but it was perfect for implementing my idea - to announce some changes. It could be the registration of a new visit, it could be the "arrival" of new tools, it could be the search for an object in the inventory or updating the contents of the storage.

## Where can OOP be seen in the code?
##### **Encapsulation:**
```
    def __init__(self):
        super().__init__()
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patients(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
```
In this case, none of the lists are being hidden, however, they still represent encapsulation. Presume, I for some reason don't want anyone to see what's inside these lists. All I have do to here is just make these lists private:
```
    def __init__(self):
        super().__init__()
        self.__patients = []
        self.__doctors = []
        self.__appointments = []
    # Since we made the lists private, we need to change something else

    def add_patients(self, patient):
        self.__patients.append(patient)

    def add_doctor(self, doctor):
        self.__doctors.append(doctor)
```
Here's another example of Public Encapsulation:
```
    def __init__(self, item_name, item_quantity, item_category, item_description=None):
        super().__init__()
        self.item_name = item_name
        self.item_quantity = item_quantity
        self.item_category = item_category
        self.item_description = item_description

    def display_info(self):
        print("Item name: ", self.item_name)
        print("Item quantity: ", self.item_quantity)
        print("Item category: ", self.item_category)
        if self.item_description:
            print("Item description: ", self.item_description)
```
And, finally:
```
    def __init__(self):
        super().__init__()
        self.items = []
    # the rest of the code
```
As you can see, I am not a huge fan of hiding stuff that ideally should be hidden. Even though I am not utilizing fully Encapsulation, I do admit that it is a good practice to make something in my code private.
##### **Inheritance:**
Inheritance was used quite often, whether I had to create a person, or to simply implement the Observer. Here's what we got:
```
class ItemSearch(Observable):
    def i_update(self, data):
        print("Item search successful:\n")
        print(data)


class ItemUpdate(Observable):
    def i_update(self, data):
        print("Updated inventory stocks:\n")
        print(data)


class ItemReceiver(Observable):
    def i_update(self, data):
        print("Shipment arrived and has been received:\n")
        print(data)
```
Here you can see 3 classes that inherit from the "Observable" class - which is actually a design pattern. Note: not sure why I named it Observable, not just Observer, but oh well, stuff happens. Each class will serve a different purpose, but the goal is simple - to notify about the successful command or a change in the results.

```
class Person:
    def __init__(self, name, age, phone, gender):
        self.name = name
        self.age = age
        self.phone = phone
        self.gender = gender

    def display_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Phone number: ", self.phone)
        print("Gender: ", self.gender)


class Patient(Person):
    def __init__(self, name, age, phone, gender, address):
        super().__init__(name, age, phone, gender)
        self.address = address

    def display_info(self):
        super().display_info()
        print("Address: ", self.address)


class Doctor(Person):
    def __init__(self, name, age, phone, gender, specialization, hourly_rate, hours_worked):
        super().__init__(name, age, phone, gender)
        self.specialization = specialization
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

    def display_info(self):
        super().display_info()
        print("This doctor is specialised ", self.specialization)
        print(f"Hourly rate for {self.specialization} is {self.hourly_rate}.")
        print(f"Dr. {self.name} is usually working {self.hours_worked} hours daily.")
        print(f"Dr. {self.name}'s salary: {self.calculate_salary()}.")

```
Here you can see another instance of Inheritance. This time we have a class that has its own attributes that are being inherited by two other classes. In this case, `class Person` has a set of standard data like name, age, phone and gender. Later on, `class Patient` and `class Doctor` inherit all of the attributes, but also are being given their own attributes like `address` for patients and `specialization`,`hourly_rate` and `hours_worked` for doctors.

##### **Abstraction:**

##### **Polymorphism:**
