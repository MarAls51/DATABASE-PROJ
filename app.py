# main file
import admin
import mongo
import user

def login(username, password, user_type):
    return mongo.query_user(username, password, user_type)

def main():
    mongo.open_db()
    user_type = None
    valid_selection = False
    while(not (user_type == "admin" or user_type == "user")):
        user_type = input("Hello and welcome the shopping cart system, are you a user or an admin? ")

    print("welcome", user_type)
    is_logged_in = False
    username = None
    password = None
    while(is_logged_in == False):
        username = input("what is your username? ")
        password = input("what is your password ")
        login_state = login(username, password, user_type)
        if(not login_state):
            print("password or username is invalid")
        else:
            print("success welcome:", username, "you are currently logged as a:", user_type)
            is_logged_in = True
    
    if(user_type == "admin"):
        admin.admin_panel(username)
    else:
        user.user_panel(username)

    mongo.close_db()


if __name__ == "__main__":
    main()