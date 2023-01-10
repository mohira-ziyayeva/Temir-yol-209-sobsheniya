import time
import mysql.connector
time.strftime('%Y-%m-%d %H:%M:%S')


id_poezd = input("id----->: ")
kod_sabsheniya = input("kod_sabsheniya----->: ")
xabarlarni_uzatish_stantsiyasi = input("xabarlarni_uzatish_stantsiyasi------->: ")
nomer_poezda= input("nomer_poezda-------->: ")
eski_index = input("eski_index-------->: ")
ozgartirish_sababi = input("ozgartirish_sababi----------->: ")
sana_vaqt_indeks_ozgarishi = input("sana_vaqt_indeks_ozgarishi--------->: ")
yangi_indeks = input("yangi_indeks--------->: ")

try:

    connection = mysql.connector.connect(host='localhost',
                                         database='temiryolspravka',
                                         user='root',
                                         password='admin')



    mySql_insert_query = """INSERT INTO mohira (id, kod_sabsheniya, xabarlarni_uzatish_stantsiyasi, nomer_poezda, eski_index, ozgartirish_sababi, sana_vaqt_indeks_ozgarishi, yangi_indeks) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
    val = (id_poezd, kod_sabsheniya, xabarlarni_uzatish_stantsiyasi, nomer_poezda, eski_index, ozgartirish_sababi,  sana_vaqt_indeks_ozgarishi, yangi_indeks)
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query, val)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into mohira table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into akmal table {}".format(error))


finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")