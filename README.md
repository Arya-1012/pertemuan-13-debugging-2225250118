# Pertemuan 13 - Debugging, Tracing, Testing, dan Test Case

**Nama:** isi nama  
**NIM:** isi NIM  
**Kelas:** isi kelas  

## Deskripsi
Proyek latihan Python untuk mempelajari debugging, tracing, penggunaan debugger VS Code, pembuatan test case, perbaikan bug, dan pengujian ulang.

## Struktur Folder
- `kasus/`: tiga contoh program bermasalah atau kasus input file.
- `latihan/`: latihan tracing, fungsi, test case, dan breakpoint.
- `praktik/`: Praktik 4 dengan perbaikan bug dan pengujian otomatis.

## Cara Menjalankan
1. Buka folder proyek ini di VS Code.
2. Pastikan Python 3 sudah terpasang dan interpreter dipilih.
3. Buka **Terminal > New Terminal**.
4. Jalankan file yang ingin dicoba, misalnya:

```bash
python praktik/praktik_4_debugging.py
```

Untuk file lain, jalankan salah satu contoh berikut:

```bash
python kasus/kasus_01_batas_kelulusan.py
python kasus/kasus_02_rata_rata.py
python latihan/01_trace_loop.py
python latihan/03_test_case.py
```

Pada beberapa sistem, gunakan `python3` sebagai pengganti `python`.

## Test Case Praktik 4

| ID | Input | Expected |
|---|---|---|
| T1 | `[80, 60, 90, 70]` | Rata-rata `75.0` |
| T2 | `[100, 80]` | Rata-rata `90.0` |
| T3 | Nilai `60` | `Lulus` |
| T4 | Nilai `59` | `Tidak lulus` |
| T5 | `[80, 60, 90, 70]` | Nilai tertinggi `90` |
| T6 | List kosong untuk rata-rata | `0` |
| T7 | List kosong untuk nilai tertinggi | `None` |

## Bug Report

1. **Bug rata-rata**  
   Gejala: hasil salah ketika jumlah data bukan lima.  
   Penyebab: pembagi ditulis tetap `/ 5`.  
   Perbaikan: menggunakan `sum(nilai) / len(nilai)` dan menangani list kosong.

2. **Bug status kelulusan**  
   Gejala: nilai 60 dianggap tidak lulus.  
   Penyebab: menggunakan `nilai > 60`.  
   Perbaikan: mengganti menjadi `nilai >= 60`.

3. **Bug nilai tertinggi**  
   Gejala: perbandingan memakai arah yang salah sehingga nilai tertinggi tidak ditemukan.  
   Penyebab: memakai `x < tertinggi`.  
   Perbaikan: mulai dari elemen pertama dan gunakan `x > tertinggi`.

## Retest
Jalankan `python praktik/praktik_4_debugging.py`. Semua test case seharusnya menampilkan `PASS`.

## Debugger VS Code
1. Klik di sebelah kiri nomor baris untuk membuat breakpoint.
2. Pilih **Run and Debug > Python File**.
3. Gunakan **Step Over**, **Step Into**, dan **Step Out** untuk menelusuri eksekusi.
4. Amati panel **Variables** dan **Call Stack**.

## GitHub
Setelah membuat repository GitHub dan menghubungkannya, jalankan:

```bash
git init
git add .
git commit -m "chore: menambahkan kasus debugging awal"
git branch -M main
git remote add origin https://github.com/USERNAME/pertemuan-13-debugging-NIM.git
git push -u origin main
```

Setelah melakukan perbaikan atau melengkapi dokumentasi:

```bash
git add .
git commit -m "fix: memperbaiki bug dan menambahkan test case"
git push
```

Ganti `USERNAME` dan `NIM` sesuai akun dan identitas sendiri.
