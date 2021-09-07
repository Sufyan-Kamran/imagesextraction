import mysql.connector
from mysql.connector import Error
import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

try:
    connection = mysql.connector.connect(host='localhost',
                                             database='example',
                                             user='root',
                                            password='')

    cursor = connection.cursor()
    sql_fetch_blob_query = """SELECT * from imgs"""

    cursor.execute(sql_fetch_blob_query)
    record = cursor.fetchall()
    i = 1
    for row in record:
        i = i+1
        def readBLOB(photo):
            print("Reading BLOB data from python_employee table")

            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='example',
                                                    user='root',
                                                    password='')

                cursor = connection.cursor()
                sql_fetch_blob_query = """SELECT * from imgs"""

                cursor.execute(sql_fetch_blob_query)
                record = cursor.fetchall()
                for row in record:
                    print("Id = ", row[0] )
                    image = row[0]
                    print("Storing employee image and bio-data on disk \n")
                    write_file(image, photo)
                    
            except mysql.connector.Error as error:
                print("Failed to read BLOB data from MySQL table {}".format(error))
        for row in record:
            s=(f"s{i}"+".png")
            sa=("labe"+f"s{i}")
            saa = (f"{100}")

            readBLOB(s)    
            # Create a photoimage object of the image in the path
            image1 = Image.open(s)
            test = ImageTk.PhotoImage(image1)
            sa = tkinter.Label(image=test)
            sa.image = test

            # Position image
            sa.place(x=saa, y=70)
            image1 = Image.open(s)
            test = ImageTk.PhotoImage(image1)
            sa = tkinter.Label(image=test)
            sa.image = test

            # Position image
            sa.place(x=100, y=200)

    
except mysql.connector.Error as error:
    print("Failed to read BLOB data from MySQL table {}".format(error))



root.mainloop()
