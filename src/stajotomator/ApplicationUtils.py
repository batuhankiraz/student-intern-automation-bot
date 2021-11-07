from datetime import date, timedelta
from src.stajotomator import Database

def getCurrentDateWithFormat():
    return date.today();

def getStudentInternEndDate(internTime, begin_date):
    student_intern_time = int(internTime);
    end_date = begin_date + timedelta(student_intern_time);
    return end_date;

def getInternUnitsByType(intern_unit_names, student_intern_type):
    seperator = "-"
    intern_units = ""
    unit_const = "Yönetim"

    if (student_intern_type == unit_const):
        for unit in Database.findAllPresidentialUnits():
            intern_unit_names.append(unit[0])
        intern_units = seperator.join(intern_unit_names)

    else:
        for unit in Database.findAllWorkshopUnits():
            intern_unit_names.append(unit[0])
        intern_units = seperator.join(intern_unit_names)

    return intern_units
