-- ================================================
-- Table: Departments
-- Database: HospitalDB
-- Topics: CREATE, INSERT, UPDATE, SELECT
-- ================================================

-- Create Departments table
CREATE TABLE Departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT,
    place_location TEXT
);

-- Insert departments — initial data
INSERT INTO Departments
VALUES
(1, 'Karonga Hospital', 'Karonga'),
(2, 'Blantyre Hospital', 'Blantyre'),
(3, 'Lilongwe Hospital', 'Lilongwe'),
(4, 'Zomba Hospital', 'Zomba');

-- Update to correct department names
UPDATE Departments SET department_name = 'Cardiology' WHERE department_id = 1;
UPDATE Departments SET department_name = 'Surgery' WHERE department_id = 2;
UPDATE Departments SET department_name = 'Physician' WHERE department_id = 3;
UPDATE Departments SET department_name = 'Pediatrics' WHERE department_id = 4;

-- View updated departments
SELECT * FROM Departments;