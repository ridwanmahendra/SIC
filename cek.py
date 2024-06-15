from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Konfigurasi MongoDB Atlas
# Ganti <username>, <password>, <cluster-url>, dan <dbname> dengan nilai yang sesuai
connection_string = "mongodb+srv://ridwanmahenra:ridwanmahenra@cluster0.h2olati.mongodb.net/?retryWrites=true&w=majority"

try:
    # Buat instance MongoClient tanpa verifikasi SSL
    client = MongoClient(connection_string, tls=True, tlsAllowInvalidCertificates=True)

    # Memeriksa koneksi dengan mencoba untuk mengambil nama database
    print("Mencoba terhubung ke database...")
    db_names = client.list_database_names()
    print("Koneksi berhasil! Nama database yang tersedia:", db_names)

except PyMongoError as e:
    print("Koneksi gagal. Error:", e)