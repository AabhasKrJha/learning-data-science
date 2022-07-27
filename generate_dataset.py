# this script genetrates and stores the generated sample dataset into a csv file

import random 
from datetime import date
import csv

# --------------------------------------------------------------------------
# CREATING SAMPLE DATASET - SCORES
# --------------------------------------------------------------------------

# students list contains list of lists with student name and gender
students = (
    ['Bhuvanesh', 'M'], ['Harish', 'M'], ['Shashank', 'M'], ['Rida', 'F'], ['Ritika', 'F'], ['Akshaya', 'F'], ['Sameer', 'M'], ['Aditya', 'M'],
    ['Surya', 'M'], ['Clarence', 'M'], ['Kavya', 'F'], ['Rahul', 'M'], ['Srinidhi', 'F'], ['Gopi', 'M'], ['Sophia', 'F'], ['Goutami', 'F'],
    ['Tauseef', 'M'], ['Arshad', 'M'], ['Abirami', 'F'], ['Vetrivel', 'M'], ['Kalyan', 'M'], ['Monika', 'F'], ['Priya', 'F'], ['Deepika', 'F'],
    ['Siddharth', 'M'], ['Geeta', 'F'], ['JK', 'M'], ['Jagan', 'M'], ['Nisha', 'F'], ['Naveen', 'M'])
data_fields = ('student_number', 'name', 'gender', 'DOB', 'City', 'mathematics', 'physics', 'chemistry')
cities = ('Patna', 'Bhubaneshwar', 'Manglore', 'Nashik', 'Jabalpur', 'Aurangabad')
student_data = []

student_data.append(data_fields)

count = 0
for student in students:

    count+=1

    # getting name and gender
    name = student[0]
    gender = student[1]

    # getting random scores for subjects
    math = random.randrange(0, 100)
    phy = random.randrange(0, 100)
    chem = random.randrange(0, 100)

    # choosing a random city from the list of cities
    city = random.choice(cities)
     
    # getting a random date using random and datetime module 
    start_dt = date.today().replace(day=1, month=1).toordinal()
    end_dt = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    dob = str(random_day)[5:]

    data = (count, name, gender,dob, city, math, phy, chem)
    student_data.append(data)

# --------------------------------------------------------------------------
# STORING THE DATASET IN CSV FILE - "scores.csv"
# --------------------------------------------------------------------------

with open('scores.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(student_data)
