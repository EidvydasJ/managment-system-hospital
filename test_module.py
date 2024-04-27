import pytest
from kursinis import Factory, Patient, Doctor, Hospital


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
    hospital = Hospital()
    hospital.add_patients(Patient("Alice Rosemann", 30, "12345690", "Female", "15 Street"))
    hospital.add_patients(Patient("Noah Robertson", 40, "14784125", "Male", "124 Main Street"))
    hospital.add_doctor(Doctor("Bob Smith", 25, "11223364", "Male", "Cardiologist", 200, 8))
    hospital.add_doctor(Doctor("Robert Ryerson", 37, "11226548", "Male", "Gynecologist", 200, 7))
    return hospital


def test_valid_appointment_scheduling(hospital):
    hospital.schedule_appointment("Alice Rosemann", "Bob Smith", "2024-04-28", "11:00")
    assert len(hospital.appointments) == 1


def test_invalid_appointment_scheduling(hospital):
    hospital.schedule_appointment("Jarrod Bowen", "Andrew Greenwood", "2024-04-28", "11:00")
    assert len(hospital.appointments) == 0


def test_invalid_time_slot(hospital):
    with pytest.raises(Exception):
        hospital.schedule_appointment("Marcus Rashford", "Robert Ryerson", "2024-05-01", "25:00")
