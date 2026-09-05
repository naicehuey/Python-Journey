# HospitalDB — SQL Project

A PostgreSQL hospital management database
built from scratch. Second SQL project —
more complex than ComputerShopDB with
5 related tables and advanced features.

## Database Tables

### Patients
Stores patient personal information.
Uses BIGINT for phone numbers to handle
international number formats.

### Doctors
Stores doctor details and specialization.
Department assigned using ALTER TABLE
after initial creation.

### Departments
Stores hospital departments and locations.
Data corrected using UPDATE after initial
insertion — real world data management.

### Appointments
Junction table linking Patients and Doctors.
Tracks appointment date and status —
Scheduled, Completed, Cancelled, No Show.

### Prescriptions
Links medicines to specific appointments.
Each prescription belongs to one appointment.

## Table Relationships


## What I Learned

### Advanced PostgreSQL
- `ALTER TABLE ADD COLUMN` — adding columns
  to an existing table after creation
- `ADD CONSTRAINT` — adding foreign key
  constraints after table creation
- `BIGINT` — larger integer for phone numbers
- `NUMERIC(10,2)` — precise decimal for prices
- Inline `REFERENCES` — shorthand foreign key

### Database Design
- Planning related tables before writing SQL
- Junction tables — Appointments links
  Patients and Doctors together
- Foreign keys enforce data integrity —
  can't add an appointment for a
  non-existent patient or doctor
- Correcting data with UPDATE instead of
  restarting — real world approach

### Complex JOINs
- Joining 3 tables in one query
- Getting prescription info through
  Appointments as the bridge table
- Joining Doctors to Departments
  for location information

## Run Order
Scripts must be run in this order
due to foreign key dependencies:
1. `departments.sql`
2. `doctors.sql`
3. `patients.sql`
4. `appointments.sql`
5. `prescriptions.sql`
6. `joins_query.sql`

## Database: HospitalDB