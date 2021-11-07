from src.stajotomator import Database
from src.stajotomator import ApplicationUtils
import sys


########################################################################

########## Create Student Data for intern automation ##################

########################################################################

#     Database.insertStudentsData()


########################################################################

########## Create Intern Units Data for intern automation ##############

########################################################################

#     Database.insertInternUnitsData()



##################################################################

########## Create veriables for intern automation ################

##################################################################
studentList = Database.findAllStudents()
firstName = ""
lastName = ""
tckNo = ""
type = ""
begin_date = ""
end_date = ""
intern_unit_names = []
seperator = "-"
intern_units = ""

print("**********************************************************************************************************************")
print("--->                                 Staj Birim Kapasiteleri Kontrol Ediliyor...")
print("**********************************************************************************************************************")
print(" ")
print(" ")

if len(Database.findStudentList()) > 50:
    print("Staj birimi kapasiteleri her birim için 10 kişi olmak üzere güncellendi.")
    Database.updateInternUnitCapacity(10)
else:
    print("Staj birimi kapasiteleri yeterli.")

print(" ")
print(" ")
print(" ")
#############################################

########## Intern Automation ################

############################################
print("**********************************************************************************************************************")
print("--->                                 Öğrenciler Kontrol Ediliyor...")
print("--->                                 Her Öğrenci İçin Staj Planı Hazırlanıyor...")
print("**********************************************************************************************************************")
print(" ")
print(" ")

for student in studentList:
    firstName = student[0]
    lastName = student[1]
    tckNo = student[2]
    type = student[3]
    begin_date = ApplicationUtils.getCurrentDateWithFormat()
    end_date = ApplicationUtils.getStudentInternEndDate(student[5], begin_date)
    if len(Database.findStudentInternPlanWithTckNo(tckNo)):
        print("STAJ-OTOMATOR-ERR:[Bu Öğrenci için daha önceden staj planı oluşturuldu.] || Kimlik Numarası: ", tckNo, " || İsim: ", firstName, " || Soyisim: ", lastName)
        print(" ")
    else:
        Database.insertStudentInternPlanData(firstName, lastName, tckNo, type, begin_date, end_date, ApplicationUtils.getInternUnitsByType(intern_unit_names, type))
        print(firstName, " ", lastName, " isimli öğrenci için staj planı oluşturuldu.")

print(" ")
print("**********************************************************************************************************************")
print("--->                                 Öğrenci Staj Planları")
print("**********************************************************************************************************************")


########################################################

########## Get all students intern plan ################

########################################################

Database.findAllStudentInternPlan()

print(" ")
print(" ")
print("**********************************************************************************************************************")
print("--->                                 Öğrenci Staj Sonlandırma İşlemleri")
print("**********************************************************************************************************************")
print(" ")
print(" ")
removableStudentTckNo = input("Lütfen Stajdan Çıkarmak İstediğiniz Öğrencinin TC Kimlik Numarasını Giriniz : ")
Database.deleteStudentWithTckNo(removableStudentTckNo)
print("TC Kimlik No: ", removableStudentTckNo, " olan öğrenci kayıtlardan başarılı şekilde çıkartıldı.")
print(" ")
print(" ")
while True:
    print("Staj Sonlandırma İşlemi Yapmak İçin Lütfen 'Y' Yazınız. Eğer İşlemi Sonlandırmak İstiyorsanız Lütfen 'E' Yazınız.")
    print(" ")
    user_answer = input("E (Programdan Çık) / Y (İşleme Devam Et)")
    print(" ")
    print(" ")
    if user_answer == "Y":
        removableStudentTckNo = input("Lütfen Stajdan Çıkarmak İstediğiniz Öğrencinin TC Kimlik Numarasını Giriniz : ")
        Database.deleteStudentWithTckNo(removableStudentTckNo)
        print("TC Kimlik No: ", removableStudentTckNo, " olan öğrenci kayıtlardan başarılı şekilde çıkartıldı.")
    if user_answer == "E":
        sys.exit()