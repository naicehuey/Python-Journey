-- ================================================
-- Table: Patients
-- Database: HospitalDB
-- Topics: CREATE, BIGINT data type, INSERT, SELECT
-- ================================================

-- Create Patients table
-- BIGINT used for phone — handles large number formats
CREATE TABLE Patients (
    patient_id INTEGER PRIMARY KEY,
    patient_name TEXT,
    date_of_birth DATE,
    phone BIGINT
);

-- Insert patients
INSERT INTO Patients
VALUES
(1, 'John Machinga', '1998-04-09', 265893467832),
(2, 'Mary Kasinja', '1995-06-04', 265998376463),
(3, 'Napiya Kasamba', '1967-05-03', 265984973920),
(4, 'Manesi Kalile', '1937-04-03', 265898468367),
(5, 'Namia Jamire', '2000-09-05', 265894028346);

-- View all patients
SELECT * FROM Patients;