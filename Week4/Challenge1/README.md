
# Penggunaan Flask




## Langkah 1: Instal dan Perbarui Modul

Pastikan Anda telah menginstal dan memperbarui Flask dan PyMongo. Jika belum, jalankan perintah berikut di terminal:

```bash
  pip install --upgrade Flask pymongo
```

## Langkah 2: Jalankan Aplikasi Flask
* Simpan kode di atas *app.py.*
* Jalankan aplikasi dengan perintah berikut di terminal:

```bash
  python app.py
```
* Aplikasi akan berjalan di http://127.0.0.1:5000/
* Gunakan Postman atau Curl untuk mengirim permintaan POST ke endpoint /sensor1 dengan body JSON seperti ini:

```
{
    "temperature": 25.5,
    "kelembapan": 60
}
```

# Penggunaan Postman

## Langkah 1: Jalankan Aplikasi Flask
Pastikan aplikasi Flask Anda sudah berjalan. Anda harus melihat output di terminal yang menunjukkan bahwa Flask sedang berjalan di http://127.0.0.1:5000/.

## Langkah 2: Buka Postman
Buka Postman di komputer Anda.
## Langkah 3: Buat Request Baru di Postman
* Klik tombol New atau + di tab untuk membuat request baru.
* Pilih metode POST dari dropdown menu di sebelah kiri URL input field.
* Masukkan URL endpoint Anda: http://127.0.0.1:5000/sensor1.
## Langkah 4: Menyusun Body Request
* Klik tab Body di bawah URL input field.
+ Pilih raw sebagai tipe input.
- Di dropdown sebelah kanan (yang defaultnya berisi Text), pilih JSON.
## Langkah 5: Masukkan Data JSON
- Masukkan JSON payload ke dalam editor. Contohnya:
```
{
    "temperature": 25.5,
    "kelembapan": 60
}
```
## Langkah 6: Mengirimkan Request
* Klik tombol Send di sebelah kanan atas untuk mengirim request.
* Anda harus melihat respon dari server di bagian bawah Postman.
## Langkah 7: Memeriksa Respon
Jika request berhasil, Anda akan melihat respon JSON yang menunjukkan data berhasil disimpan, contohnya:
```
{
    "message": "Data berhasil disimpan",
    "inserted_id": "<ID dokumen yang baru dimasukkan>"
}
```

Jika request gagal, Anda akan melihat pesan error, contohnya:

```
{
    "message": "Gagal menyimpan data",
    "error": "<deskripsi error>"
}
```

If you experience any problems or have questions, please feel free to contact [Ridwan Mahenra] at [ridwanmahenra@gmail.com].

Enjoy using the application!