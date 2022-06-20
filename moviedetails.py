import mainmenu2
import director_details
import budget
import mysql.connector as co
def MOVIEDETAILS_MENU():
    while True:
        #MODULE : moviedetails
        print("""-----------------------------------------------------
        Welcome to Movie Details Menu
        -----------------------------------------------------
        Here are the details about top movies from all around the world. What do you want today? 
        Select the desired number""")
        print(" 1 : to enter movie details")
        print(" 2 : show movie details")
        print(" 3 : search")
        print(" 4 : delete a record")
        print(" 5 : update movie details")
        print(" 6 : return")
        print("-----------------------------------------------------")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            movi_details()
        elif choice==2:
            show_movi_details()
        elif choice==3:
            search_movi_details()
        elif choice==4:
            delete_movi_details()
        elif choice==5:
            edit_movi_details()
        elif choice==6:
            return
        else:
            print("Error : Please enter a number from 1 to 6")
            conti="Press any key to return to the main menu"
def movi_details():
    try:
        mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
        cursor =mycon.cursor()
        sno=int(input("Enter S.No. "))
        name= input("Enter Name ")
        stars=int(input("Enter number of stars the movie has "))
        directorname = input("Enter director's name ")
        typo = input("Enter type of movie ")
        originallanguage = input("Enter original language")
        profitpercent = int(input("Enter profit percantage of the movie"))
        query="insert into moviedetails(sno,name,stars,directorname,typo,originallanguage,profitpercent)values('{}','{}','{}','{}','{}','{}','{}')".format(sno,name,stars,directorname,typo,originallanguage,profitpercent)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print("""Record has been saved in the table
        Thank you for sharing your knowledge""")
    except:
            print("error")

def show_movi_details():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    cursor.execute("select *from moviedetails")
    data=cursor.fetchall()
    for row in data:
         print(row)

def search_movi_details():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter Movie Name : ")
    st="select *from movie details where name='%s"%(ac)
    cursor.execute(st)
    data=cursor.fetchall()
    print(data)

def delete_movi_details():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter Movie Name : ")
    st="delete *from movie details where name='%s"%(ac)
    cursor.execute(st) 
    mycon.commit()
    print("Data deleted successfully")

def edit_movi_details():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    print("1.Edit Name")
    print("2. Edit Stars")
    print("3. Edit Director Name")
    print("4. Edit type")
    print("5. Edit original language")
    print("6. Edit profit percent")
    print("7. return")
    print("-----------------------------")
    choice=int(input("enter your choice"))
    if choice==1:
        edit_name()
    elif choice==2:
        edit_stars()
    elif choice==3:
        edit_directorname()
    elif choice==4:
        edit_typo()
    elif choice==5:
        edit_originallanguage()
    elif choice==6:
        edit_profitpercent()
    elif choice==7:
        return
    else:
        print("Error : Invalid choice, try again...")
        conti="press any key to continue"

def edit_name():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter Movie Name : ")
    nm= input("enter correct name")
    st="update moviedetails set name='%s' where sno='%s'"%(nm,ac)
    cursor.execute(st) 
    mycon.commit()
    print("data successfully updated")

def edit_stars():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter Movie Name : ")
    nm = int(input("enter correct number of stars "))
    st="update moviedetails set stars='%s' where name='%s'"%(nm,ac)
    cursor.execute(st) 
    mycon.commit()
    print("data successfully updated")

def edit_directorname():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter Movie Name : ")
    nm = input("enter correct director name")
    st="update moviedetails set directorname='%s' where name='%s'"%(nm,ac)
    cursor.execute(st) 
    mycon.commit()
    print("data successfully updated")

def edit_typo():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter Movie Name : ")
    nm = input("enter correct type")
    st="update moviedetails set type='%s' where name='%s'"%(nm,ac)
    cursor.execute(st) 
    mycon.commit()
    print("data successfully updated")

def edit_originallanguage():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter Movie Name : ")
    nm = input("enter correct language")
    st="update moviedetails set originallanguage='%s' where name='%s'"%(nm,ac)
    cursor.execute(st) 
    mycon.commit()
    print("data successfully updated")

def edit_profitpercent():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter Movie Name : ")
    nm = input("enter correct profit percentage")
    st="update moviedetails set profitpercent='%s' where name='%s'"%(nm,ac)
    cursor.execute(st) 
    mycon.commit()
    print("data successfully updated")