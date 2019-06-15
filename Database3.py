import sqlite3
conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()
cursor.execute("INSERT INTO LAUNDROMART (ID,USERNAME,PASSWORD,FIRSTNAME,LASTNAME,EMAIL,POINTS) \
      VALUES (101, 'GOLD', 'GOLD', 'GOLD', 'WEJINYA', 'goldminefinz@gmail.com', 200)");
cursor.execute("INSERT INTO LAUNDROMART (ID,USERNAME,PASSWORD,FIRSTNAME,LASTNAME, EMAIL, POINTS) \
      VALUES (102, 'ABDUL', 'ABDUL, 'ABDUL', 'ABDUL', 'abdul@gmail.com', 150 )");
cursor.execute("INSERT INTO LAUNDROMART (ID,USERNAME,PASSWORD,FIRSTNAME,LASTNAME,EMAIL,POINTS) \
      VALUES (103, 'SUSAN', 'SUSAN', 'SUZAN', 'NTANYI', 'nkemforatte@gmail.com', 400 )");
cursor.execute("INSERT INTO LAUNDROMART (ID,USERNAME,PASSWORD,FIRSTNAME,LASTNAME,EMAIL,POINTS) \
      VALUES (104, 'SHADRACK', SHADRACK', 'SHADRACK', 'SHADRACK', 'shaderack@gmail.com', 650)");
conn.commit()
conn.close()
