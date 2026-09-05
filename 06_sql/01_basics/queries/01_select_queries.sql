-- ================================================
-- File: select_queries.sql
-- Database: PracticeDB
-- Topics: CREATE, INSERT, SELECT, WHERE, AS, DISTINCT, DELETE, RETURNING, DROP
-- ================================================

-- Creating a simple Students table
CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    age INTEGER,
    grade TEXT,
    city TEXT
);

-- Inserting 5 students
INSERT INTO Students
VALUES
(1, 'James Tania', 14, 6, 'Lilongwe'),
(2, 'Mary Nania', 12, 5, 'Blantyre'),
(3, 'Frank Kanyenya', 16, 8,'Lilongwe'),
(4, 'Atupele Yadidi', 12, 7, 'Lilongwe'),
(5, 'Mineria Surez', 14, 4, 'Blantyre');

-- Now writing queries:

-- 1. Selecting all students
SELECT * FROM Students;

-- 2. Selecting only student_name and grade
SELECT student_name, grade FROM Students;

-- 3. Selecting only students from one city
SELECT student_name, city FROM Students
WHERE city = 'Lilongwe';

-- 4. Selecting students older than 13
SELECT student_name, age FROM Students
WHERE age > 13;

-- 5. Select student_name with an alias called "Full Name"
SELECT student_name AS full_name FROM Students;

-- 6. Deleting a student
DELETE FROM Students WHERE student_id = 2 RETURNING *;

-- 7. Adding one more student
INSERT INTO STudents
VAlues
(6, 'Naomi Kante', 11, 3, 'Dedza');

-- 8. Selecting only unique cities — no duplicates
SELECT DISTINCT city FROM Students;

-- 9. Drop Table
DROP TABLE Students;

-- Note: I Usually use RETURNING to show effects taken without using creating a SELECT_query separately