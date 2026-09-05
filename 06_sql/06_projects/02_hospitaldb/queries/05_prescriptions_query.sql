-- ================================================
-- Table: Prescriptions
-- Database: HospitalDB
-- Topics: CREATE, FOREIGN KEY, INSERT, SELECT
-- ================================================

-- Create Prescriptions table
-- Links to Appointments — each prescription
-- belongs to a specific appointment
CREATE TABLE Prescriptions (
    prescription_id INTEGER PRIMARY KEY,
    appointment_id INTEGER REFERENCES Appointments(appointment_id),
    medicine_name TEXT,
    dosage INT
);

-- Insert prescriptions
INSERT INTO Prescriptions
VALUES
(1, 2, 'Panado', 10),
(2, 4, 'Aspirin', 20),
(3, 3, 'Parapain', 30),
(4, 1, 'Spirit', 1),
(5, 5, 'Blufen', 40);

-- View all prescriptions
SELECT * FROM Prescriptions;