-- ================================================
-- JOIN Queries
-- Database: HospitalDB
-- Topics: Multi-table JOINs across 3-4 tables
-- ================================================

-- Patient appointments with their doctors
SELECT patient_name, doctor_name, appointment_date
FROM Patients
JOIN Appointments
ON Patients.patient_id = Appointments.patient_id
JOIN Doctors
ON Doctors.doctor_id = Appointments.doctor_id;

-- Patient prescriptions — what medicine each patient received
SELECT patient_name, medicine_name, dosage
FROM Patients
JOIN Appointments
ON Patients.patient_id = Appointments.patient_id
JOIN Prescriptions
ON Appointments.appointment_id = Prescriptions.appointment_id;

-- Patient appointment status
SELECT patient_name, doctor_name, status
FROM Patients
JOIN Appointments
ON Patients.patient_id = Appointments.patient_id
JOIN Doctors
ON Doctors.doctor_id = Appointments.doctor_id;

-- Which doctor works in which department and location
SELECT doctor_name, department_name, place_location
FROM Doctors
JOIN Departments
ON Doctors.department_id = Departments.department_id;

-- Connect Patients → Appointments → Doctors → Departments in one query.