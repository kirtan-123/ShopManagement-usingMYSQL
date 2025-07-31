import mysql.connector as m
from tabulate import tabulate

def admin():
    print("----------------------***----------------------------")  
    a = input("Enter password to access admin menu: ")
    if a == "ABC123":
        adminmenu()
    else:
        print("Wrong password")
        home()

def adminmenu():
    while True:
        print("----------------------***----------------------------")
        print("1. View all items")
        print("2. Search item")
        print("3. Insert cycle details")
        print("4. Update cycle details")
        print("5. Delete cycle details")
        print("6. Insert Customer details")
        print("7. Update Customer details")
        print("8. Delete Customer details")
        print("9. View Customer details")
        print("10. Sort By Price")
        print("11. Sort By Profit_m")
        print("12. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            disp1()
        elif choice == 2:
            search1()
        elif choice == 3:
            insert()
        elif choice == 4:
            update()
        elif choice == 5:
            delete()
        elif choice == 6:
            insertc()
        elif choice == 7:
            updatec()
        elif choice == 8:
            deletec()
        elif choice == 9:
            dispc()
        elif choice == 10:
            sortp()
        elif choice == 11:
            sortpm()
        elif choice == 12:
            print("Thank you")
            home()
        else:
            print("Try again with a valid choice")

def disp1():
    con = m.connect(host="localhost", user="root", password="root", database="root")
    print("Connection Established successfully!!")
    cur = con.cursor()
    query = "select c.cycle_id,c.price,c.brand,c.model,c.type,i.quantity,i.profit_m from cycle c,inventory i where i.cycle_id=c.cycle_id ;"
    cur.execute(query)
    rs = cur.fetchall()
    if not rs:
        print("No Records Found!!")
    else:
        headers = ["ID", "PRICE", "BRAND", "MODEL", "TYPE", "QUANTITY", "PROFIT_MARGIN"]
        print(tabulate(rs, headers=headers, tablefmt="grid"))
    print("\n")
    con.close()
    adminmenu()

def search1():
    con = m.connect(host="localhost", user="root", password="root", database="root")
    cur = con.cursor()
    sid = int(input("Enter the cycle ID to search: "))
    query = f"SELECT c.cycle_id,c.price,c.brand,c.model,c.type,i.quantity,i.profit_m from cycle c,inventory i where i.cycle_id=c.cycle_id and c.cycle_id={sid};"
    cur.execute(query)
    rs = cur.fetchone()
    if rs is None:
        print("No such Record found!!")
    else:
        headers = ["ID", "PRICE", "BRAND", "MODEL", "TYPE", "QUANTITY", "PROFIT_MARGIN"]
        print("Details are as follows:")
        print(tabulate([rs], headers=headers, tablefmt="grid"))
        print("\n")
    con.close()
    adminmenu()

def update():
    con = m.connect(host="localhost", user="root", password="root", database="root")
    cur = con.cursor()
    a = int(input("Enter cycle ID of the cycle whose data has to be updated: "))
    searchq = f"SELECT c.cycle_id,c.price,c.brand,c.model,c.type,i.quantity,i.profit_m from cycle c,inventory i where i.cycle_id=c.cycle_id and c.cycle_id={a};;"
    cur.execute(searchq)
    rs = cur.fetchone()
    if rs is None:
        print("No such cycle in the table!!")
    else:
        headers = ["ID", "PRICE", "BRAND", "MODEL", "TYPE", "QUANTITY", "PROFIT_MARGIN"]
        print("Cycle Details are as follows:")
        print(tabulate([rs], headers=headers, tablefmt="grid"))
        print("\n")
        print("------------------------------")
        print("1. Update brand")
        print("2. Update model")
        print("3. Update type")
        print("4. Update price")
        print("5. Update quantity")
        print("6. Update profit margin")
        print("------------------------------")
        ch = int(input("Enter your choice (1-6): "))
        if ch == 1:
            brand = input("Enter the correct brand: ")
            query = f"UPDATE cycle SET brand='{brand}' WHERE cycle_id={a};"
        elif ch == 2:
            model = input("Enter the correct model: ")
            query = f"UPDATE cycle SET model='{model}' WHERE cycle_id={a};"
        elif ch == 3:
            ctype = input("Enter the correct type: ")
            query = f"UPDATE cycle SET type='{ctype}' WHERE cycle_id={a};"
        elif ch == 4:
            price = input("Enter the correct price: ")
            query = f"UPDATE cycle SET price={price} WHERE cycle_id={a};"
        elif ch == 5:
            qt = input("Enter the correct quantity: ")
            query = f"UPDATE inventory SET quantity={qt} WHERE cycle_id={a};"
        elif ch == 6:
            profit = input("Enter the correct pofit margin: ")
            query = f"UPDATE inventory SET profit_m={profit} WHERE cycle_id={a};"
        cur.execute(query)
        con.commit()
        print("Updation successful!")
    con.close()
    adminmenu()

def delete():
    con = m.connect(host="localhost", user="root", password="root", database="root")
    cur = con.cursor()
    b = int(input("Enter the cycle ID of the cycle whose data to be deleted: "))
    searchq = f"SELECT * FROM cycle WHERE cycle_id={b};"
    cur.execute(searchq)
    rs = cur.fetchone()
    if rs is None:
        print("No such cycle ID in the table!!")
    else:
        fquery = f"DELETE FROM inventory WHERE cycle_id={b};"
        cur.execute(fquery)
        con.commit()
        dquery = f"DELETE FROM cycle WHERE cycle_id={b};"
        cur.execute(dquery)
        con.commit()
        print("Deletion successful!")
    con.close()
    adminmenu()

def insert():
    con = m.connect(host="localhost", user="root", password="root", database="root")
    cur = con.cursor()
    c = int(input("Enter the cycle ID of the cycle whose data to be inserted: "))
    searchq = f"SELECT * FROM cycle WHERE cycle_id={c};"
    cur.execute(searchq)
    rs = cur.fetchone()
    if rs is not None:
        print("Cycle ID already exists in the table!!")
    else:
        print("Enter the following info to be inserted into the List Table:")
        brand = input("Enter brand: ")
        model = input("Enter model: ")
        ctype = input("Enter type: ")
        price = input("Enter price: ")
        quantity = input("Enter Quantity:")
        profit_m = input("Enter Profit Margin:")
        query = f"INSERT INTO cycle VALUES ({c}, {price}, '{brand}', '{model}', '{ctype}');"
        fquery = f"INSERT INTO inventory VALUES ({c}, {quantity}, {profit_m});"
        cur.execute(query)
        con.commit()
        cur.execute(fquery)
        con.commit()
        print("Cycle record inserted successfully!")
    con.close()
    adminmenu()

def dispc():
    con = m.connect(host="localhost", user="root", password="root", database="root")
    print("Connection Established successfully!!")
    cur = con.cursor()
    query = "select cs.cust_id,c.cycle_id,c.brand,c.model,c.price,cs.name,cs.city,cs.phone from cycle c,customer cs where cs.cycle_id=c.cycle_id ;"
    cur.execute(query)
    rs = cur.fetchall()
    if not rs:
        print("No Records Found!!")
    else:
        headers = ["CUST_ID", "CY_ID", "BRAND", "MODEL", "PRICE", "NAME", "CITY", "PHONE"]
        print(tabulate(rs, headers=headers, tablefmt="grid"))
    print("\n")
    con.close()
    adminmenu()

def insertc():
    con = m.connect(host="localhost", user="root", password="root", database="root")
    cur = con.cursor()
    c = int(input("Enter the Customer ID of the Customer whose data to be inserted: "))
    searchq = f"SELECT * FROM customer WHERE cust_id={c};"
    cur.execute(searchq)
    rs = cur.fetchone()
    if rs is not None:
        print("Customer ID already exists in the table!!")
    else:
        print("Enter the following info to be inserted into the List Table:")
        cyid = input("Enter Cycle_id: ")
        name = input("Enter name: ")
        city = input("Enter city: ")
        phone = input("Enter phone: ")
        query = f"INSERT INTO customer VALUES ({c}, {cyid}, '{name}', '{city}', {phone});"
        cur.execute(query)
        con.commit()
        print("Customer record inserted successfully!")
    con.close()
    adminmenu()



def updatec():
    con = m.connect(host="localhost", user="root", password="root", database="root")
    cur = con.cursor()
    a = int(input("Enter Customer ID of the Customer whose data has to be updated: "))
    searchq = f"SELECT * FROM customer WHERE cust_id={a};"
    cur.execute(searchq)
    rs = cur.fetchone()
    if rs is None:
        print("No such Customer in the table!!")
    else:
        headers = ["CUST_ID", "NAME", "CITY", "PHONE", "CYCLE_ID"]
        print("Customer Details are as follows:")
        print(tabulate([rs], headers=headers, tablefmt="grid"))
        print("\n")
        print("------------------------------")
        print("1. Update CY_ID")
        print("2. Update NAME")
        print("3. Update CITY")
        print("4. Update PHONE")
        print("------------------------------")
        ch = int(input("Enter your choice (1-4): "))
        if ch == 1:
            f = input("Enter the correct CY_ID: ")
            query = f"UPDATE customer SET cycle_id={f} WHERE cust_id={a};"
        elif ch == 2:
            f = input("Enter the correct NAME: ")
            query = f"UPDATE customer SET name='{f}' WHERE cust_id={a};"
        elif ch == 3:
            f = input("Enter the correct CITY: ")
            query = f"UPDATE customer SET city='{f}' WHERE cust_id={a};"
        elif ch == 4:
            f = input("Enter the correct PHONE: ")
            query = f"UPDATE customer SET phone={f} WHERE cust_id={a};"
        cur.execute(query)
        con.commit()
        print("Updation successful!")
    con.close()
    adminmenu()


def deletec():
    con = m.connect(host="localhost", user="root", password="root", database="root")
    cur = con.cursor()
    b = int(input("Enter the Customer ID of the Customer whose data to be deleted: "))
    searchq = f"SELECT * FROM customer WHERE cust_id={b};"
    cur.execute(searchq)
    rs = cur.fetchone()
    if rs is None:
        print("No such Customer ID in the table!!")
    else:
        dquery = f"DELETE FROM customer WHERE cust_id={b};"
        cur.execute(dquery)
        con.commit()
        print("Deletion successful!")
    con.close()
    adminmenu()


def sortp():
    con = m.connect(host="localhost", user="root", password="root", database="root")
    cur = con.cursor()
    query = "select c.cycle_id,c.price,c.brand,c.model,c.type,i.quantity,i.profit_m from cycle c,inventory i where i.cycle_id=c.cycle_id order by c.price;"
    cur.execute(query)
    rs = cur.fetchall()
    if not rs:
        print("No Records Found!!")
    else:
        headers = ["ID", "PRICE", "BRAND", "MODEL", "TYPE", "QUANTITY", "PROFIT_MARGIN"]
        print(tabulate(rs, headers=headers, tablefmt="grid"))
    print("\n")
    con.close()
    adminmenu()

def sortpm():
    con = m.connect(host="localhost", user="root", password="root", database="root")
    cur = con.cursor()
    query = "select c.cycle_id,c.price,c.brand,c.model,c.type,i.quantity,i.profit_m from cycle c,inventory i where i.cycle_id=c.cycle_id order by i.profit_m"
    cur.execute(query)
    rs = cur.fetchall()
    if not rs:
        print("No Records Found!!")
    else:
        headers = ["ID", "PRICE", "BRAND", "MODEL", "TYPE", "QUANTITY", "PROFIT_MARGIN"]
        print(tabulate(rs, headers=headers, tablefmt="grid"))
    print("\n")
    con.close()
    adminmenu()
    
    
def customer():
    while True:
        print("----------------------***----------------------------")
        print("1. View all items")
        print("2. Search item by brand")
        print("3. Search item by model")
        print("4. Search item by type")
        print("5. Sort items by price")
        print("6. View item by budget")
        print("7. Exit Customer Menu")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            disp2()
        elif choice == 2:
            search2()
        elif choice == 3:
            search3()
        elif choice == 4:
            search4()
        elif choice == 5:
            sort_by_price()
        elif choice == 6:
            search_by_price()
        elif choice == 7:
            print("Thank you")
            home()
            
        else:
            print("Try again with a valid choice")

def disp2():
    con = m.connect(host="localhost", user="root", password="root", database="root")
    cur = con.cursor()
    query = "SELECT * FROM cycle;"
    cur.execute(query)
    rs = cur.fetchall()
    if not rs:
        print("No Records Found!!")
    else:
        print("Details are as follows:")
        headers = ["ID", "PRICE", "BRAND", "MODEL", "TYPE"]
        print(tabulate(rs, headers=headers, tablefmt="grid"))
    print("\n")
    con.close()
    customer()

def search2():
    con = m.connect(host="localhost", user="root", password="root", database="root")
    cur = con.cursor()
    brand = input("Enter the cycle brand to search: ")
    query = f"SELECT * FROM cycle WHERE brand='{brand}';"
    cur.execute(query)
    rs = cur.fetchall()
    if not rs:
        print("No such Record found!!")
    else:
        print("Details are as follows:")
        headers = ["ID", "PRICE", "BRAND", "MODEL", "TYPE"]
        print(tabulate(rs, headers=headers, tablefmt="grid"))
    print("\n")
    con.close()
    customer()

def search3():
    con = m.connect(host="localhost", user="root", password="root", database="root")
    cur = con.cursor()
    model = input("Enter the cycle model to search: ")
    query = f"SELECT * FROM cycle WHERE model='{model}';"
    cur.execute(query)
    rs = cur.fetchall()
    if not rs:
        print("No such Record found!!")
    else:
        print("Details are as follows:")
        headers = ["ID", "PRICE", "BRAND", "MODEL", "TYPE"]
        print(tabulate(rs, headers=headers, tablefmt="grid"))
    print("\n")
    con.close()
    customer()

def search4():
    con = m.connect(host="localhost", user="root", password="root", database="root")
    cur = con.cursor()
    ctype = input("Enter the cycle type to search: ")
    query = f"SELECT * FROM cycle WHERE type='{ctype}';"
    cur.execute(query)
    rs = cur.fetchall()
    if not rs:
        print("No such Record found!!")
    else:
        print("Details are as follows:")
        headers = ["ID", "PRICE", "BRAND", "MODEL", "TYPE"]
        print(tabulate(rs, headers=headers, tablefmt="grid"))
    print("\n")
    con.close()
    customer()

def sort_by_price():
    con = m.connect(host="localhost", user="root", password="root", database="root")
    cur = con.cursor()
    query = "SELECT * FROM cycle ORDER BY price;"
    cur.execute(query)
    rs = cur.fetchall()
    if not rs:
        print("No Records Found!!")
    else:
        headers = ["ID", "PRICE", "BRAND", "MODEL", "TYPE"]
        print(tabulate(rs, headers=headers, tablefmt="grid"))
    print("\n")
    con.close()
    customer()

def search_by_price():
    con = m.connect(host="localhost", user="root", password="root", database="root")
    cur = con.cursor()
    max_price = input("Enter your max budget: ")
    query = f"SELECT * FROM cycle WHERE price < '{max_price}' order by price;"
    cur.execute(query)
    rs = cur.fetchall()
    if not rs:
        print(f"No cycles found with price below {max_price}.")
    else:
        headers = ["ID", "PRICE", "BRAND", "MODEL", "TYPE"]
        print(tabulate(rs, headers=headers, tablefmt="grid"))
    print("\n")
    con.close()
    customer()

def home():
    while True:
        print("----------------------***----------------------------")
        print("Welcome to Cycle Management System")
        print("Enter your choice")
        print("----------------------***----------------------------")
        print("1. Login to admin menu")
        print("2. Buy cycle")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            admin()
        elif choice == 2:
            customer()
        elif choice == 3:
            print("Thank you")
            exit()
        else:
            print("Try again with a valid choice")

home()
