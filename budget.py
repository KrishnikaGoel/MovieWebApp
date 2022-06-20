import mainmenu2
import budget
import director_details
import budget 
import mysql.connector as co
def EVE_MENU():
    while True:
        #MODULE : BUDGET
        print("""-----------------------------------------------------
        Welcome to budget main menu
        -----------------------------------------------------
        Here are the details about budget of blockbuster films from all around the world. What do you want today? 
        Select the desired number""")
        print(" 1 : to enter budget")
        print(" 2 : show budget")
        print(" 3 : search")
        print(" 4 : delete a record")
        print(" 5 : update budget")
        print(" 6 : return")
        print("-----------------------------------------------------")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            budget_details()
        elif choice==2:
            show_budget()
        elif choice==3:
            search_budget()
        elif choice==4:
            delete_budget()
        elif choice==5:
            edit_budget()
        elif choice==6:
            return
        else:
            print("Error : Please enter a number from 1 to 6")
            conti="Press any key to return to the main menu"

def budget_details():
    try:
        mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
        cursor=mycon.cursor()
        sno=int(input("enter sno"))
        fname=input("enter movie name")
        creativetalent=int(input("enter creative talent in budget"))
        directproductioncost=input("enter direct production cost of the directed movie in the budget")
        postproductioncost=input("enter the post production cost of the directed movie in the budget")
        other=input("enter any other cost of the directed movie in the budget")
        totalbudget=int(input("enter total budget"))
        totalprofit=input("enter total profit")
        earnings=input("enter earnings")
        query="insert into budget(sno,fname,creativetalent,directproductioncost,postproductioncost,other,totalbudget,totalprofit,earnings)values({},{},{},{},{},{},{},{},{})".format(sno,fname,creativetalent,directproductioncost,postproductioncost,other,totalbudget,totalprofit,earnings)
        cursor.execcute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print("""Record has been saved in the table
        Thank you for sharing your knowledge""")
    except:
            print('error')

def show_budget():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    cursor.execute("select *from budget")
    data=cursor.fetchall()
    for row in data:
        print(row)

def search_budget():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter fname : ")
    st="select *from budget where fname='%s"%(ac)
    cursor.execute(st)
    data=cursor.fetchall()
    print(data)

def delete_budget():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter fname ")
    st="delete *from budget where fname='%s"%(ac)
    cursor.execute(st) 
    mycon.commit()
    print("Data deleted successfully")

def edit_budget():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    print("1.Edit fname")
    print("2. Edit creativetalent")
    print("3. Edit directproductioncost")
    print("4. Edit postproductioncost")
    print("5. Edit other")
    print("6. Edit totalbudget")
    print("7. edit totalprofit")
    print("8. edit earnings")
    print("9. return")
    print("-----------------------------")
    choice=int(input("enter your choice"))
    if choice==1:
        budget.edit_fname()
    elif choice==2:
        budget.edit_creativetalent()
    elif choice==3:
        budget.edit_directcostproduction()
    elif choice==4:
        budget.edit_postcostproduction()
    elif choice==5:
        budget.edit_other()
    elif choice==6:
        budget.edit_totalbudget()
    elif choice==7:
        budget.edit_totalprofit()
    elif choice==8:
        budget.edit_earnings()
    elif choice==9:
        return
    else:
        print("Error : Invalid choice, try again...")
        conti="press any key to continue"

def edit_fname():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter sno")
    nm= input("enter correct fname")
    st="update budget set fname='%s' where sno='%s'"%(nm,ac)
    cursor.execute(st) 
    mycon.commit()
    print("data successfully updated")

def edit_creativetalent():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter fname")
    nm = int(input("enter correct amount of creativetalent "))
    st="update budget set creativetalent='%s' where fname='%s'"%(nm,ac)
    cursor.execute(st) 
    mycon.commit()
    print("data successfully updated")

def edit_directproductioncost():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter fname")
    nm = input("enter correct direct production cost")
    st="update budget set directproductioncost='%s' where fname='%s'"%(nm,ac)
    cursor.execute(st) 
    mycon.commit()
    print("data successfully updated")

def edit_postproductioncost():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter fname ")
    nm = input("enter correct postproductioncost")
    st="update budget set postproductioncost='%s' where fname='%s'"%(nm,ac)
    cursor.execute(st) 
    mycon.commit()
    print("data successfully updated")

def edit_other():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter fname")
    nm = input("enter correct amount of other costs")
    st="update budget set other='%s' where fname='%s'"%(nm,ac)
    cursor.execute(st) 
    mycon.commit()
    print("data successfully updated")

def edit_totalbudget():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter fname")
    nm = input("enter correct amount of total budget")
    st="update budget set totalbudget='%s' where fname='%s'"%(nm,ac)
    cursor.execute(st) 
    mycon.commit()
    print("data successfully updated")

def edit_totalprofit():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter fname")
    nm = input("enter correct amount of total profit")
    st="update budget set totalprofit='%s' where fname='%s'"%(nm,ac)
    cursor.execute(st) 
    mycon.commit()
    print("data successfully updated")

def edit_earnings():
    mycon=co.connect(user="root", password="mysql", host="localhost", database="projcet")
    cursor=mycon.cursor()
    ac=input("Enter fname")
    nm = input("enter correct amount of earnings")
    st="update budget set earnings='%s' where fname='%s'"%(nm,ac)
    cursor.execute(st) 
    mycon.commit()
    print("data successfully updated")