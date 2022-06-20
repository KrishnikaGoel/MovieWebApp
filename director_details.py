import mainmenu2
import moviedetails
import budget
import mysql.connector as co
def BOL_MENU():
    while True:
        #MODULE : director_details
        print("""-----------------------------------------------------
        Welcome to Director Details Menu
        -----------------------------------------------------
        Here are the details about top directors from all around the world. What do you want today? 
        Select the desired number""")
        print(" 1 : to enter director details")
        print(" 2 : show director details")
        print(" 3 : search")
        print(" 4 : delete a record")
        print(" 5 : update director details")
        print(" 6 : return")
        print("-----------------------------------------------------")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            director_details()
        elif choice==2:
            show_director_details()
        elif choice==3:
            search_director_details()
        elif choice==4:
            delete_director_details()
        elif choice==5:
            edit_director_details()
        elif choice==6:
            return
        else:
            print("Error : Please enter a number from 1 to 6")
            conti="Press any key to return to the main menu"
def director_details():
    try:
        mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
        cursor=mycon.cursor()
        sno=int(input("enter sno "))
        dname=input("enter director name ")
        dob = int(input("enter dob of director"))
        famousmovies=input("enter name of famous movie directed by the director ")
        totalmovies=int(input("enter total no.of movies directed by the director"))
        awards= int(input("enter no. of awards won by the director"))
        nationality= int(input("enter nationality of director"))
        query="insert into director_details(sno,dname,dob,famousmovies,totalmovies,awards,nationality)values('{}','{}','{}','{}','{}','{}','{}')".format(sno,dname,dob,famousmovies,totalmovies,awards,nationality)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print("""Record has been saved in the table
        Thank you for sharing your knowledge""")
    except:
            print("error")

def show_director_details():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    cursor.execute("select *from director_details")
    data=cursor.fetchall()
    for row in data:
        print(row)
    
def search_director_details():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("enter director name")
    st="select *from director_details where dname='%s'"%(ac)
    cursor.execute(st)
    data=cursor.fetchall()
    print(data)

def delete_director_details():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("enter director name")
    st="delete from director_details where dname='%s'"%(ac)
    cursor.execute(st)
    mycon.commit()
    print("data deleted successfully")

def edit_director_details():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    print("1.Edit dname")
    print("2. Edit dob")
    print("3. Edit famousmovie")
    print("4. Edit totalmovies")
    print("5. Edit awards")
    print("6. Edit nationality")
    print("7. return")
    print("-----------------------------")
    choice=int(input("enter your choice"))
    if choice==1:
        edit_dname()
    elif choice==2:
        edit_dob()
    elif choice==3:
        edit_famousmovies()
    elif choice==4:
        edit_totalmovies()
    elif choice==5:
        edit_awards()
    elif choice==6:
        edit_nationality()
    elif choice==7:
        return
    else:
        print("Error : Invalid choice, try again...")
        conti="press any key to continue"

def edit_dname():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=int(input("emter sno"))
    nm=input("enter correct director name")
    st="upate director_details set dname='%s' where sno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('data successfully updated')

def edit_dob():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=int(input("emter dname"))
    nm=input("enter correct dob")
    st="upate set dob='%s' where dname='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('data successfully updated')

def edit_famousmovies():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=int(input("emter sno"))
    nm=input("enter correct director name")
    st="upate director_details set dname='%s' where sno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('data successfully updated')

def edit_totalmovies():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("emter dname")
    nm=input("enter correct total no. of movies")
    st="upate director_details set totalmovies='%s' where dname='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('data successfully updated')

def edit_awards():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("emter dname")
    nm=input("enter correct awards")
    st="upate director_details set awards='%s' where dname='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('data successfully updated')

def edit_nationality():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=int(input("emter dname"))
    nm=input("enter correct nationality")
    st="upate director_details set nationality='%s' where dname='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('data successfully updated')