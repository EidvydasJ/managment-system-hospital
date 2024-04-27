import pytest
import datetime
from kursinis import Factory, Patient, Doctor, Hospital, Appointment


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

