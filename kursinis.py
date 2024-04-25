import time
import json
curr = time.gmtime()
time_str = time.asctime(curr)
print(curr)


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

    def is_happening_now(self):
        current_time = time.gmtime()
        current_timestamp = time.mktime(current_time)
        appointment_timestamp = time.mktime(time.strptime(f"{self.date} {self.time_slot}", "%Y-%m-%d %H:%M"))
        return current_timestamp == appointment_timestamp

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
        if patient and doctor:
            appointment = Appointment(patient, doctor, date, time_slot)
            self.appointments.append(appointment)
            self.notify_observers(appointment)
            print('Appointment has been scheduled successfully.')
        else:
            print('Something went wrong... Patient/Doctor not found')

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

    def remove_patients(self, patient):
        pass

    def save_to_file(self, filename):
        data = {
            "patients": [vars(p) for p in self.patients],
            "doctors": [vars(d) for d in self.doctors],
            "appointments": [(a.patient.name, a.doctor.surname, a.date, a.time_slot) for a in self.appointments]
        }
        with open(filename, "w") as file:
            json.dump(data, file)

    def load_from_file(self, filename):
        with open("pyData.csv", "r") as file:
            data = json.load(file)
            self.patients = [Patient(**p) for p in data["patients"]]
            self.doctors = [Doctor(**d) for d in data["doctors"]]
            self.appointments = [Appointment(next((p for p in self.patients if p.name == apt[0]), None),
                                             next((d for d in self.doctors if d.name == apt[1]), None),
                                             apt[2], apt[3]) for apt in data["appointments"]]


hospital = Hospital()
appointment_notifier = AppointmentNotifier()
hospital.add_an_observer(appointment_notifier)

# current_date = time.strftime("%Y-%m-%d", time.localtime())
# current_time_slot = time.strftime("%H:%M", time.localtime())

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
hospital.schedule_appointment("Marcus Rashford", "Bob Smith", "2024-04-19", "09:17")

hospital.view_patients()
hospital.view_doctors()
hospital.view_appointments()

# f = open("duom.txt", "r")
# print(f.read())





