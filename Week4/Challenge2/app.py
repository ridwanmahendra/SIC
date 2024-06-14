from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Konfigurasi MongoDB Atlas
# Ganti <username>, <password>, <cluster-url>, dan <dbname> dengan nilai yang sesuai
connection_string = "mongodb+srv://ridwanmahenra:ridwanmahenra@cluster0.h2olati.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string, tls=True, tlsAllowInvalidCertificates=True)
db = client['nama_database']  # Ganti 'nama_database' dengan nama database Anda
collection = db['sensor_data2']  # Koleksi untuk menyimpan data sensor

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

# Endpoint untuk mengambil semua data sensor berdasarkan nama sensor
@app.route('/sensor1/<sensor_name>/all', methods=['GET'])
def get_all_sensor_data(sensor_name):
    try:
        # Ambil semua data berdasarkan nama sensor
        data = list(collection.find({ "sensor_name": sensor_name }))
        
        # Ubah _id dari ObjectId ke string untuk JSON serialization
        for item in data:
            item['_id'] = str(item['_id'])
        
        return jsonify(data), 200
    
    except Exception as e:
        return jsonify({'message': 'Gagal mengambil data', 'error': str(e)}), 500

# Endpoint untuk menghitung nilai rata-rata data sensor berdasarkan nama sensor
@app.route('/sensor1/<sensor_name>/avg', methods=['GET'])
def get_avg_sensor_data(sensor_name):
    try:
        # Ambil semua data berdasarkan nama sensor
        data = list(collection.find({ "sensor_name": sensor_name }))
        
        if not data:
            return jsonify({'message': 'Data tidak ditemukan'}), 404
        
        # Hitung nilai rata-rata temperature dan kelembapan
        total_temperature = sum(item['temperature'] for item in data)
        total_kelembapan = sum(item['kelembapan'] for item in data)
        
        avg_temperature = total_temperature / len(data)
        avg_kelembapan = total_kelembapan / len(data)
        
        return jsonify({
            'average_temperature': avg_temperature,
            'average_kelembapan': avg_kelembapan
        }), 200
    
    except Exception as e:
        return jsonify({'message': 'Gagal menghitung rata-rata', 'error': str(e)}), 500

# Menjalankan aplikasi Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
