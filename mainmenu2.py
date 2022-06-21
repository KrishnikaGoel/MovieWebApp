#%%
import moviedetails
import director_details
import budget 

while True:
    #mainmenu2
    print("""-----------------------------------------------------
    Attention All Movie Lovers!!!
    -----------------------------------------------------
    Hello everyone. We present to you the highest grossing movies of all time! We hope our work would be beneficial for striving   producers so that they can watch and learn from the best, without struggling to find good movies as we are serving them a full platter""")
    print("This can also help the cinema fans who are bored out of their minds due to lockdown and are tired of searching for good movies")
    print("""Here's a list just for that.
    So giddy up if you are in search of movies to watch as this is just the right place for you""")
    print("HERE IT GOES.....ENJOY")
    print(" 1) Movie Details")
    print(" 2) Director Details")
    print(" 3) Budget Details")
    print(" 4) Exit")
    print("-----------------------------------------------------")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        moviedetails.MOVIEDETAILS_MENU()
    elif choice == 2:
        director_details.BOL_MENU()
    elif choice == 3:
        budget.EVE_MENU()
    elif choice == 4:
        break
    else:
        print("Error : Please select a number from 1 to 4")
        conti=input("Press any key to continue")
# %%
