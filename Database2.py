cursor.execute('''CREATE TABLE LAUNDROMART SERVICES
         (ID INT PRIMARY KEY     NOT NULL,
         FIRST NAME           TEXT    NOT NULL,
         LAST NAME           TEXT     NOT NULL,
         EMAIL ADDRESS       CHAR(50),
         POINTS          INT);''')
cursor.close()
