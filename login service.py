class Loginservice:
 import sqlite3

def login():
    while True:
        username = input("please enter your username: ")
        password = input("please enter your password: ")
        with sqlite3.connect("names.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM USER WHERE username = ? AND password = ?")
        cursor.execute(find_user,[(username),(password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("Welcome to Laundromat Services!!!!,"
                       + i[2] + i[3])
            #retrun("exit")
            break

        else:
            print("Username and Password not recognized")
            again = input("Do you want to try again?(y/n):")
            if again.lower() == "n":
                print("goodbye")
                time.sleep(1)
                #retuen("exit")

                break

login()

    
