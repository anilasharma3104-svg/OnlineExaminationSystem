# SHHSS Online Examination Platform

This is a Python-based online examination system using MySQL database.

It supports:
- Student login and exam attempt
- Teacher question creation
- Management record handling

-----------------------------------

## Technologies Used

- Python 3
- MySQL
- mysql-connector-python

-----------------------------------

## Installation Steps

1. Clone the repository

git clone https://github.com/anilasharma3104-svg/OnlineExaminationSystem.git

2. Install required package

pip install -r requirements.txt

3. Create MySQL database

Run the following in MySQL:

CREATE DATABASE MANAGEMENT;

CREATE TABLE students (
    ADM_NO INT PRIMARY KEY,
    NAME VARCHAR(50),
    CLASS INT,
    SECTION VARCHAR(5),
    AGE INT
);

CREATE TABLE teachers (
    ID INT PRIMARY KEY,
    NAME VARCHAR(50),
    SUBJECT VARCHAR(50),
    AGE INT
);

CREATE TABLE management (
    ID INT PRIMARY KEY,
    NAME VARCHAR(50),
    AGE INT
);

-----------------------------------

## How to Run

python exam.py

-----------------------------------

## Features

✔ Student can attempt exam  
✔ Teacher can create exam questions  
✔ Management can add new members  
✔ Automatic score calculation  

-----------------------------------

## Future Improvements

- Convert to GUI application
- Deploy online version

-----------------------------------

Author: Anila Sharma
