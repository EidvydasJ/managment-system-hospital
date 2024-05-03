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

##### **Inheritance:**

##### **Abstraction:**

##### **Polymorphism:**
