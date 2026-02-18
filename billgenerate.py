import pyodbc


conn=pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-I7V7GR2\SQLEXPRESS;"
    "Database=CAFE;"
    "Trusted_Connection=yes;"

)
cursor = conn.cursor()

cursor.execute("SELECT * FROM dbo.MENU")
records = cursor.fetchall()

for row in records:
    print(row)

def generate_bill():
    table_no = int(input("Enter table number for bill: "))

    cursor.execute("""
        SELECT  table_no,food_item, qty, price, total
        FROM ORDERS
        WHERE table_no=?
    """, table_no)

    rows = cursor.fetchall()

    print("\n======= HOTEL BILL =======")
    print("Table No:", table_no)
    print("---------------------------")
    print("Food\tQty\tPrice\tTotal")

    grand_total = 0

    for r in rows:
        print(f"{r.food_item}\t{r.qty}\t{r.price}\t{r.total}")
        grand_total += r.total

    print("---------------------------")
    print("Grand Total =", grand_total)




tableNo=int(input("enter table number : "))
while True:
    food_item=input("enter food menu or done")
    food_item=food_item.lower()
    if food_item=="done":
        break
         
    qty=int(input("enter quantity"))
     
    cursor.execute("SELECT Price FROM dbo.MENU  WHERE menu=?",food_item)
    price1=cursor.fetchall()
    
    price=price1[0][0]
    total=price*qty
    print(total)

    cursor.execute("INSERT INTO ORDERS(table_no,food_item,qty,price,total) VALUES (?,?,?,?,?)",tableNo,food_item,qty,price,total)
    conn.commit()
generate_bill()









    

         
         
         



