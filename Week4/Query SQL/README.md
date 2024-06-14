# Persiapan
* https://www.db-fiddle.com/
* masukan Schema SQL:
```
CREATE TABLE student_grades (
    exam_result_id INT PRIMARY KEY,
    name VARCHAR(50),
    subject VARCHAR(50),
    score INT,
    exam_date DATE
);
INSERT INTO student_grades (exam_result_id, name, subject, score, exam_date)
VALUES
(111, 'Alice', 'physics', 9, '2020-02-02'),
(112, 'Alice', 'Math', 8, '2020-03-03'),
(113, 'Alice', 'CS', 6, '2020-01-01'),
(114, 'Bob', 'Geography', 5, '2020-02-02'),
(115, 'Bob', 'Physics', 7, '2020-01-01'),
(116, 'Charles', 'Physics', NULL, '2020-08-01');
```

#
## SELECT statement/ SQL query
```
SELECT score
FROM student_grades
```
- `SELECT` clause: Bagian ini menentukan kolom atau ekspresi apa yang ingin ditampilkan dalam hasil query. Misalnya, `SELECT column1, column2` akan mengambil nilai dari column1 dan column2.

- `FROM` clause: Menentukan tabel dari mana data akan diambil. Contoh, `FROM tablename` akan mengambil data dari tabel dengan nama tablename.

#
```
SELECT score AS grade,  -- Menggunakan AS untuk memberi alias kolom score menjadi grade
       name            -- Kolom name tetap ditampilkan tanpa perubahan
FROM student_grades;    -- Memilih data dari tabel student_grades
```
- `SELECT score AS grade`: Dalam bagian SELECT,  `score` adalah nama kolom asli dari tabel `student_grades`, sedangkan `AS grade` memberi alias atau menamai ulang kolom tersebut menjadi `grade`. Dengan ini, dalam hasil query, nilai dari kolom score akan ditampilkan dengan nama `grade`.

- `name`: Kolom name tidak diberi alias atau diubah namanya, sehingga nilai dari kolom ini akan ditampilkan dengan nama `name` seperti pada tabel aslinya.

- `FROM student_grades`: Mengindikasikan bahwa data yang diambil berasal dari tabel `student_grades`.

Jadi, hasil dari query ini akan menampilkan nilai dari kolom score dengan nama `grade` dan kolom name tanpa perubahan, dari tabel `student_grades`. Dengan demikian, `SELECT` statement dalam SQL memungkinkan untuk fleksibilitas dalam menentukan bagaimana nama dan urutan kolom ditampilkan dalam hasil query.

#
```
SELECT score + 1 AS augmented_score
FROM student_grades;
```
- `SELECT score + 1 AS augmented_score`: Dalam bagian SELECT, `score + 1 `adalah ekspresi aritmatika yang mengambil nilai dari kolom `score` dalam setiap baris dari tabel `student_grades`, lalu menambahkan 1 ke nilai tersebut. Hasil dari operasi ini diberi alias dengan nama `augmented_score`.

- `FROM student_grades`: Menunjukkan bahwa data yang diambil berasal dari tabel `student_grades`.

Jadi, hasil dari query ini akan menghasilkan satu kolom tambahan dalam hasilnya, yang dinamakan `augmented_score`, dan nilai dari kolom ini adalah nilai `score` dari setiap baris dalam tabel `student_grades` yang ditambah 1. Misalnya, jika ada baris dengan score 85, maka `augmented_score` akan bernilai 86.

#
```
SELECT * 
FROM student_grades;
```
- `SELECT *`: Tanda bintang (*) digunakan sebagai wildcard dalam SQL untuk memilih semua kolom yang ada dalam tabel. Dengan menggunakan `*`, kita menyatakan bahwa kita ingin mengambil semua kolom dari tabel `student_grades`.

- `FROM student_grades`: Menunjukkan bahwa data yang diambil berasal dari tabel `student_grades`.

Jadi, hasil dari query ini akan mengembalikan semua data yang ada dalam tabel `student_grades`, termasuk semua kolom yang ada di dalamnya. Ini adalah cara yang sangat praktis untuk mendapatkan semua informasi yang tersedia tentang setiap entitas atau objek (dalam hal ini, siswa dan nilai mereka) dalam basis data.

#
```
SELECT * EXCEPT (exam_date)
FROM student_grades
```
Dalam SQL tidak ada. diganti dengan nama kolom yang di ingin kan.

#
```
SELECT *
FROM student_grades
WHERE name = 'Alice';
```
-  `SELECT *`: Tanda bintang `(*)` digunakan untuk memilih semua kolom yang ada dalam tabel `student_grades`. Dalam konteks ini, ini berarti kita akan mengambil semua kolom untuk setiap baris yang memenuhi kondisi yang ditentukan.

- `FROM student_grades`: Menunjukkan bahwa data yang akan diambil berasal dari tabel `student_grades`.

- `WHERE name = 'Alice'`: Merupakan klausa `WHERE` yang digunakan untuk memfilter baris-baris data yang akan dimasukkan ke dalam hasil query. Dalam hal ini, hanya baris-baris di mana nilai kolom `name` adalah "Alice" yang akan dimasukkan.

Jadi, hasil dari query ini akan mengembalikan semua kolom untuk setiap baris dalam tabel `student_grades` di mana nilai kolom `name` sama dengan "Alice". Dengan demikian, kita hanya akan melihat data yang relevan dengan entitas atau objek yang memiliki nama "Alice" dalam data kita.

#
```
SELECT *
FROM student_grades
WHERE name IN ('Alice', 'Bob');
```
- `SELECT *`: Tanda bintang `(*)` digunakan untuk memilih semua kolom yang ada dalam tabel `student_grades`. Ini berarti kita akan mengambil semua kolom untuk setiap baris yang memenuhi salah satu dari kondisi yang ditentukan dalam klausa `WHERE`.

- `FROM student_grades`: Menunjukkan bahwa data yang akan diambil berasal dari tabel `student_grades`.

- `WHERE name IN ('Alice', 'Bob')`: Merupakan klausa `WHERE` yang digunakan untuk memfilter baris-baris data yang akan dimasukkan ke dalam hasil query. Dalam hal ini, hanya baris-baris di mana nilai kolom `name` adalah "Alice" atau "Bob" yang akan dimasukkan.

Dengan menggunakan operator `IN`, kita dapat menyediakan daftar nilai atau ekspresi yang memungkinkan kita untuk membandingkan nilai kolom dengan beberapa nilai sekaligus. Dalam contoh ini, kita memilih untuk mengambil data untuk semua siswa yang bernama "Alice" atau "Bob".

Hasil dari query ini akan mengembalikan semua kolom untuk setiap baris dalam tabel `student_grades` di mana nilai kolom name sama dengan "Alice" atau "Bob". Ini sangat berguna ketika kita ingin memilih data untuk beberapa entitas atau objek yang memiliki beberapa nilai yang mungkin berbeda dalam kolom tertentu.

#

```
SELECT *
FROM student_grades
WHERE 
    (name IN ('Alice', 'Bob'))  -- Kondisi pertama: Memilih baris dengan nilai 'Alice' atau 'Bob' di kolom 'name'
    AND 
    (score >= 7);  -- Kondisi kedua: Memilih baris dengan nilai score yang lebih besar atau sama dengan 7
```

- `SELECT *`: Tanda bintang `(*)` digunakan untuk memilih semua kolom yang ada dalam tabel `student_grades`. Ini berarti kita akan mengambil semua kolom untuk setiap baris yang memenuhi kedua kondisi yang ditentukan dalam klausa `WHERE`.

- `FROM student_grades`: Menunjukkan bahwa data yang akan diambil berasal dari tabel `student_grades`.

- `WHERE (name IN ('Alice', 'Bob')) AND (score >= 7)`: Merupakan klausa `WHERE` yang menggabungkan dua kondisi dengan operator logika `AND`.

  - Kondisi pertama (name IN ('Alice', 'Bob')) memilih baris-baris di mana nilai kolom name adalah "Alice" atau "Bob".
  - Kondisi kedua (score >= 7) memilih baris-baris di mana nilai kolom score lebih besar atau sama dengan 7.
Jadi, hasil dari query ini akan mengembalikan semua kolom untuk setiap baris dalam tabel student_grades di mana nilai kolom name adalah "Alice" atau "Bob", dan nilai kolom score lebih besar atau sama dengan 7. Dengan demikian, kita hanya akan melihat data yang relevan dengan siswa yang bernama "Alice" atau "Bob" dan memiliki nilai score yang memenuhi atau melebihi nilai 7.

Ini adalah contoh penggunaan yang lebih kompleks dari klausa WHERE dalam SQL, di mana kita dapat menggabungkan beberapa kondisi untuk membatasi data yang dikembalikan berdasarkan kriteria yang lebih spesifik.

#

```
SELECT *
FROM student_grades
WHERE score IS NOT NULL;
```
- ``SELECT *`: Tanda bintang `(*)` digunakan untuk memilih semua kolom yang ada dalam tabel `student_grades`. Ini berarti kita akan mengambil semua kolom untuk setiap baris yang memenuhi kondisi yang ditentukan.

- `FROM student_grades`: Menunjukkan bahwa data yang akan diambil berasal dari tabel `student_grades`.

- `WHERE score IS NOT NULL`: Merupakan klausa `WHERE` yang digunakan untuk memfilter baris-baris data yang akan dimasukkan ke dalam hasil query. Dalam hal ini, kita hanya memilih baris-baris di mana nilai kolom `score` tidak `NULL`.

Operator `IS NOT NULL` digunakan untuk memeriksa apakah nilai kolom tersebut bukan NULL. Dengan menggunakan kondisi ini, query akan mengabaikan atau tidak memasukkan baris yang memiliki nilai `NULL` di kolom `score`.

Jadi, hasil dari query ini akan mengembalikan semua kolom untuk setiap baris dalam tabel `student_grades` di mana nilai kolom `score` tidak `NULL`. Ini berguna ketika kita ingin mengekstrak data yang lengkap atau valid, dan tidak tertarik dengan baris yang memiliki data yang hilang atau belum diisi dalam kolom tertentu.

#

```
SELECT *
FROM student_grades
LIMIT 4;
```

- `LIMIT 4`: Merupakan klausa `LIMIT` yang digunakan untuk membatasi jumlah baris yang akan dikembalikan oleh query. Dalam hal ini, query akan mengembalikan hanya 4 baris pertama yang ditemukan dalam tabel.

Jadi, hasil dari query ini akan mengembalikan semua kolom untuk 4 baris pertama dalam tabel `student_grades`. Klausa `LIMIT` sangat berguna ketika kita hanya tertarik untuk melihat sejumlah kecil data pertama atau saat kita ingin melakukan pengujian atau pengambilan sampel data.

#
```
SELECT DISTINCT name
FROM student_grades;
```

- `SELECT DISTINCT name`: Dalam bagian `SELECT`, `DISTINCT name` digunakan untuk memilih nilai unik dari kolom `name`. Ini berarti query akan mengembalikan nilai `name` yang berbeda-beda dan tidak ada duplikat.

Klausa `DISTINCT` sangat berguna ketika kita ingin melihat nilai-nilai unik dari suatu kolom tertentu dalam tabel. Dalam konteks ini, query akan mengambil setiap nilai unik dari kolom name yang ada dalam tabel `student_grades`.

Jadi, hasil dari query ini akan mengembalikan daftar nilai unik dari kolom name. Misalnya, jika tabel `student_grades` memiliki beberapa entri untuk siswa dengan nama yang sama, query ini akan mengembalikan setiap nama hanya satu kali tanpa adanya duplikat.

#

## Aggregation Functions
Fungsi agregasi dalam SQL digunakan untuk melakukan perhitungan di atas sekelompok nilai untuk menghasilkan satu nilai ringkasan. Fungsi agregasi sangat berguna untuk menghitung statistik, seperti total, rata-rata, nilai maksimum, nilai minimum, dan lain-lain, dari data dalam sebuah tabel. Berikut adalah beberapa fungsi agregasi umum yang sering digunakan dalam SQL:

- `COUNT()`: Menghitung jumlah baris yang memenuhi kriteria tertentu.
```
SELECT COUNT(*) FROM tablename;
```
- `SUM()`: Menghitung total nilai dari suatu kolom numerik.

```
SELECT SUM(column_name) FROM tablename;
```

- AVG(): Menghitung rata-rata nilai dari suatu kolom numerik.

```
SELECT AVG(column_name) FROM tablename;
```

- `MIN()`: Mengambil nilai minimum dari suatu kolom.

```
SELECT MIN(column_name) FROM tablename;
```
- `MAX()`: Mengambil nilai maksimum dari suatu kolom.
```
SELECT MAX(column_name) FROM tablename;
```

#### Contoh 1:
```
SELECT 
    MIN(exam_result_id) AS min_id,  -- Menghitung nilai minimum dari kolom exam_result_id, dan memberi alias sebagai min_id
    MAX(exam_result_id) AS max_id,  -- Menghitung nilai maksimum dari kolom exam_result_id, dan memberi alias sebagai max_id
    COUNT(score) AS count_score     -- Menghitung jumlah nilai yang tidak NULL dari kolom score, dan memberi alias sebagai count_score
FROM student_grades;
```
_Penjelasan dari query di atas:_

- `MIN(exam_result_id) AS min_id`: Menggunakan fungsi `MIN()` untuk mengambil nilai terkecil dari kolom `exam_result_id` dalam tabel `student_grades`. Hasil dari fungsi ini diberi alias sebagai `min_id`.

- `MAX(exam_result_id) AS max_id`: Menggunakan fungsi `MAX()` untuk mengambil nilai terbesar dari kolom `exam_result_id` dalam tabel `student_grades`. Hasil dari fungsi ini diberi alias sebagai `max_id`.

- `COUNT(score) AS count_score`: Menggunakan fungsi `COUNT()` untuk menghitung jumlah nilai yang tidak `NULL` dari kolom score dalam tabel `student_grades`. Hasil dari fungsi ini diberi alias sebagai `count_score`.

_Jadi, hasil dari query ini akan mengembalikan satu baris dengan tiga kolom hasil:_

- `min_id`: Nilai minimum dari kolom `exam_result_id` dalam tabel.
- `max_id`: Nilai maksimum dari kolom `exam_result_id` dalam tabel.
- `count_score`: Jumlah nilai yang tidak `NULL` dari kolom score dalam tabel.
#

#### Contoh 2:
```
SELECT 
    name,                          -- Memilih kolom name untuk dikelompokkan
    MIN(exam_result_id) AS min_id, -- Menghitung nilai minimum dari kolom exam_result_id dan memberi alias sebagai min_id
    MAX(exam_result_id) AS max_id, -- Menghitung nilai maksimum dari kolom exam_result_id dan memberi alias sebagai max_id
    AVG(score) AS avg_score        -- Menghitung rata-rata nilai dari kolom score dan memberi alias sebagai avg_score
FROM 
    student_grades
GROUP BY 
    name;  -- Mengelompokkan hasil berdasarkan nilai unik dari kolom name
```
_Penjelasan dari query di atas:_

- `SELECT name, ...`: Memilih kolom `name` untuk dikelompokkan. Ini adalah kolom yang akan digunakan sebagai kunci untuk mengelompokkan hasil.

- `MIN(exam_result_id) AS min_id`: Menggunakan fungsi `MIN()` untuk mengambil nilai terkecil dari kolom `exam_result_id` dalam setiap kelompok (group) yang dibuat oleh nilai unik dari kolom `name`. Hasil dari fungsi ini diberi alias sebagai `min_id`.

- `MAX(exam_result_id) AS max_id`: Menggunakan fungsi `MAX()` untuk mengambil nilai terbesar dari kolom `exam_result_id` dalam setiap kelompok yang dibuat oleh nilai unik dari kolom `name`. Hasil dari fungsi ini diberi alias sebagai `max_id`.

- `AVG(score) AS avg_score`: Menggunakan fungsi `AVG()` untuk menghitung rata-rata nilai dari kolom `score` dalam setiap kelompok yang dibuat oleh nilai unik dari kolom `name`. Hasil dari fungsi ini diberi alias sebagai `avg_score`.

- `FROM student_grades`: Menunjukkan bahwa data yang akan diambil berasal dari tabel `student_grades`.

- `GROUP BY name`: Mengelompokkan hasil berdasarkan nilai unik dari kolom `name`. Ini berarti query akan menghitung statistik (nilai minimum, maksimum, dan rata-rata dari kolom `exam_result_id` dan `score`) untuk setiap nilai unik yang ada dalam kolom `name`.

Jadi, hasil dari query ini akan mengembalikan beberapa statistik dasar (`min_id`, `max_id`, dan `avg_score`) untuk setiap siswa yang ada dalam tabel `student_grades`, dihitung berdasarkan nilai unik dari kolom `name`. Ini berguna ketika Anda ingin menganalisis atau melaporkan statistik per individu atau entitas dalam basis data Anda.

#
### ORDER BY to sort the query results by column 
```
SELECT *
FROM student_grades
ORDER BY score DESC;
```
_Penjelasan dari query di atas:_

- `SELECT *`: Tanda bintang `(*)` digunakan untuk memilih semua kolom yang ada dalam tabel `student_grades`. Ini berarti kita akan mengambil semua kolom untuk setiap baris dalam tabel.

- `FROM student_grades`: Menunjukkan bahwa data yang akan diambil berasal dari tabel `student_grades`.

- `ORDER BY score DESC`: Merupakan klausa `ORDER BY` yang digunakan untuk mengurutkan hasil query berdasarkan nilai kolom `score` secara menurun (descending). `DESC` adalah singkatan dari descending, yang berarti urutan dari nilai tertinggi ke terendah.

Jadi, hasil dari query ini akan mengembalikan semua kolom dari tabel `student_grades`, diurutkan berdasarkan nilai `score` dari yang tertinggi ke yang terendah. Dengan menggunakan klausa `ORDER BY`, kita dapat dengan mudah mengurutkan hasil query berdasarkan kolom tertentu sesuai dengan kebutuhan analisis atau tampilan data.









