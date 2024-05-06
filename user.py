# user panel options
import mongo

def product_catalog():
    print("here is the following product catalog")
    product_list = mongo.query_products()
    for item in product_list:
        print(f'''
----PRODUCT---
name: {item["name"]}
description: {item["description"]}
price: {item["price"]}
category: {item["category"]}
----PRODUCT---''')

def track_orders(username):
    print("your current orders")
    orders = mongo.query_orders(username)
    for order_id in orders:
        order = mongo.query_primary_key(order_id, "Order")
        print(f'''
------ORDERS------
order id: {order_id}
total price: {order["total_price"]}
date: {order["date"]}
------ORDERS------
        ''')

    user_input = input("Would you like to delete your most recent order? (1) Yes, (2) No: ")
    if(user_input == "1"):
        order_found = mongo.remove_data_using_primary_key(username, orders[-1], "orders", "User")
        if(order_found):
            print("order cancelled")

def view_account_details(username):
    user_input = None
    while(user_input != "2"):
        print("The information for your account is as listed as below.")
        user_details = mongo.query_user(username)
        print(f'''
---USER DETAIS---
name: {user_details["name"]}
email: {user_details["email"]}
password: {user_details["password"]}
address: {user_details["address"]}
---USER DETAILS---
        ''')

        user_input = input('''
Would you like to update any information
(1) Yes
(2) No 
: ''')
        if(user_input == "1"):
            update_input = input('''
select the information you would like to update
(1) name
(2) email
(3) password
(4) address
: ''')
            old_username = username 
            new_data = input("enter the new data: ")
            field_selection = None
            if(update_input == "1"):
                field_selection = "name"
                username = new_data
            elif(update_input == "2"):
                field_selection = "email"
            elif(update_input == "3"):
                field_selection = "password"
            elif(update_input == "4"):
                field_selection = "address"

            update_state = mongo.update_data(old_username,field_selection,new_data, "User")
            if(update_state):
                print("Your data has been change")
            return username 

def user_panel(username):
    print("Welcome:", username, "this is your user panel")
    user_input = None
    while(user_input != "4"):
        user_input = input('''
--------------USER PANEL----------------
(1) View Product Catalog 
(2) Manage Orders
(3) View Account Details
(4) Exit 
--------------USER PANEL----------------
: ''')
        if(user_input == "4"):
            print("Goodbye")
            return
        if(user_input == "1"):
            product_catalog()
        elif(user_input == "2"):
            track_orders(username)
        elif(user_input == "3"):
            username = view_account_details(username)

