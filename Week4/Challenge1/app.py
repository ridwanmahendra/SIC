from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Konfigurasi MongoDB Atlas
# Ganti <username>, <password>, <cluster-url>, dan <dbname> dengan nilai yang sesuai
connection_string = "mongodb+srv://ridwanmahenra:ridwanmahenra@cluster0.h2olati.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string, tls=True, tlsAllowInvalidCertificates=True)
db = client['week4']  # Ganti 'nama_database' dengan nama database Anda
collection = db['challenge1']  # Koleksi untuk menyimpan data sensor

# Endpoint untuk menyimpan data sensor
@app.route('/sensor1', methods=['POST'])
def insert_sensor_data():
    try:
        # Ambil data dari request JSON
        data = request.get_json()
        
        # Pastikan data lengkap (temperature, kelembapan)
        if 'temperature' not in data or 'kelembapan' not in data:
            return jsonify({'message': 'Data tidak lengkap'}), 400
        
        # Tambahkan timestamp
        data['timestamp'] = datetime.now()

        # Masukkan data ke dalam database
        result = collection.insert_one(data)

        return jsonify({'message': 'Data berhasil disimpan', 'inserted_id': str(result.inserted_id)}), 201
    
    except Exception as e:
        return jsonify({'message': 'Gagal menyimpan data', 'error': str(e)}), 500

# Menjalankan aplikasi Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
