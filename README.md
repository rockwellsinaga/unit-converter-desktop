# Length Unit Converter

Aplikasi desktop sederhana untuk mengonversi satuan panjang antara meter, foot, yard, dan inch. Proyek ini awalnya dibuat sebagai tugas dasar pemrograman Python dan dipertahankan sebagai bagian dari perjalanan belajar saya.

Versi terbaru memisahkan logika konversi dari antarmuka Tkinter. Dengan begitu, perhitungannya dapat diuji otomatis tanpa harus membuka jendela aplikasi.

## Fitur

- Konversi dua arah antara empat satuan panjang.
- Validasi input numerik dengan pesan kesalahan yang jelas.
- Tombol untuk mengonversi, membersihkan formulir, dan menutup aplikasi.
- Unit test untuk logika konversi dan validasi unit.

## Menjalankan aplikasi

Pastikan Python 3 dengan dukungan Tkinter telah terpasang, lalu jalankan:

```bash
python UnitConv.py
```

## Menjalankan test

```bash
python -m unittest discover -s tests -v
```

## Struktur proyek

```text
.
├── UnitConv.py
├── tests/
│   └── test_unit_converter.py
└── README.md
```

## Catatan perjalanan

Repository ini sengaja tetap sederhana. Tujuannya bukan menjadi aplikasi konversi berskala besar, tetapi menunjukkan perkembangan dari script GUI satu file menuju kode yang lebih terstruktur, dapat digunakan ulang, dan dapat diuji.
