from FinalProject import Employee
import os
import pickle
import re
import sys
import time
import yaml
import pprint

def clear() : 
    if os.name == "nt" :
        _ = os.system("cls")
    else : 
        _ = os.system("clear")

try : 
    database = "employee_database.txt"
    inputFile = open(database, 'rb')
    dictionary = pickle.load(inputFile)
    inputFile.close()
except : 
    dictionary = {}
    

def menu():
    while True:
        print("1. Add New Employee\n")
        print("2. Delete Employee\n")
        print("3. Find Emplyoee Based on ID\n")
        print("4. Print Employee Database\n")
        print("5. Change Aspects of Employee\n")
        print("6. Quit Program/Save\n")
        print("\n")
        menuselection = input("What Menu Selection? 1-6?")
        try: 
            if menuselection.isdigit() == False :
                raise ValueError
            if menuselection == "1":
                clear()
                getstuff()
            elif menuselection == "2":
                clear()
                delpeeps()
            elif menuselection == "3":
                clear()
                findstuff()
            elif menuselection == "4":
                clear()
                showeverything()
            elif menuselection == "5":
                clear()
                changeaspects()
            elif menuselection == "6":
                clear()
                breaktime() 
            elif menuselection == "7":
                clear()
                cleardict()
            else:
                clear()
                print("Number must be 1-6!!")
        except ValueError:
            print("Not Valid Selection must be a number 1-6!")
            continue

def findstuff():
    while True : 
        # input employee ID
        id_ = input("Enter the employee ID: ")
        # regex pattern to confirm ID in specified format
        idPattern = re.search(r"^\d{5}$", id_)
        try : 
            if id_ and idPattern :                
                if id_ in dictionary : 
                    
                    # retrieve employee from dict
                    smartboyshit = dictionary[id_]
                    
                    # print employee record in formatted columns
                    print("-------" * 5 + "-")
                    print("%-10s %14s" % ("\nEmployee First Name: ", smartboyshit.First))
                    print("%-10s %15s" % ("Employee Last Name: ", smartboyshit.Last))
                    print("%-10s %22s" % ("Employee ID: ", smartboyshit.id))
                    print("%-10s %14s" % ("Employee Department: ", smartboyshit.Department))
                    print("%-10s %15s" % ("Employee Job Title: ", smartboyshit.JobT), "\n")
                    print("-------" * 5 + "-")
                    input("\nPress any key to continue")
                    time.sleep(.75)
                    clear()
                    break
                # if employee not found in dict
                else :
                    clear()
                    print("Employee not in database")
                    print("********************")
                    time.sleep(1)
                    break
            # if ID entered is not in specified format
            elif idPattern == None :
                raise ValueError
        except ValueError :
            clear()
            print("Invalid ID entry. Enter ID format 12345\n")
            continue
    
def delpeeps():
    while True : 
        # input employee ID
        id_ = input("Enter the employee ID: ")
        # regex pattern to confirm ID in specified format
        idPattern = re.search(r"^\d{5}$", id_)
        try : 
            if id_ and idPattern :                
                if id_ in dictionary : 
                    bobby1 = input("Are you Sure you want to delete this? Yes or No?")
                    bobby = dictionary[id_]
                    if bobby1 == "Yes":
                        del dictionary[id_]
                        print("Employee Deleted")
                        time.sleep(.75)
                        clear()
                        break
                    else:
                        print("Not Deleting")
                        time.sleep(.75)
                        clear()
                        break
                # if employee not found in dict
                else :
                    clear()
                    print("Employee not in database")
                    print("********************")
                    time.sleep(1)
                    break                    
            elif idPattern == None :
                raise ValueError
        except ValueError :
            clear()
            print("Invalid ID entry. Enter ID format 12345\n")
            continue
                        
def getstuff():
    obj = Employee()
    while True:
        try:
            first = input("What is your First Name:")
            obj.First = first
            if obj.FIRST == False:
                raise ValueError
            else:
                break           
        except ValueError:
            clear()
            print("Invalid Input(Must Be Alphabetical)")
            time.sleep(0.5)
            continue
        
    while True:
        try:
            last = input("What is your Last Name:")
            obj.Last = last
            
            if obj.LAST == False:
                raise ValueError    
            else:
                break            
        except ValueError:
            clear()
            print("Invalid Input(Must Be Alphabetical)")
            time.sleep(0.5)
            continue
        
    while True:
        try:
            id_ = input("What is your ID#:")
            obj.id = id_
            if obj.ID == False:
                raise ValueError
            else:
                break             
        except ValueError:
            clear()
            print("Invalid Input(Must Be Only 5 Digits)")
            time.sleep(0.5)
            continue
        
    while True:
        try:
            department = input("What is your Department:")
            obj.Department = department
            if obj.DEPARTMENT == False:
                raise ValueError
            else:
                break 
        except ValueError:
            clear()
            print("Invalid Input(Must Be Alphabetical)")
            time.sleep(0.5)
            continue
        
    while True:
        try:
            jobt = input("What is your Job Title:")
            obj.JobT = jobt
            if obj.JOBT == False:
                raise ValueError
            else:
                break 
        except ValueError:
            clear()
            print("Invalid Input(Must Be Alphabetical)")
            time.sleep(0.5)
            continue

   # add object to dictionary
    dictionary[id_] = obj
    print("\nEmployee record created")
    print("********************")
    time.sleep(1)
    clear()
    
def breaktime():
    while True:
        try:
            database = "employee_database.txt"
            database = open(database, 'wb')
            pickle.dump(dictionary, database)
            database.close()
  
        except:
            print("Something went wrong")
        finalchance = input("Are you Sure? (Yes or No)").lower()
        try:
            if finalchance == "yes":
                quit()
            elif finalchance == "no":
                menu()
                # print("menu works")
                break
            else:
                raise ValueError
        except ValueError:
            continue

def showeverything():
    print("-------" * 15 + "-")
    print("%-10s %20s %22s %17s %24s" % ("ID Number", "Firstname", "Lastname", "Department", "Job Title\n"))
    for key in sorted(dictionary) : 
        print("%-10s %20s %22s %17s %24s" % (str(dictionary[key].ID), str(dictionary[key].FIRST), str(dictionary[key].LAST), str(dictionary[key].DEPARTMENT), str(dictionary[key].JOBT)))
    print("-------" * 15 + "-")
    while True:
        try:
            input("\nEnter Key To Contiune")
            time.sleep(.75)
            clear()
            break
        except Exception:
            False
       
def cleardict():
    input("Press something to clear")
    global dictionary
    dictionary = None
    dictionary = {}

def changeaspects():
    while True : 
        # input employee ID
        id_ = input("Enter the employee ID: ")
        # regex pattern to confirm ID in specified format
        idPattern = re.search(r"^\d{5}$", id_)
        try : 
            if id_ and idPattern :                
                if id_ in dictionary : 
                    
                    # retrieve employee from dict
                    koolkid = dictionary[id_]
                    wtm = input("Would you like to change Firstname (Type First), Lastname(Type Last), ID(Type id), Department(Type Department), or Job Title(Type JobT)?").lower()
                    
                    if wtm == "first":
                        try:
                            first = input("What should firstname be change to?:")
                            koolkid.First = first
                            if koolkid.FIRST == False:
                                raise ValueError
                            else:
                                print("Change Made!")
                                time.sleep(1)
                                clear()
                                break           
                        except ValueError:
                            clear()
                            print("Invalid Input(Must Be Alphabetical)")
                            time.sleep(0.5)
                            continue  
                        
                    elif wtm == "last":
                        try:
                            last = input("What should lastname be changed to?:")
                            koolkid.Last = last
                            if koolkid.LAST == False:
                                raise ValueError    
                            else:
                                print("Change Made!")
                                time.sleep(1)
                                clear()                                
                                break            
                        except ValueError:
                            clear()
                            print("Invalid Input(Must Be Alphabetical)")
                            time.sleep(0.5)                            
                            continue 
                    
                    elif wtm == "id":                        
                        try:
                            id_ = input("What whould the ID number be?:")
                            koolkid.id = id_
                            if koolkid.ID == False:
                                raise ValueError
                            else:
                                print("Change Made!")
                                time.sleep(1)
                                clear()                                
                                break             
                        except ValueError:
                            clear()
                            print("Invalid Input(Must Be 5 Digits)")
                            time.sleep(0.5)
                            continue 
                    
                    elif wtm == 'department':
                        try:
                            department = input("What should department be?:")
                            koolkid.Department = department
                            if koolkid.DEPARTMENT == False:
                                raise ValueError
                            else:
                                print("Change Made!")
                                time.sleep(1)
                                clear()                                
                                break 
                        except ValueError:
                            clear()
                            print("Invalid Input(Must Be Alphabetical)")
                            time.sleep(0.5)
                            continue
                    
                    elif wtm == "jobt":
                        try:
                            jobt = input("What should the job title be?:")
                            koolkid.JobT = jobt
                            if koolkid.JOBT == False:
                                raise ValueError
                            else:
                                print("Change Made!")
                                time.sleep(1)
                                clear()                                
                                break 
                        except ValueError:
                            clear()
                            print("Invalid Input(Must Be Alphabetical)")
                            time.sleep(0.5)
                            continue
                    else:
                        print("Your Input Must Be Either First, Last, id, Department, or JobT!!")
                        clear()     
                                 
                    break
                # if employee not found in dict
                else :
                    clear()
                    print("Employee not in database")
                    print("********************")
                    time.sleep(1)
                    break
            # if ID entered is not in specified format
            elif idPattern == None :
                raise ValueError
        except ValueError :
            clear()
            print("Invalid ID entry. Enter ID format 12345\n")
            continue    

if __name__ == '__main__':
    menu()
    
    
    





# siddhu = Employee()
# siddhu.First = "Siddhu"
# siddhu.Last = "Tedla"
# siddhu.id = "53453"
# siddhu.Department = "Acc3Noounting"
# siddhu.JobT = "CFO3"
# print(siddhu.ID)
# print(siddhu.Last)
# print(siddhu.First)
# print(siddhu.Department)
# print(siddhu.JobT)
