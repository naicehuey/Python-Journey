-- ================================================
-- Table: Doctors
-- Database: HospitalDB
-- Topics: CREATE, INSERT, ALTER TABLE,
--         ADD COLUMN, ADD CONSTRAINT,
--         FOREIGN KEY, UPDATE
-- ================================================

-- Create Doctors table
CREATE TABLE Doctors (
    doctor_id INTEGER PRIMARY KEY,
    doctor_name TEXT,
    specialization TEXT
);

-- Insert doctors
INSERT INTO Doctors
VALUES
(1, 'James Kaliwundu', 'Family Physicians'),
(2, 'Mariana Nupolela', 'Pediatricians'),
(3, 'Namiana Kalito', 'Gynecologists'),
(4, 'Karen Tembo', 'Geriatricians'),
(5, 'Tadala Kazino', 'Cardiologists'),
(6, 'George Kazembera', 'Neurologists');

-- View all doctors
SELECT * FROM Doctors;

-- Add department_id column after table creation
-- This is ALTER TABLE — modifying an existing table
ALTER TABLE Doctors
ADD COLUMN department_id INTEGER,
ADD CONSTRAINT doctors_department_id_fkey
FOREIGN KEY (department_id)
REFERENCES Departments(department_id);

-- Assign each doctor to a department
UPDATE Doctors SET department_id = 4 WHERE doctor_id = 1;
UPDATE Doctors SET department_id = 2 WHERE doctor_id = 2;
UPDATE Doctors SET department_id = 4 WHERE doctor_id = 3;
UPDATE Doctors SET department_id = 3 WHERE doctor_id = 4;
UPDATE Doctors SET department_id = 2 WHERE doctor_id = 5;
UPDATE Doctors SET department_id = 1 WHERE doctor_id = 6;

-- Verify assignments
SELECT * FROM Doctors;