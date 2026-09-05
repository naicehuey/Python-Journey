-- ================================================
-- Table: Appointments
-- Database: HospitalDB
-- Topics: CREATE, FOREIGN KEYS, INSERT, SELECT
-- ================================================

-- Create Appointments table
-- Links Patients and Doctors together
CREATE TABLE Appointments (
    appointment_id INTEGER PRIMARY KEY,
    patient_id INTEGER REFERENCES Patients(patient_id),
    doctor_id INTEGER REFERENCES Doctors(doctor_id),
    appointment_date DATE,
    status TEXT
);

-- Insert appointment records
INSERT INTO Appointments
VALUES
(1, 2, 1, '2026-07-21', 'No Show'),
(2, 1, 3, '2026-08-28', 'Cancelled'),
(3, 4, 6, '2026-08-29', 'Scheduled'),
(4, 1, 3, '2026-09-01', 'Completed'),
(5, 3, 5, '2026-10-02', 'Scheduled');

-- View all appointments
SELECT * FROM Appointments;