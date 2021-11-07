import sqlite3


def createDbTables():
    connection = sqlite3.connect('main_application_database.db');
    cursor = connection.cursor();
    ## create students table
    cursor.execute("""CREATE TABLE students (
                    first_name text,
                    last_name text,
                    tckNo text,
                    class text,
                    intern_type text,
                    intern_days integer,
                    left_intern_days integer
                    )""");
    ## create internunits table
    cursor.execute("""CREATE TABLE internunits (
                    unit_name text,
                    type text,
                    capacity integer,
                    short_intern text,
                    long_intern text
                    )""");

    connection.commit();
    print("Database executions completed successfully...");
    connection.close();


def createInternPlanDbTable():
    connection = sqlite3.connect('main_application_database.db');
    cursor = connection.cursor();

    ## create studentinternplan table
    cursor.execute("""CREATE TABLE internplan (
                    first_name text,
                    last_name text,
                    tckNo text,
                    type text,
                    begin_date text,
                    end_date text,
                    intern_unit_names text
                    )""");
    connection.commit();
    print("Database executions completed successfully...");
    connection.close();


def insertStudentsData():
    connection = sqlite3.connect('main_application_database.db');
    cursor = connection.cursor();
    student_list = [
        ('Hazal', 'Pekgöz', '36595587711', '4.Sınıf', 'Yönetim', 25, 25),
        ('Batuhan', 'Kiraz', '39583882821', '4.Sınıf', 'Yönetim', 25, 25),
        ('Güneş', 'Dünya', '46595587791', '4.Sınıf', 'Yönetim', 25, 25),
        ('Pelin', 'Takı', '32595531071', '4.Sınıf', 'Yönetim', 20, 20),
        ('Selin', 'Cura', '36595587712', '3.Sınıf', 'Üretim', 20, 20),
        ('Merve', 'Acar', '49595587711', '3.Sınıf', 'Üretim', 25, 25)
    ]
    querry = """INSERT INTO students
                          (first_name, last_name, tckNo, class, intern_type, intern_days, left_intern_days) 
                          VALUES (?, ?, ?, ?, ?, ?, ?);"""

    cursor.executemany(querry, student_list);
    connection.commit();
    print("Total", cursor.rowcount, "Records inserted successfully into [students] table")
    connection.close();


def insertInternUnitsData():
    connection = sqlite3.connect('main_application_database.db');
    cursor = connection.cursor();
    ınternUnitList = [
        ('Jet Revizyon', 'Atolye', 30, '4', '5'),
        ('Aksesuar Revizyon Müdürlüğü', 'Atolye', 30, '4', '5'),
        ('Elektronik Sistemler Müdürlüğü(ESM)', 'Atolye', 30, '4', '5'),
        ('Uçak FASBAT', 'Atolye', 30, '4', '5'),
        ('İmalat Müdürlüğü', 'Atolye', 30, '4', '5'),
        ('Kalite Güvence Baskanlıgı', 'Baskanlık', 30, '4', '5'),
        ('Teknik Yönetim Baskanlıgı', 'Baskanlık', 30, '4', '5'),
        ('Plan Program Baskanlıgı', 'Baskanlık', 30, '4', '5'),
        ('F-35 Sube Yönetim Bakım Müdürlüğü', 'Baskanlık', 30, '4', '5'),
        ('Üretim Baskanlıgı', 'Baskanlık', 30, '4', '5')
    ]
    querry = """INSERT INTO internunits
                          (unit_name, type, capacity, short_intern, long_intern) 
                          VALUES (?, ?, ?, ?, ?);"""

    cursor.executemany(querry, ınternUnitList);
    connection.commit();
    print("Total", cursor.rowcount, "Records inserted successfully into [internunits] table")
    connection.close();


def insertStudentInternPlanData(first_name, last_name, tckNo, type, begin_date, end_date, intern_unit_names):
    connection = sqlite3.connect('main_application_database.db');
    cursor = connection.cursor();
    studentInternDataPlan = [
        (first_name, last_name, tckNo, type, begin_date, end_date, intern_unit_names),
    ]
    query = """INSERT INTO internplan
                          (first_name, last_name, tckNo, type, begin_date, end_date, intern_unit_names) 
                          VALUES (?, ?, ?, ?, ?, ?, ?);"""

    cursor.executemany(query, studentInternDataPlan);
    connection.commit();
    print("Total", cursor.rowcount, "Records inserted successfully into [studentinternplan] table")
    connection.close();


def findAllStudents():
    try:
        connection = sqlite3.connect('main_application_database.db');
        cursor = connection.cursor();

        query = """SELECT * from students"""
        cursor.execute(query)

        student_list_records = cursor.fetchall()
        print("          ÖĞRENCİLER         ")
        print("*****************************")
        for row in student_list_records:
            print("                   ")
            print("***************************")
            print("First Name: ", row[0])
            print("Last Name: ", row[1])
            print("TC Kimlik No: ", row[2])
            print("Sınıfı: ", row[3])
            print("Staj Tipi: ", row[4])
            print("Staj Süresi: ", row[5])
            print("Kalan Staj Süresi: ", row[6])
            print("\n")

        return student_list_records
        cursor.close()

    except sqlite3.Error as e:
        print("Failed to read data from students table", e)
    finally:
        if connection:
            connection.close()


def findStudentList():
    try:
        connection = sqlite3.connect('main_application_database.db');
        cursor = connection.cursor();

        query = """SELECT * from students"""
        cursor.execute(query)

        student_list_records = cursor.fetchall()
        return student_list_records
        cursor.close()

    except sqlite3.Error as e:
        print("Failed to read data from students table", e)
    finally:
        if connection:
            connection.close()


def findAllInternUnits():
    try:
        connection = sqlite3.connect('main_application_database.db');
        cursor = connection.cursor();

        query = """SELECT * from internunits """
        cursor.execute(query)

        unit_list_records = cursor.fetchall()

        for row in unit_list_records:
            print("***************************")
            print("***************************")
            print("Unit Name: ", row[0])
            print("Type: ", row[1])
            print("Capacity: ", row[2])
            print("Short Period Time: ", row[3])
            print("Long Period Time: ", row[4])
            print("\n")

        cursor.close()

    except sqlite3.Error as e:
        print("Failed to read data from internunits table", e)
    finally:
        if connection:
            connection.close()


def findAllStudentInternPlan():
    try:
        connection = sqlite3.connect('main_application_database.db');
        cursor = connection.cursor();

        query = """SELECT * from internplan """
        cursor.execute(query)

        unit_list_records = cursor.fetchall()

        for row in unit_list_records:
            print("***************************")
            print("First Name: ", row[0])
            print("Last Name: ", row[1])
            print("TC Kimlik No: ", row[2])
            print("Sınıfı: ", row[3])
            print("Başlangıç Tarihi: ", row[4])
            print("Bitiş Tarihi: ", row[5])
            print("Staj Yaptığı Birimler: ", row[6])
            print("\n")

        cursor.close()

    except sqlite3.Error as e:
        print("Failed to read data from studentinternplan table", e)
    finally:
        if connection:
            connection.close()


def findAllWorkshopUnits():
    try:
        connection = sqlite3.connect('main_application_database.db');
        cursor = connection.cursor();

        query = """SELECT * from internunits where type = 'Atolye' """
        cursor.execute(query)

        workshop_unit_list_records = cursor.fetchall()
        return workshop_unit_list_records;
        cursor.close()

    except sqlite3.Error as e:
        print("Failed to read data from internunits table", e)
    finally:
        if connection:
            connection.close()


def findAllPresidentialUnits():
    try:
        connection = sqlite3.connect('main_application_database.db');
        cursor = connection.cursor();

        query = """SELECT * from internunits where type = 'Baskanlık' """
        cursor.execute(query)

        presidential_unit_list_records = cursor.fetchall()
        return presidential_unit_list_records;

        cursor.close()

    except sqlite3.Error as e:
        print("Failed to read data from internunits table", e)
    finally:
        if connection:
            connection.close()


def findAllLongManagmentInternStudents():
    try:
        connection = sqlite3.connect('main_application_database.db');
        cursor = connection.cursor();

        query = """SELECT * from students WHERE intern_type = 'Yönetim' AND  intern_days = 25"""
        cursor.execute(query)

        student_list_records = cursor.fetchall()
        return student_list_records;

        cursor.close()

    except sqlite3.Error as e:
        print("Failed to read long management data from students table", e)
    finally:
        if connection:
            connection.close()


def findAllShortManagmentInternStudents():
    try:
        connection = sqlite3.connect('main_application_database.db');
        cursor = connection.cursor();

        query = """SELECT * from students WHERE intern_type = 'Yönetim' AND  intern_days = 20"""
        cursor.execute(query)

        student_list_records = cursor.fetchall()
        return student_list_records;

        cursor.close()

    except sqlite3.Error as e:
        print("Failed to read long management data from students table", e)
    finally:
        if connection:
            connection.close()


def findAllLongManifactoringInternStudents():
    try:
        connection = sqlite3.connect('main_application_database.db');
        cursor = connection.cursor();

        query = """SELECT * from students WHERE intern_type = 'Üretim' AND  intern_days = 25"""
        cursor.execute(query)

        student_list_records = cursor.fetchall()
        return student_list_records;
        cursor.close()

    except sqlite3.Error as e:
        print("Failed to read long management data from students table", e)
    finally:
        if connection:
            connection.close()


def findAllShortManifactoringInternStudents():
    try:
        connection = sqlite3.connect('main_application_database.db');
        cursor = connection.cursor();

        query = """SELECT * from students WHERE intern_type = 'Üretim' AND  intern_days = 20"""
        cursor.execute(query)

        student_list_records = cursor.fetchall()
        return student_list_records;
        cursor.close()

    except sqlite3.Error as e:
        print("Failed to read long management data from students table", e)
    finally:
        if connection:
            connection.close()


def findStudentInternPlanWithTckNo(tckNo):
    try:
        connection = sqlite3.connect('main_application_database.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * from internplan WHERE tckNo = ?", (tckNo,))
        student_intern_plan = cursor.fetchall()
        return student_intern_plan
        cursor.close()

    except sqlite3.Error as e:
        print("Failed to read data from student intern plan table", e)
    finally:
        if connection:
            connection.close()


def findInternUnitsByType(type):
    try:
        connection = sqlite3.connect('main_application_database.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * from internunits where type = ?", (type,))

        units = cursor.fetchall()
        return units
        cursor.close()

    except sqlite3.Error as e:
        print("Failed to read data from intern units table", e)
    finally:
        if connection:
            connection.close()


def updateInternUnitCapacity(new_capacity):
    try:
        connection = sqlite3.connect('main_application_database.db')
        cursor = connection.cursor()
        cursor.execute("Update internunits set capacity = ?", (new_capacity,))
        connection.commit()
        ıntern_unit_list = cursor.fetchall()
        return ıntern_unit_list
        print("Record Updated successfully")
        cursor.close()

    except sqlite3.Error as e:
        print("Failed to update sqlite table", e)
    finally:
        if connection:
            connection.close()


def deleteStudentWithTckNo(tckNo):
    try:
        connection = sqlite3.connect('main_application_database.db')
        cursor = connection.cursor()
        cursor.execute("Delete from students Where tckNo=?", (tckNo,))
        connection.commit()
        cursor.close()

    except sqlite3.Error as e:
        print("Failed to delete data from student table", e)
    finally:
        if connection:
            connection.close()
