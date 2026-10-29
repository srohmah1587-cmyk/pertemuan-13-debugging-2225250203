# Pertemuan 13 - Debugging dan Testing

**Nama:** Siti Rohmah  
**NIM:** 2225250203  
**Kelas:** 3A

## Kasus

Program yang diuji terdiri dari tiga fungsi Python, yaitu `hitung_rata_rata()` untuk menghitung rata-rata nilai, `status()` untuk menentukan kelulusan mahasiswa, dan `nilai_tertinggi()` untuk mencari nilai maksimum dari suatu list.

Pengujian dilakukan untuk menemukan kesalahan logika, memperbaiki kode dengan perubahan minimal, dan memastikan hasilnya sesuai dengan test case yang ditentukan.

## Test Case

| ID | Input | Expected | Actual Awal | Status Awal |
|---|---|---|---|---|
| T1 | `[80, 60, 90, 70]` | `75.0` | `60.0` | FAIL |
| T2 | `[100, 80]` | `90.0` | `36.0` | FAIL |
| T3 | `60` | `Lulus` | `Tidak lulus` | FAIL |
| T4 | `59` | `Tidak lulus` | `Tidak lulus` | PASS |
| T5 | `[80, 60, 90, 70]` | `90` | `0` | FAIL |

## Bug Report

### Bug 1: Perhitungan rata-rata

- **Gejala:** Hasil rata-rata tidak sesuai dengan data.
- **Lokasi:** Fungsi `hitung_rata_rata()`, baris pembagian.
- **Akar penyebab:** Program selalu membagi jumlah nilai dengan 5.
- **Perbaikan:** Menggunakan `len(nilai)` sebagai pembagi agar sesuai dengan jumlah elemen list.

### Bug 2: Penentuan kelulusan

- **Gejala:** Nilai 60 dinyatakan tidak lulus.
- **Lokasi:** Fungsi `status()`, kondisi `if nilai > 60`.
- **Akar penyebab:** Operator `>` tidak mencakup nilai yang sama dengan 60.
- **Perbaikan:** Mengubah operator menjadi `>=`.

### Bug 3: Pencarian nilai tertinggi

- **Gejala:** Fungsi menghasilkan 0 meskipun data memiliki nilai yang lebih tinggi.
- **Lokasi:** Fungsi `nilai_tertinggi()`, inisialisasi variabel dan kondisi perbandingan.
- **Akar penyebab:** Nilai awal ditetapkan 0 dan operator pembanding menggunakan `<`.
- **Perbaikan:** Menginisialisasi `tertinggi` dengan elemen pertama list dan menggunakan operator `>`.

## Retest

Setelah perbaikan, kelima test case dijalankan kembali. Hasil yang diharapkan adalah:

| ID | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|
| T1 | `75.0` | `75.0` | PASS |
| T2 | `90.0` | `90.0` | PASS |
| T3 | `Lulus` | `Lulus` | PASS |
| T4 | `Tidak lulus` | `Tidak lulus` | PASS |
| T5 | `90` | `90` | PASS |

## Cara Menjalankan

Jalankan perintah berikut dari direktori utama proyek:

```bash
python3 praktik/praktik_4_debugging.py
```

## Refleksi

Teknik debugging yang paling membantu adalah tracing variabel dan penggunaan breakpoint pada VS Code. Tracing membantu melihat perubahan nilai variabel pada setiap langkah, sedangkan breakpoint memungkinkan program dihentikan pada bagian tertentu untuk memeriksa alur eksekusi.

Dari praktik ini, saya memahami bahwa kesalahan logika dapat menyebabkan program menghasilkan output yang keliru meskipun tidak menampilkan pesan error. Pengujian dengan beberapa input membantu menemukan bug dan memastikan perbaikan bekerja sesuai harapan.