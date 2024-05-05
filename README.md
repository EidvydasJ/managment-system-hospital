# Simple Hospital Management System

## Overview
This hospital management system is a Python program designed to help manage patient and doctor rosters, manage visits and inventory in a hospital environment. It includes features for planning visits, managing information about patients and doctors, and managing the inventory of medical tools and equipment. You should be able to run this program on any code editing sotfware like Visual Studio Code, PyCharm. Well, this course work has been done using PyCharm because it offered the easiest way of operating with files, as well as PyCharm recognised Git, so they easily got paired. As a result, I could commit my changes via PyCharm, not even having to open Git Bash.

Using this program is quite easy - as it was the point of my work. Unfortunately, I've had issues with this work even though I was trying to do stuff in the easiest way possible. Perhaps that is why, as a user, you have to be careful while operating with data file "pyResults.txt". Sometimes, this file may lead to misbehavior in the results, as will be shown in a screenshot a little bit later. But other than that, everything else is relatively easy to comprehend. All you have to do is call necessary methods, functions with corresponding data. Without further ado, let's dive into it.

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
I've realised that to this date I don't see the difference between Encapsulation and Abstraction. I really feel like they are the same thing, even though I've been told otherwise. Even the examples I've seen couldn't help me understand it more. Just for this case, I've asked Chat GPT to look for potential examples of Abstraction. Obviously, GPT finds and generates anything you need. Well, the results are as follows:

```
class Item:
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
```
class Hospital(Observable):
    def __init__(self):
        super().__init__()
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patients(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def schedule_appointment(self, patient_name, doctor_name, date, time_slot):
        patient = next((p for p in self.patients if p.name == patient_name), None)
        doctor = next((d for d in self.doctors if d.name == doctor_name), None)
        if not patient and not doctor:
            print('Something went wrong... Patient/Doctor not found\n')
            return
# ...
```
Presumably, these examples can be considered as potential examples of Abstraction, because when I define a class, I'm abstracting away the implementation details and focusing on defining the structure and behavior of objects. Users of the class don't need to know how the class is implemented internally and they only need to understand how to interact with its public interface. You only need to know what each method does and how to use it and if you know how it works, well, you can simply call the methods you need without worrying about the underlying logic or algorithms. 
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

`save_inventory` method is used for saving the current state of the inventory to a file specified by `filename`, which is the mentioned before 'pyResults.txt'. It first creates a dictionary `existing_inventory` to store the data to be written to the file. It attempts to open the file specified by `filename` in read mode ("r"). If the file exists, it reads its contents and populates `existing_inventory` with the data. If the file does not exist, it raises a `FileNotFoundError`, which is being monitored in the `except` block. If the file exists, the method reads each line, splitting it into fields (name, quantity, category, description), and adds the data to `existing_inventory`. After reading the existing data (or if no existing data is found), the method updates `existing_inventory` with the current inventory data. It then opens the file again, this time in write mode ("w"), and writes the contents of `existing_inventory` back to the file, effectively updating it with the latest inventory information. 

`load_inventory` method is responsible for loading inventory data from 'pyResults.txt'. It opens the file in read mode ("r"). It then iterates over each line in the file, splitting it into fields (name, quantity, category, description), and creates `Item` objects from the data. For each line in the file, it creates an `Item` object with the extracted data and adds it to the inventory. After processing all lines in the file, the method closes the file. These methods provide a way to persist inventory data to a file (`save_inventory`) and retrieve inventory data from a file (`load_inventory`). They are essential for maintaining data between program executions and for sharing data between different instances of the program.

Here's how I create an item:
```
item1 = Item("Gloves", 2, "Medical device", "Mandatory for surgeons and nurses")
item2 = Item("Surgical Knife", 1, "Medical device", "Surgeon's best friend")
inventory.add_item(item1)
inventory.add_item(item2)

new_item = Item("Disposable Syringe", 100, "Medical device", "Single-use syringes for medical procedures")
inventory.add_item(new_item)
```
With all of the implementations mentioned, here is how the file 'pyResults.txt' is looking after running the code:

![image](https://github.com/EidvydasJ/managment-system-hospital/assets/167422894/d14ac4bd-f025-4538-b8ce-fb51f0d5df21)

## Unit testing
```
import pytest
import datetime
from kursinis import Factory, Patient, Doctor, Hospital, Appointment
```
I've created 8 tests using `pytest`. The tests feature these topics:
- **Testing Factory Method**
- **Testing For Valid Appointment Scheduling**
- **Testing For Appointment Status**

#### Testing Factory Method:
```
@pytest.fixture
def sample_patient_data():
    return ("Alice Rosemann", 30, "12345690", "Female", "15 Street")


@pytest.fixture
def sample_doctor_data():
    return ("Bob Smith", 25, "11223364", "Male", "Cardiologist", 200, 8)


def test_create_patient(sample_patient_data):
    name, age, phone, gender, address = sample_patient_data
    patient = Factory.create_person("patient", name, age, phone, gender, address)
    assert isinstance(patient, Patient)
    assert patient.name == name
    assert patient.age == age
    assert patient.phone == phone
    assert patient.gender == gender
    assert patient.address == address


def test_create_doctor(sample_doctor_data):
    name, age, phone, gender, specialization, hourly_rate, hours_worked = sample_doctor_data
    doctor = Factory.create_person("doctor", name, age, phone, gender, specialization, hourly_rate, hours_worked)
    assert isinstance(doctor, Doctor)
    assert doctor.name == name
    assert doctor.age == age
    assert doctor.phone == phone
    assert doctor.gender == gender
    assert doctor.specialization == specialization
    assert doctor.hourly_rate == hourly_rate
    assert doctor.hours_worked == hours_worked

```
This is how I've tested if the Factory Method works the way it is intended to work. Factory successfully creates a person- both doctor and patient.
#### Testing For Valid Appointment Scheduling:
```
@pytest.fixture
def hospital():
    hospital_instance = Hospital()
    hospital_instance.add_patients(Patient("Alice Rosemann", 30, "12345690", "Female", "15 Street"))
    hospital_instance.add_patients(Patient("Noah Robertson", 40, "14784125", "Male", "124 Main Street"))
    hospital_instance.add_doctor(Doctor("Bob Smith", 25, "11223364", "Male", "Cardiologist", 200, 8))
    hospital_instance.add_doctor(Doctor("Robert Ryerson", 37, "11226548", "Male", "Gynecologist", 200, 7))
    return hospital_instance


def test_valid_appointment_scheduling(hospital):
    hospital.schedule_appointment("Alice Rosemann", "Bob Smith", "2024-04-28", "11:00")
    assert len(hospital.appointments) == 1


def test_invalid_appointment_scheduling(hospital):
    hospital.schedule_appointment("Jarrod Bowen", "Andrew Greenwood", "2024-04-28", "11:00")
    assert len(hospital.appointments) == 0


def test_invalid_time_slot(hospital):
    with pytest.raises(ValueError):
        hospital.schedule_appointment("Noah Robertson", "Robert Ryerson", "2024-05-01", "25:00")

```
Now, in `def test_valid_appointment_scheduling` you can see, that pytest should expect an addition to the appointments list (because if an appointment is valid, the list extends its length by 1). Oppositely, in `def test_invalid_appointment_scheduling` you can see, that pytest should expect the appointments list to remain unchanged (if appointment is invalid, the list doesn't get extended, hence the length is 0, to make things easier).
#### Testing For Appointment Status:
```
@pytest.fixture
def sample_appointment_data(hospital):
    patient = hospital.patients[0]
    doctor = hospital.doctors[0]
    return (patient, doctor, "2024-04-27", "16:17")

def test_appointment_is_upcoming(hospital, sample_appointment_data):
    patient, doctor, date, time_slot = sample_appointment_data
    appointment = Appointment(patient, doctor, date, time_slot)
    assert appointment.is_upcoming() == False

def test_appointment_has_ended(hospital, sample_appointment_data):
    patient, doctor, date, time_slot = sample_appointment_data
    appointment = Appointment(patient, doctor, date, time_slot)
    assert appointment.has_ended() == True

def test_appointment_is_happening_now(hospital, sample_appointment_data):
    patient, doctor, date, time_slot = sample_appointment_data
    # Get the current date and time
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.strftime("%Y-%m-%d")
    current_time = current_datetime.strftime("%H:%M")
    appointment_hours, appointment_minutes = map(int, time_slot.split(':'))
    current_hours, current_minutes = map(int, current_time.split(':'))
    time_difference = abs((current_hours * 60 + current_minutes) - (appointment_hours * 60 + appointment_minutes))
    threshold_minutes = 15
    appointment_is_happening_now = time_difference <= threshold_minutes
    appointment = Appointment(patient, doctor, date, time_slot)
    assert appointment.is_happening_now() == appointment_is_happening_now

```
The way these tests work, is that you manually choose a date and time, like in the example above: `return (patient, doctor, "2024-04-27", "16:17")`. Next step for you is to manually set boolean values for each test that will be performed. In this case, we assert that today is `2024-05-05 21:43`. Clearly, this appointment should have ended by now. Hence why the boolean values are as follows: `assert appointment.is_upcoming() == False`, `assert appointment.has_ended() == True` and `assert appointment.is_happening_now() == appointment_is_happening_now`. Notice that in the last test we dont actually specify the boolean value. Instead, we have much more sophisticated implementation. Much like in the main code, we need to split the hours and minutes apart and then calculate time difference. Here in `appointment_is_happening_now = time_difference <= threshold_minutes`, `time_difference` represents the difference in minutes between the current time and the time of the appointment. `threshold_minutes` is a pre-defined threshold indicating the maximum allowed difference in minutes (15) for an appointment to be considered as currently happening. If the condition is satisfied, it means that the appointment is happening now, as the difference in time between the current time and the appointment time is within the allowed threshold. Otherwise, if the condition is false, the appointment is not happening now.
So, in this case, the boolean value is `False`.
 
## Difficulties; potential problems that will require additional attention
#### Difficulties:

It wasn't very simple to implement everything that I've wanted to. At the end of the day, I take all of this work as a huge positive. However there are issues worth mentioning before heading towards results and conclusions.

My biggest nightmare was to operate with the time. That includes checking if the appointment is valid, checking the status. Luckily, I was able to relatively succeed regardless.
```
import time
import datetime
curr = datetime.datetime.now()
print(f"Code has been executed on: ", curr)
```
This is a snippet of the very first lines in my code. Purpose is quite simple - to show what time the code has been executed. Output in the terminal:

![image](https://github.com/EidvydasJ/managment-system-hospital/assets/167422894/341505ab-cd28-4f8d-8ea8-a50ec5410525)

I tried using `time.localtime()`, `time.gmtime()` alongside `time.mktime()`, `time.strftime()` methods, but to no avail. That was until I asked Copilot for help. Copilot helped me to resolve this issue. As you can see, the time is shown just like I wanted to. 

Now, the next instance where I had to operate with time was appointment scheduling.
```
class Appointment:
# ...
    def is_happening_now(self):
        current_time = time.localtime()
        current_date = time.strftime("%Y-%m-%d", current_time)
        current_time_slot = time.strftime("%H:%M", current_time)

        if self.date != current_date:
            return False

        appointment_hours, appointment_minutes = map(int, self.time_slot.split(':'))

        current_hours, current_minutes = map(int, current_time_slot.split(':'))

        time_difference = abs((current_hours * 60 + current_minutes) - (appointment_hours * 60 + appointment_minutes))
        return time_difference <= 15

    def has_ended(self):
        current_time = time.localtime()
        current_date = time.strftime("%Y-%m-%d", current_time)
        current_time_slot = time.strftime("%H:%M", current_time)
        return self.date < current_date or (self.date == current_date and self.time_slot < current_time_slot)

    def is_upcoming(self):
        return not self.is_happening_now() and not self.has_ended()
```
I've made that an appointment would be 15 minutes. This is how I could operate with the time and check the status of the appointment. Toughest part here is perhaps utilizing `map() .split(':')` function, where I split hours and minutes apart and operate independently. But firstly, I have to check this condition- `if self.date != current_date: return False`. If the appointment's date matches the current date, the method calculates the time difference between the appointment's time slot and the current time. It converts both the appointment time slot and the current time to minutes since midnight to facilitate comparison. The method checks if the time difference calculated is less than or equal to 15 minutes. This threshold is used to determine if the appointment is considered to be happening now. If the difference is within the threshold, it returns `True`, indicating that the appointment is currently ongoing. If the difference exceeds the threshold, it returns `False`, indicating that the appointment is not currently ongoing.

Now, `has_ended` method is responsible for ensuring if the appointment has already ended. The logic is simple here, as the current date and time should exceed the appointment date and time, should the appointment be finished.

Finally, easiest logic here in `is_upcoming` method. We simply say that if none of the cases are true, that means only one can be true. That is why there's only one line needed: `return not self.is_happening_now() and not self.has_ended()`.

Okay, but where do we *actually* check the appointment status?
```
class Appointment:
# ...
    def display_info(self):
        print("Patient: ", self.patient.name)
        print("Doctor: ", self.doctor.name)
        print(f"Date {self.date}, time {self.time_slot}")

        if self.is_happening_now():
            print("This appointment is happening right now.")
        elif self.is_upcoming():
            print("This appointment is upcoming.")
        elif self.has_ended():
            print("This appointment has ended.")
```
Simple as that, right?

```
class Hospital(Observable):
# ...
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
Here I've been told by Chat GPT to use this way of scheduling the appointments. Firstly, we check if the patient that is looking forward to visit a doctor is existing, much like we check if the doctor is existing. If the output is `False` (meaning the doctor and the patient have been found in their respective lists `self.patients` and `self.doctors`), we are safe to move to the next check phase. If the output is `True`, a message `Something went wrong... Patient/Doctor not found` is printed. In the `try-except` block, I am checking if the time format is correct. The time cannot be `-01:65` or `25:00`, right?

#### Potential problems that will require additional attention:

Main issue I am seeing im my work is actually related to files. If you run the program multiple times, the file does not change, like I wanted. But, a problem occurs because of the file. You see, the results I am seeing may not be consistent. Let's take the shaped file as an example:

![image](https://github.com/EidvydasJ/managment-system-hospital/assets/167422894/d14ac4bd-f025-4538-b8ce-fb51f0d5df21)

Let's look at the output terminal:

![image](https://github.com/EidvydasJ/managment-system-hospital/assets/167422894/f7055554-5d34-476b-abcf-5c55e1bf9b0b)

![image](https://github.com/EidvydasJ/managment-system-hospital/assets/167422894/5b096945-443c-403e-8914-e86ad5c0c3eb)

![image](https://github.com/EidvydasJ/managment-system-hospital/assets/167422894/ea53f593-0993-4ada-9c23-39cf8d420f3e)

![image](https://github.com/EidvydasJ/managment-system-hospital/assets/167422894/7e1ddca2-95e9-49da-a072-5c45fcab3b57)

![image](https://github.com/EidvydasJ/managment-system-hospital/assets/167422894/c4c99c16-5873-45be-a267-648acb7ad085)

As you can clearly see, the program behaves weirdly. At some cases, it shouldn't print unnecessary lines, as well as duplicates (disposable syringes). Well, let's try to remove the last line. That line is actually an instance where I'm creating an item and then saving it in the inventory and later on command to load.

![image](https://github.com/EidvydasJ/managment-system-hospital/assets/167422894/979b3477-90be-4324-82a0-f9982c6ddd84)

Now take a look at the results:

![image](https://github.com/EidvydasJ/managment-system-hospital/assets/167422894/a66e3544-2c6f-4561-a909-46be5b5b9c7d)

![image](https://github.com/EidvydasJ/managment-system-hospital/assets/167422894/dc0c308c-8269-4637-b617-5969eb41bec2)

![image](https://github.com/EidvydasJ/managment-system-hospital/assets/167422894/08de68e8-5e60-4e5c-847c-7ada090cfca2)

![image](https://github.com/EidvydasJ/managment-system-hospital/assets/167422894/ba4c53d5-51ac-4ae9-ab36-a016a2964374)

Even though there still are some unnecessary text, but hey, the difference is clear, right? That concludes it for this section. This would be the only reminder- either to remove content from the file, or to change the data before running the program.

#### Possible improvements?
Well, firstly, I think that I really should fully comprehend basics - OOP pillars. Most likely, I haven't fulfilled the task of implementing all 4 of them, due to the fact that I can't tell the difference between Encapsulation and Abstraction.

Perhaps, searching an item should be implemented in the other way so it would not interfere with the rest of the code:
```
Query = "Paper Sheet"
result = inventory.search_item(Query)
for item_search in result:
    item_search.display_info()
```
Or maybe I should really work on where I should use these:
```
inventory.load_inventory("pyResults.txt")
inventory.save_inventory("pyResults.txt")
inventory.display_inventory()
```
Because these little fellas might be the reason my results could be inconsistent in the long run. Quite possibly, that using `inventory.items = []` more often could help me operate with the data more easily, as `inventory.items = []` this operation should remove all items from the inventory, making it empty. 

Another part which could be improved is not to use something in the code, if I don't need it or don't plan to use it, like:
```
    def remove_items(self, rm_item_name):
        self.items = [item for item in self.items if item.name != rm_item_name]
```
or:
```
    def remove_an_observer(self, observer):
        self._observers.append(observer)
```
Basically, I've added these implementations just for the sake of it. Do I really need them? Not necessarily. Should they really be here? Most likely not, due to the fact that I'm not sure how to utilize them.

## Results and Conclusion

The completion of this coursework has me yielded a quite decent and solid understanding of Object-Oriented Programming concept even though it was quite a task to make a transition from Procedural Programming. Even though I've had difficulties to implement everything I've wanted and my code having plenty of room to be improved, I am more than happy with the results of my course work. As a non-really-programming person, I've found that with the help from AI even though it generated a lot of my code, I've basically understood everything AI has offered me. Well, speaking of the code itself, once again, the only reminder- either to remove content from the file, or to change the data before running the program. This way the code should be executed smoothly and the results are relatively accurate.

In conclusion, the transition from Procedural Programming to OOP in such short time span was difficult. Fully comprehending and utilizing all of the OOP pillars, as well as including design patterns of my own choice, when I really did not know where to use them to their best extent in my code was indeed a tough task to fulfill. However, like I've mentioned before, I take all of this work as a huge positive. All things considered, I feel like this course work really induced me to give my absolute everything towards creating a decent implementation of my idea. Even though I found time to complain to the universe about how difficult it was for me, I've found my way through all of it (luckily I can be a hungry learner sometimes).
