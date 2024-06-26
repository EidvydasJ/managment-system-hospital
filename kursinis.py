import time
import datetime
curr = datetime.datetime.now()
print(f"Code has been executed on: ", curr)


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


class Factory:  # design pattern
    @staticmethod
    def create_person(person_type, *args, **kwargs):
        if person_type == 'patient':
            return Patient(*args, **kwargs)
        elif person_type == 'doctor':
            return Doctor(*args, **kwargs)
        else:
            return "Invalid person type..."


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


class Appointment:
    def __init__(self, patient, doctor, date, time_slot):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time_slot = time_slot

    def __str__(self):
        return f"Patient: {self.patient.name}, Doctor: {self.doctor.name}, Date: {self.date}, Time: {self.time_slot}"

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

    def view_patients(self):
        print('----- Patients -----')
        for patient in self.patients:
            patient.display_info()
            print('\n')
        print('--------------------')

    def view_doctors(self):
        print('\n')
        print('----- Doctors -----')
        for doctor in self.doctors:
            doctor.display_info()
            print('\n')
        print('--------------------')

    def view_appointments(self):
        print('\n')
        print('----- Appointments -----')
        for appointment in self.appointments:
            appointment.display_info()
            print('\n')
        print('--------------------')


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

    def __str__(self):
        description = f"Item name: {self.item_name}, Item quantity: {self.item_quantity}, Item category: {self.item_category}"
        if self.item_description:
            description += f", Item description: {self.item_description}"
        return description


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

    def display_inventory(self):
        print("----- Inventory -----")
        for item in self.items:
            item.display_info()
            print("")
        print("--------------------")

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


hospital = Hospital()
appointment_notifier = AppointmentNotifier()
hospital.add_an_observer(appointment_notifier)

patient_factory = Factory.create_person("patient", "Alice Rosemann", 30, "12345690", "Female", "15 Street, City")
hospital.add_patients(patient_factory)
patient_factory = Factory.create_person("patient", "Noah Robertson", 40, "14784125", "Male", "124 Main Street, City")
hospital.add_patients(patient_factory)
patient_factory = Factory.create_person("patient", "Marcus Rashford", 24, "17845236", "Male", "153 Street, City")
hospital.add_patients(patient_factory)

doctor_factory = Factory.create_person("doctor", "Bob Smith", 25, "11223364", "Male", "Cardiologist", 200, 8)
hospital.add_doctor(doctor_factory)
doctor_factory = Factory.create_person("doctor", "Robert Ryerson", 37, "11226548", "Male", "Gynecologist", 200, 7)
hospital.add_doctor(doctor_factory)
doctor_factory = Factory.create_person("doctor", "Rosie Richards", 35, "11229578", "Female", "Nurse", 50, 12)
hospital.add_doctor(doctor_factory)
doctor_factory = Factory.create_person("doctor", "Andrew Greenwood", 32, "11224758", "Male", "Surgeon", 350, 7)
hospital.add_doctor(doctor_factory)

hospital.schedule_appointment("Alice Rosemann", "Andrew Greenwood", "2024-04-28", "11:00")
hospital.schedule_appointment("Noah Robertson", "Bob Smith", "2024-04-20", "13:00")
hospital.schedule_appointment("Marcus Rashford", "Bob Smith", "2024-04-27", "15:45")
# hospital.schedule_appointment("Marcus Rashford", "Andrew Greenwood", "2024-05-01", "25:00")


hospital.view_patients()
hospital.view_doctors()
hospital.view_appointments()

inventory = Inventory()
item_receiver = ItemReceiver()
inventory.add_an_observer(item_receiver)
item1 = Item("Gloves", 2, "Medical device", "Mandatory for surgeons and nurses")
item2 = Item("Surgical Knife", 1, "Medical device", "Surgeon's best friend")
inventory.add_item(item1)
inventory.add_item(item2)

item_search = ItemSearch()
item_update = ItemUpdate()
inventory.add_an_observer(item_search)

inventory.load_inventory("pyResults.txt")
inventory.save_inventory("pyResults.txt")
inventory.items = []
inventory.load_inventory("pyResults.txt")

inventory.display_inventory()

Query = "Paper Sheet"
result = inventory.search_item(Query)
for item_search in result:
    item_search.display_info()

inventory.update_item_inventory("Surgical Knife", 5)
inventory.display_inventory()
inventory.add_an_observer(item_update)

new_item = Item("Disposable Syringe", 100, "Medical device", "Single-use syringes for medical procedures")
inventory.add_item(new_item)
inventory.save_inventory("pyResults.txt")
inventory.display_inventory()
