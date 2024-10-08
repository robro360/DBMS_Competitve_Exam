# '''
# This program generates random marks for the students whose ID's and names were already created in generate_master_data program and stored in MySQL. It Stores them in SQL Database.
# '''

# import numpy as np
# import random
# import mysql.connector as msql
# import getpass

# def get_student_marks():
#     password = getpass.getpass('Enter Password for MySQL: ')
#     conect = msql.connect(host = 'localhost', user = 'root', passwd = password, database = 'JEE_Mains')
#     cursor = conect.cursor()
#     cursor.execute("SELECT Reg_ID FROM Student_Master;")
#     lis = cursor.fetchall()
#     cursor.execute('CREATE TABLE Registration_Control (Reg_ID CHAR(11), Attempt_Number INT, Session_Number INT,PRIMARY KEY (Reg_ID, Attempt_Number));')
#     for i in range(8):
#         cursor.execute('DROP TABLE IF EXISTS Session%s' %(str(i + 1)))
#         cursor.execute('CREATE TABLE Session%s (Reg_ID CHAR(11) NOT NULL PRIMARY KEY, Math_Marks Integer, Phy_Marks Integer, Chem_Marks Integer, Total Integer, Math_Percentile FLOAT(10, 7), Phy_Percentile FLOAT(10, 7), Chem_Percentile FLOAT(10, 7), Total_Percentile FLOAT(10, 7));' %(str(i + 1)))
#     conect.commit()

#     bands = []
#     probs = []
#     band1 = (-20, -10, 0.1)
#     band2 = (-10, 0, 0.1)
#     band3 = (0, 10, 0.2)
#     band4 = (10, 20, 0.2)
#     band5 = (20, 30, 0.1)
#     band6 = (30, 40, 0.1)
#     band7 = (40, 50, 0.1)
#     band8 = (50, 60, 0.05)
#     band9 = (60, 70, 0.02)
#     band10 = (70, 77, 0.01)
#     band11 = (77, 83, 0.01)
#     band12 = (83, 88, 0.0055)
#     band13 = (88, 92, 0.0025)
#     band14 = (92, 95, 0.0013)
#     band15 = (95, 97, 0.0005)
#     band16 = (97, 99, 0.00018)
#     band17 = (99, 100, 0.00002)
    
#     for i in range(1, 18):
#         a = 'band' + str(i)
#         bands.append(a)
#         a = eval(a)
#         probs.append(a[2])

#     for i in range (len(lis)):
#         #attempts = np.random.choice([1,2,3], p = [0.25, 0.25, 0.5])
#         #attempts = np.random.choice([1,2], p = [0.5, 0.5])
#         for attempts in range(1,3):
#             try:
#                 cursor.execute("INSERT INTO Registration_Control (Reg_ID, Attempt_Number, Session_Number) VALUES ('%s',%d,%d);"  (str(lis[i][0], attempts, i)))
#                 if attempts == 1:
#                     marks_band = eval(np.random.choice(bands, p = probs))
#                     math_marks = random.randint(marks_band[0], marks_band[1])
#                     phy_marks = random.randint(marks_band[0], marks_band[1])
#                     chem_marks = random.randint(marks_band[0], marks_band[1])
#                     num = random.choice([1,2,3,4])
#                     cursor.execute("INSERT INTO Session%s (Reg_ID, Math_Marks, Phy_Marks, Chem_Marks, Attempt) VALUES ('%s', '%s', '%s', '%s', '%s')" %(str(num), str(lis[i][0]), str(math_marks), str(phy_marks), str(chem_marks), str(attempts)))
#                     conect.commit()
#                     cursor.execute('UPDATE Student_Master SET Attempt1 = %s WHERE Reg_ID = "%s";' %(str(num), str(lis[i][0])))
#                     conect.commit()

#                 elif attempts == 2:
#                     marks_band = eval(np.random.choice(bands, p = probs))
#                     math_marks = random.randint(marks_band[0], marks_band[1])
#                     phy_marks = random.randint(marks_band[0], marks_band[1])
#                     chem_marks = random.randint(marks_band[0], marks_band[1])
#                     num = random.choice([5,6,7,8])
#                     cursor.execute("INSERT INTO Session%s (Reg_ID, Math_Marks, Phy_Marks, Chem_Marks) VALUES ('%s', '%s', '%s', '%s')" %(str(num), str(lis[i][0]), str(math_marks), str(phy_marks), str(chem_marks)))
#                     conect.commit()
#                     cursor.execute('UPDATE Student_Master SET Attempt2= %s WHERE Reg_ID = "%s";' %(str(num), str(lis[i][0])))
#                     conect.commit()
#             except:
#                 pass

#         # elif attempts == 3:
#         #     num = random.choice([1,2,3,4])
#         #     cursor.execute("INSERT INTO Session%s (Reg_ID, Math_Marks, Phy_Marks, Chem_Marks) VALUES ('%s', '%s', '%s', '%s')" %(str(num), str(lis[i][0]), str(math_marks), str(phy_marks), str(chem_marks)))
#         #     conect.commit()
#         #     cursor.execute('UPDATE Student_Master SET Attempt1 = %s WHERE Reg_ID = "%s";' %(str(num), str(lis[i][0])))
#         #     conect.commit()

#         #     math_marks = random.randint(marks_band[0], marks_band[1])
#         #     phy_marks = random.randint(marks_band[0], marks_band[1])
#         #     chem_marks = random.randint(marks_band[0], marks_band[1])

#         #     num = random.choice([5,6,7,8])
#         #     cursor.execute("INSERT INTO Session%s (Reg_ID, Math_Marks, Phy_Marks, Chem_Marks) VALUES ('%s', '%s', '%s', '%s')" %(str(num), str(lis[i][0]), str(math_marks), str(phy_marks), str(chem_marks)))
#         #     conect.commit()
#         #     cursor.execute('UPDATE Student_Master SET Attempt2 = %s WHERE Reg_ID = "%s";' %(str(num), str(lis[i][0])))
#         #     conect.commit()

#     for i in range(1,9):
#         cursor.execute('UPDATE Session%s SET Total = Math_Marks + Phy_Marks + Chem_Marks;' %(str(i)))
#         conect.commit()
    
#     conect.close()
# #__main__
# get_student_marks()

import numpy as np
import random
import mysql.connector as msql
import getpass

def get_student_marks():
    password = "hello"
    #password = getpass.getpass('Enter Password for MySQL: ')
    conect = msql.connect(host='localhost', user='root', passwd=password, database='JEE_Mains')
    cursor = conect.cursor()
    
    # Fetch all student IDs
    cursor.execute("SELECT Reg_ID FROM Student_Master;")
    lis = cursor.fetchall()

    # Create the Registration_Control table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Registration_Control (
        Reg_ID CHAR(11), 
        Attempt_Number INT, 
        Session_Number INT, 
        PRIMARY KEY (Reg_ID, Attempt_Number),
        FOREIGN KEY (Reg_ID) REFERENCES Student_master(Reg_ID) ON DELETE CASCADE
    );
""")

    # Create Session tables if they do not exist
    for i in range(8):
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS Session{i + 1} (
                Reg_ID CHAR(11), 
                Math_Marks Integer, 
                Phy_Marks Integer, 
                Chem_Marks Integer, 
                Total Integer, 
                Math_Percentile FLOAT(10, 7), 
                Phy_Percentile FLOAT(10, 7), 
                Chem_Percentile FLOAT(10, 7), 
                Total_Percentile FLOAT(10, 7),
                FOREIGN KEY (Reg_ID) REFERENCES Student_master(Reg_ID) ON DELETE CASCADE,
                PRIMARY KEY (Reg_ID)
            );
        """)
    conect.commit()

    # Define the bands for marks generation
    bands = [
        (-20, -10, 0.1), (-10, 0, 0.1), (0, 10, 0.2), (10, 20, 0.2),
        (20, 30, 0.1), (30, 40, 0.1), (40, 50, 0.1), (50, 60, 0.05),
        (60, 70, 0.02), (70, 77, 0.01), (77, 83, 0.01), (83, 88, 0.0055),
        (88, 92, 0.0025), (92, 95, 0.0013), (95, 97, 0.0005), (97, 99, 0.00018),
        (99, 100, 0.00002)
    ]
    
    probs = [band[2] for band in bands]

    # Insert marks into session tables
    for student in lis:
        reg_id = student[0]
        for attempts in range(1, 3):
            try:
                # Insert into Registration_Control
                cursor.execute(
                    "INSERT INTO Registration_Control (Reg_ID, Attempt_Number, Session_Number) VALUES (%s, %s, %s)", 
                    (reg_id, attempts, attempts)
                )
                
                # Generate marks based on bands
                marks_band = random.choices(bands, probs)[0]
                math_marks = random.randint(marks_band[0], marks_band[1])
                phy_marks = random.randint(marks_band[0], marks_band[1])
                chem_marks = random.randint(marks_band[0], marks_band[1])
                
                if attempts == 1:
                    num = random.choice([1, 2, 3, 4])
                    cursor.execute(f"""
                        INSERT INTO Session{num} (Reg_ID, Math_Marks, Phy_Marks, Chem_Marks) 
                        VALUES (%s, %s, %s, %s)
                    """, (reg_id, math_marks, phy_marks, chem_marks))
                    conect.commit()
                    cursor.execute("UPDATE Student_Master SET Attempt1 = %s WHERE Reg_ID = %s;", (num, reg_id))
                    conect.commit()
                
                elif attempts == 2:
                    num = random.choice([5, 6, 7, 8])
                    cursor.execute(f"""
                        INSERT INTO Session{num} (Reg_ID, Math_Marks, Phy_Marks, Chem_Marks) 
                        VALUES (%s, %s, %s, %s)
                    """, (reg_id, math_marks, phy_marks, chem_marks))
                    conect.commit()
                    cursor.execute("UPDATE Student_Master SET Attempt2 = %s WHERE Reg_ID = %s;", (num, reg_id))
                    conect.commit()

            except msql.Error as err:
                # Check for duplicate key error (MySQL error code 1062)
                if err.errno == 1062:
                    print(f"Duplicate entry found for Reg_ID {reg_id} and Attempt_Number {attempts}. Skipping...")
                else:
                    print(f"Error: {err}")
                conect.rollback()

    # Update the total marks for each session
    for i in range(1, 9):
        cursor.execute(f'UPDATE Session{i} SET Total = Math_Marks + Phy_Marks + Chem_Marks;')
        conect.commit()
    
    conect.close()

# Main
get_student_marks()
