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
#### **Encapsulation:**
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
As you can see, I am not a huge fan of hiding stuff that ideally should be hidden. Even though I am not fully utilizing Encapsulation, I do admit that it is a good practice to make something in my code private.
#### **Inheritance:**
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

#### **Abstraction:**

#### **Polymorphism:**
Polymorphism can be seen several times. The inheritance hierarchy between `Patient` and `Doctor` classes demonstrates polymorphism. Here's how:
```
class Person:
# the rest of the method (initialization)
    def display_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Phone number: ", self.phone)
        print("Gender: ", self.gender)
```
```
class Patient(Person):
# the rest of the method (initialization)
    def display_info(self):
        super().display_info()
        print("Address: ", self.address)
```
```
class Doctor(Person):
# the rest of the method (initialization)
    def display_info(self):
        super().display_info()
        print("This doctor is specialised ", self.specialization)
        print(f"Hourly rate for {self.specialization} is {self.hourly_rate}.")
        print(f"Dr. {self.name} is usually working {self.hours_worked} hours daily.")
        print(f"Dr. {self.name}'s salary: {self.calculate_salary()}.")
```
Both `Patient` and `Doctor` inherit the `display_info` method from the parent class `Person`. However, each class has its own implementation of `display_info` to show patient-specific or doctor-specific information.

When you call `display_info` on a `Patient` object or a `Doctor` object, the correct implementation is executed based on the object's actual type. This is polymorphism, because the same method name (`display_info`) exhibits different behavior depending on the object it's called on.

In addition, `display_info` method can also be seen in the class `Item` (another instance of polymorphism):
```
class Item:
# initialization
    def display_info(self):
        print("Item name: ", self.item_name)
        print("Item quantity: ", self.item_quantity)
        print("Item category: ", self.item_category)
        if self.item_description:
            print("Item description: ", self.item_description)
```

The `Observable` class and its subclasses demonstrate a different type of polymorphism. Here's why:
```
class Observable:
# the rest of the class (will be shown next paragraph)
    def notify_observers_items(self, data):
        for observer in self._observers:
            observer.i_update(data)

    def i_update(self, data):
        pass

# ....

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
- The `Observable` class defines an interface with methods like `notify_observers`.
- Different classes like `Hospital` and `Inventory` inherit from `Observable`.
- Even though they inherit the same method (`notify_observers`), each class might have its own data and logic for what information it sends to the observers.

When you call `notify_observers` on a `Hospital` object or an `Inventory` object, the specific implementation defined in that class is executed. This allows different subclasses to provide their own behavior for the inherited method, showcasing another form of polymorphism. So, the code demonstrates polymorphism through inheritance with overridden methods and through the use of an abstract base class (`Observable`) that allows subclasses to define specific notification behaviors.

## Examples of the design patterns used in this work
#### Observer pattern:
Observer is a behavioral design pattern that allows some objects to notify other objects about changes in their state. Let's take a look at the main class of the Observer pattern.
```
class Observable:  # design pattern
    def __init__(self):
        self._observers = []

    def add_an_observer(self, observer):
        self._observers.append(observer)

    def remove_an_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, data):
        for observer in self._observers:
            observer.update(data)

    def notify_observers_items(self, data):
        for observer in self._observers:
            observer.i_update(data)

    def i_update(self, data):
        pass
```
Subject `Observable` defines the interface for attaching and detaching observers, as well as it maintains a list of observers and notifies them of state changes. Methods `notify_observers` and `notify_observers_items` are responsible for notifying the program about executed queries in the code. For example:

![image](https://github.com/EidvydasJ/managment-system-hospital/assets/167422894/5e75e1d7-896e-4409-964c-78bdbd4a5bb6)

Here, messages like `New appointment scheduled` and `Appointment has been scheduled successfully` are printed, which suggest that changes were successful. It was `notify_observers` responsibility. On the other hand, `notify_observers_items` is responsible for notifying about item search, update, add:

![image](https://github.com/EidvydasJ/managment-system-hospital/assets/167422894/1cb34131-5f43-4831-bd16-4097552304e6)

Here you can see that query of adding an item was successfully completed.

Let's dive into how it was implemented:
```
class AppointmentNotifier:
    def update(self, data):
        print("New appointment scheduled:\n")
        print(data)


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
Here you can see `class Observable` subclasses, which have their own purpose. `class AppointmentNotifier` prints out `New appointment scheduled` message and then prints out the data. Classes `ItemSearch`, `ItemUpdate` and `ItemReceiver` have their own tasks to do. A corresponding message alongside corresponding data will be printed out.

You might wonder where are these classes are being called. Let me show you:
```
class Appointment:
# initialization
    def __str__(self):
        return f"Patient: {self.patient.name}, Doctor: {self.doctor.name}, Date: {self.date}, Time: {self.time_slot}" # here is the corresponding data that will be printed out as a string
# methods that check the status of the scheduled appointment (if it is upcoming, is it taking place right now or has it ended

class Hospital(Observable):
# initialization and rest of the class
    def schedule_appointment(self, patient_name, doctor_name, date, time_slot):
        patient = next((p for p in self.patients if p.name == patient_name), None)
        doctor = next((d for d in self.doctors if d.name == doctor_name), None)
        if not patient and not doctor:
            print('Something went wrong... Patient/Doctor not found\n')
            return

        try:
            hours, minutes = map(int, time_slot.split(':'))
            if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
                raise ValueError("Invalid time! The time should be between 00:00 and 23:59.\n")
        except ValueError as e:
            print(e)
            raise

        appointment = Appointment(patient, doctor, date, time_slot)
        self.appointments.append(appointment)
        self.notify_observers(appointment)
        print('Appointment has been scheduled successfully.\n')

```
In `schedule_appointment` method, if every stipulation is satisfied, in the `Hospital` class we schedule the appointment, then through the `appointment` object we send data to the `Appointment` class, where the data is returned as a string. The finishing touch of the implementation is the message `Appointment has been scheduled successfully` is returned.

Now, how I implemented the Observer for the item inventory:
```
class Item:
# initialization and display info method ...
    def __str__(self):
        description = f"Item name: {self.item_name}, Item quantity: {self.item_quantity}, Item category: {self.item_category}"
        if self.item_description:
            description += f", Item description: {self.item_description}"
        return description
```
In this section all of the required data is printed out as a string. Next, specific message(-s) will be printed, depending on the feature you want to operate with, This was achieved in the `Inventory` class:
```
class Inventory(Observable):
    def __init__(self):
        super().__init__()
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        self.notify_observers_items("Item added: " + str(item))

    def remove_items(self, rm_item_name):
        self.items = [item for item in self.items if item.name != rm_item_name]

    def update_item_inventory(self, item_name, new_quantity):
        for item in self.items:
            if item.item_name == item_name:
                item.item_quantity = new_quantity
                self.notify_observers_items(item)

    def search_item(self, query):
        s_result = [item for item in self.items if query.lower() in item.item_name.lower()]
        item_names = [item.item_name for item in s_result]
        result_string = ", ".join(item_names)
        self.notify_observers_items("Search results: " + result_string)
        return s_result
```
Lastly, here is how an Observer is being created for each method:
```
hospital = Hospital()
appointment_notifier = AppointmentNotifier()
hospital.add_an_observer(appointment_notifier)

inventory = Inventory()
item_receiver = ItemReceiver()
inventory.add_an_observer(item_receiver)

item_search = ItemSearch()
item_update = ItemUpdate()
inventory.add_an_observer(item_search)

inventory.add_an_observer(item_update)
```
#### Factory method:
Factory method is a creational design pattern which solves the problem of creating product objects without specifying their concrete classes. Let's take a look into Factory method in this code:
```
class Factory:  # design pattern
    @staticmethod
    def create_person(person_type, *args, **kwargs):
        if person_type == 'patient':
            return Patient(*args, **kwargs)
        elif person_type == 'doctor':
            return Doctor(*args, **kwargs)
        else:
            return "Invalid person type..."

```
As you can see, I have made that just two types of a person is available - `patient` and `doctor`. If the method receives anything else other than these two strings, a corresponding message will be shown, like `Invalid person type...`. Now, how do we create a person then? It's really simple. Here is a snippet:
```
patient_factory = Factory.create_person("patient", "Alice Rosemann", 30, "12345690", "Female", "15 Street, City")
hospital.add_patients(patient_factory)
patient_factory = Factory.create_person("patient", "Noah Robertson", 40, "14784125", "Male", "124 Main Street, City")
hospital.add_patients(patient_factory)
patient_factory = Factory.create_person("patient", "Marcus Rashford", 24, "17845236", "Male", "153 Street, City")
hospital.add_patients(patient_factory)
```
And just like that, we have created three patients, which will be stored in `self.patients = []` list (it resides in the `class Hospital`). Similarly, `self.doctors = []` is in the same `class Hospital` and will store all of the created doctors. Creating a doctor is a similar simple task, like we did when we were creating a patient:
```
doctor_factory = Factory.create_person("doctor", "Bob Smith", 25, "11223364", "Male", "Cardiologist", 200, 8)
hospital.add_doctor(doctor_factory)
doctor_factory = Factory.create_person("doctor", "Robert Ryerson", 37, "11226548", "Male", "Gynecologist", 200, 7)
hospital.add_doctor(doctor_factory)
doctor_factory = Factory.create_person("doctor", "Rosie Richards", 35, "11229578", "Female", "Nurse", 50, 12)
hospital.add_doctor(doctor_factory)
doctor_factory = Factory.create_person("doctor", "Andrew Greenwood", 32, "11224758", "Male", "Surgeon", 350, 7)
hospital.add_doctor(doctor_factory)
```

## File handling
I thought it was quite a difficult task to operate with files using all of the patients and doctors, since then Factory method would lose its credibility. Of course, I still can use Factory to create another person, but I believed there was no need because I simply wanted to showcase an instance of actually using Factory from zero. Instead of this, I thought it would be a good idea to utilize file reading and writing with another type of data - items. Firstly, I've created a text file called 'pyResults.txt'. Then my goal was to make the file stay the same if nothing really changes (here I mean the situations where I run the program multiple times. The file should contain the same data, without overwriting and appending unnecessary text). After succeeding, I've removed everything the file contained and have written some data of my own, in this case: `Paper Sheet,250,Utility,Used for documenting`. So the idea was to see if it'd remembered what was in the file before and write the new components at the end of it, without overwritting the file completely. And it worked.

Now, let's take a look at the implementation. I was executing it in the `class Inventory`:
```
# ....the code....
    def save_inventory(self, filename):
        existing_inventory = {}
        try:
            with open(filename, "r") as file:
                for line in file:
                    name, quantity, category, description = line.strip().split(',')
                    existing_inventory[name] = (int(quantity), category, description)
        except FileNotFoundError:
            pass

        for item in self.items:
            existing_inventory[item.item_name] = (item.item_quantity, item.item_category, item.item_description)

        with open(filename, "w") as file:
            for name, (quantity, category, description) in existing_inventory.items():
                file.write(f"{name},{quantity},{category},{description}\n")

    def load_inventory(self, filename):
        with open(filename, "r") as file:
            for line in file:
                name, quantity, category, description = line.strip().split(',')
                self.items.append(Item(name, int(quantity), category, description))

```
Now, you might wonder why in the `except` section I am not doing anything. It's because I want to handle an exception but I don't want to take any specific actions. The code works just fine even when I'm not actually doing anything. In addition, Chat GPT suggested that it's fine to use `pass`. The AI encouraged me actually, suggesting that using `pass` leaves the door open for future modifications, meaning I can edit the code on the get go whenever I need to, without having to refactor the existing code significantly.
