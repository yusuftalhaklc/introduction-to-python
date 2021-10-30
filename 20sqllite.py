import sqlite3

def selectoperations():
    conn = sqlite3.connect("chinook.db")
    # cursor = conn.execute("""
    #                     SELECT FirstName,Lastname 
    #                     FROM customers 
    #                     WHERE city ='Prague' or city ='Berlin'
    #                     ORDER BY Firstname,LastName DESC        # DESC AND ASC
    #                      """)
    # for row in cursor:
    #     print(f"First Name : {row[0]}")
    #     print(f"Last Name : {row[1]}")

    # cursor = conn.execute("""
    #                     SELECT city,count(*) FROM Customers
    #                     GROUP BY city 
    #                     HAVING count(*)>1
    #                     ORDER BY count(*) DESC
    #                     """)

    # for row in cursor:
    #     print(f"City : {row[0]}")
    #     print(f"Count : {row[1]}")

    cursor = conn.execute("""
                            SELECT FirstName,Lastname 
                            FROM customers 
                            WHERE FirstName like 'a%'
                            """)
                            #'%a%' or 'a%' or '%a'
    for row in cursor:
        print(f"First Name : {row[0]}")
        print(f"Last Name : {row[1]}")

    conn.close()

def insertCustomer():
    conn = sqlite3.connect("chinook.db")
    conn.execute("""
                    INSERT INTO customers (FirstName,LastName,city,Email)
                    VALUES
                    ("Yusuf","KILIÇ","İstanbul","yusuftalhaklc@gmail.com")
    
                """)
    conn.close()

def updateCustomer():
    conn = sqlite3.connect("chinook.db")

    conn.execute("""
                UPDATE customers SET city = 'Ankara'
                WHERE city = 'İstanbul'
                """)
    conn.commit()
    conn.close()

def deleteCustomer():
    conn = sqlite3.connect("chinook.db")
    conn.execute("""
                    DELETE FROM customers 
                    WHERE FirstName ='Yusuf'
                """)
    conn.commit()
    conn.close()

def innerjoinoperations():
    conn = sqlite3.connect("chinook.db")
    cursor = conn.execute("""
                            SELECT albums.Title,artists.Name 
                            FROM artists 
                            INNER JOIN albums
                            ON artists.ArtistId = albums.ArtistId
                            """)
    for row in cursor:
        print(f"Title : {row[0]} \nName : {row[1]}")
        print("************")
    conn.close()
innerjoinoperations()