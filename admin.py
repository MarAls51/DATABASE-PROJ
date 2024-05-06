#admin panel stuff
import mongo

def product_catalog():
    admin_input = None
    while (admin_input != "4"):
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

        admin_input = input("do you wish to modify the inventory? (1) remove a product, (2) add a product, (3) edit an existing product, (4) return: ")
        if(admin_input == "4"):
            return
        if(admin_input == "1" or admin_input == "3"):
            name_of_product_item = input("select the product name: ")
            if(admin_input == "1"):
                mongo.remove_item(name_of_product_item, "Product")
            else:
                update_input = input('''
select the information you would like to update
(1) name
(2) description
(3) price
(4) supplierID
(5) category
: ''')

                new_data = input("enter the new data: ")
                field_selection = None
                if(update_input == "1"):
                    field_selection = "name"
                elif(update_input == "2"):
                    field_selection = "description"
                elif(update_input == "3"):
                    field_selection = "price"
                    new_data = int(new_data)
                elif(update_input == "4"):
                    field_selection = "supplierID"
                elif(update_input == "5"):
                    field_selection = " category"
                update_state = mongo.update_data(name_of_product_item,field_selection,new_data, "Product")
                if(update_state):
                    print("Your data has been change")
        else:
            name = input("please enter a name: ")
            description = input("please enter a description: ")
            price = input("price: ")
            supplierID = input("supplierID: ")
            category = input("category: ")

            new_product = {
            "name": name,
            "description": description,
            "price": int(price),
            "supplierID": supplierID,
            "category": category
            }
            mongo.insert_item(new_product, "Product")

def manage_accounts(username):
    admin_input = None
    while(admin_input != "2"):
        print("accounts currently under your supervision")
        users = mongo.query_supervised_users(username)
        print(users)
        for user_id in users:
            user = mongo.query_primary_key(user_id, "User")
            print(user)
            print(f'''
------Users------
name: {user["name"]}
------Users------
''')
        admin_input = input("would you like to remove an account from the db?, (1) Yes, (2) No: ")
        if(admin_input == "2"):
            return
        else:
            user_to_remove = input("please state the name of the user you want to remove from supervision: ")
            result = mongo.query_user(user_to_remove)
            user_id = result["_id"]
            mongo.remove_data_using_primary_key(username,user_id, "users", "Admin")


def admin_panel(username):
    print("Welcome:", username, "this is your admin panel")

    admin_input = None
    while(admin_input != "3"):
        admin_input = input('''
--------------ADMIN PANEL----------------
(1) view product catalog
(2) manage user accounts
(3) Exit
--------------ADMIN PANEL----------------
''')

        if(admin_input == "3"):
            print("Goodbye")
            return
        if(admin_input == "1"):
            product_catalog()
        elif(admin_input == "2"):
            manage_accounts(username)
