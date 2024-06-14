
# Penggunaan Flask
## Langkah 1: Instal dan Perbarui Modul

Pastikan Anda telah menginstal dan memperbarui Flask dan PyMongo. Jika belum, jalankan perintah berikut di terminal:

```bash
  pip install Flask pymongo
```

## Langkah 2: Jalankan Aplikasi Flask
* Simpan kode di atas *app.py.*
* Jalankan aplikasi dengan perintah berikut di terminal:

```bash
  python app.py
```
* Aplikasi akan berjalan di http://127.0.0.1:5000/



# Pengujian Menggunakan Postman
### POST Request untuk Menyimpan Data
* Buka Postman dan buat request baru dengan metode POST.
* Masukkan URL http://127.0.0.1:5000/sensor1
* Di tab Body, pilih raw dan kemudian JSON.
* Masukkan JSON payload seperti ini:
```
{
    "sensor_name": "sensor1",
    "temperature": 25.5,
    "kelembapan": 60
}
```
* Klik `Send`

### GET Request untuk Mengambil Semua Data
* Buka Postman dan buat request baru dengan metode GET.
* Masukkan URL http://127.0.0.1:5000/sensor1/sensor1/all
* Klik `Send`
* Anda akan melihat semua data yang disimpan untuk sensor1.

### GET Request untuk Menghitung Rata-Rata
* Buka Postman dan buat request baru dengan metode GET.
* Masukkan URL http://127.0.0.1:5000/sensor1/sensor1/avg
* Klik `Send`
* Anda akan melihat nilai rata-rata temperature dan kelembapan untuk sensor1.



If you experience any problems or have questions, please feel free to contact [Ridwan Mahenra] at [ridwanmahenra@gmail.com].

Enjoy using the application!