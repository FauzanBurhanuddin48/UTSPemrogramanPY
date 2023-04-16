#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

#Koneksi dari database
dataBase = mysql.connector.connect(
    user  = 'root',
    host = 'localhost'
)#untuk membuat koneksi ke server MySQL lokal dengan menggunakan username "root" dan host "localhost".

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE db_V3922020")#Membuat database baru


# In[2]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'db_V3922020'
)#menyambungkan ke database

cursorObject = dataBase.cursor()#eksekusi perintah SQL pada database.


DataBarang = """CREATE TABLE data_stok_barang (
                    Id_Barang VARCHAR(10) PRIMARY KEY,
                    Nama_Barang VARCHAR(20),
                    Harga_Barang INT,
                    Stok_Awal INT,
                    Barang_Masuk INT,
                    Barang_Keluar INT,
                    Stok_Akhir INT
                    )"""#membuat tabel

cursorObject.execute(DataBarang)#methodeksekusi 


dataBase.close()#memutuskan koneksi dari server MySQL.


# In[5]:


import mysql.connector

#Koneksi ke database
dataBase = mysql.connector.connect(
    user = 'root',
    host = 'localhost',
    database = 'db_V3922020'
)

cursorObject = dataBase.cursor()

#Fungsi untuk menambahkan data ke tabel
def insert_data( Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir ):
    sql = "INSERT INTO data_stok_barang (Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)    VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)
    
    cursorObject.execute(sql, val)
    dataBase.commit()

    print(" ")
    print("Data berhasil ditambahkan")

#Fungsi untuk menampilkan data dari tabel
def show_data():
    query = "SELECT * FROM data_stok_barang"
    
    cursorObject.execute(query)

    myresult = cursorObject.fetchall()

    for x in myresult:
        print(x)
        
    print(" ")
    print("Data berhasil ditampilkan")

#Fungsi untuk mengupdate data di tabel
def update_data(Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir):
    sql = "UPDATE data_stok_barang SET Nama_Barang = %s, Harga_Barang = %s, Stok_Awal = %s, Barang_Masuk = %s, Barang_Keluar = %s, Stok_Akhir = %s WHERE Id_Barang = %s"
    val = (Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir, Id_Barang)
    
    cursorObject.execute(sql, val)
    dataBase.commit()
    
    print(" ")
    print("Data berhasil diupdate")

#Fungsi untuk menghapus data dari tabel
def delete_data(Id_Barang):
    sql = "DELETE FROM data_stok_barang WHERE Id_Barang = %s"
    val = (Id_Barang,)
    
    cursorObject.execute(sql, val)
    dataBase.commit()
    
    print(" ")
    print("Data berhasil dihapus")


def search_data(id_barang):#Fungsi untuk mencari data
    sql = "SELECT * FROM data_stok_barang WHERE Id_Barang = %s"
    val = (Id_Barang,)
    
    cursorObject.execute(sql, val)
    
    myresult = cursorObject.fetchall()
    
    for x in myresult:
        print(x)
        
    print(" ")
    print("Data berhasil ditemukan")

#pilihan menu
while True:
    print(" ")
    print("=== APLIKASI DATABASE PYTHON ===")
    print("1. Insert data")
    print("2. Show data")
    print("3. Update data")
    print("4. Hapus data")
    print("5. Cari data")
    print("6. Keluar")
    print("-------------------")
    menu = input("Pilih menu> ") #input untuk pilihan menu yang akan dicari
    print(" ")

    #pilihan 1 "insert data"
    if menu == "1":
        Id_Barang = input("Masukkan Id Barang : ")
        Nama_Barang = input("Masukkan Nama Barang : ")
        Harga_Barang = int(input("Masukkan Harga Barang : "))
        Stok_Awal = int(input("Masukkan Stok Awal : "))
        Barang_Masuk = int(input("Masukkan Barang Masuk : "))
        Barang_Keluar = int(input("Masukkan Barang Keluar : "))
        
        
        Stok_Akhir = Stok_Awal + Barang_Masuk - Barang_Keluar#Rumus untuk mencari stok_akhir
        
       
        print("Stok Akhir : ", Stok_Akhir) #mencetak Stok_Akhir dari rumus sebelumnya
        
        insert_data(Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)
    
    #pilihan 2 "show data"
    elif menu == "2":
        show_data()

    #pilihan 3 "update data"
    elif menu == "3":
        Id_Barang = input("Masukkan Id Barang yang akan diupdate : ")
        Nama_Barang = input("Masukkan Nama Barang baru : ")
        Harga_Barang = int(input("Masukkan Harga Barang baru : "))
        Stok_Awal = int(input("Masukkan Stok Awal baru : "))
        Barang_Masuk = int(input("Masukkan Barang Masuk baru : "))
        Barang_Keluar = int(input("Masukkan Barang Keluar baru : "))
        
        Stok_Akhir = Stok_Awal + Barang_Masuk - Barang_Keluar
        print("Stok Akhir setelah diupdate : ", Stok_Akhir)
        
        update_data(Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)

    #pilihan 4 "hapus data"
    elif menu == "4":
        Id_Barang = input("Masukkan Id Barang yang ingin dihapus : ")
        
        delete_data(Id_Barang)

    #pilihan 5 "cari data"
    elif menu == "5":
        Id_Barang = input("Masukkan Id Barang yang ingin dicari : ")
        
        search_data(Id_Barang)

    #pilihan 6 "keluar dari program"
    elif menu == "6":
        print("Terima kasih telah menggunakan program ini")
        break

    #ketika menginputkan tidak sesuai dengan pilihan yang tertera
    else:
        print("Pilih menu dengan benar")


# In[ ]:




