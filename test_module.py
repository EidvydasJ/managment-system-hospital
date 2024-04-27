import pytest
from kursinis import Factory, Patient, Doctor


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
