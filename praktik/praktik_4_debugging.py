def hitung_rata_rata(nilai):
    return sum(nilai) / 5

def status(nilai):
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"

def nilai_tertinggi(nilai):
    tertinggi = 0
    for x in nilai:
        if x < tertinggi:
            tertinggi = x
    return tertinggi

nilai = [80, 60, 90, 70]
print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))

# kode setelah perbaikan minimal
def hitung_rata_rata(nilai):
    return sum(nilai) / len(nilai)


def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


def nilai_tertinggi(nilai):
    tertinggi = nilai[0]
    for x in nilai:
        if x > tertinggi:
            tertinggi = x
    return tertinggi


nilai = [80, 60, 90, 70]

print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))

# kode pengujian test case memeriksa kelima test case secara otomatis

def jalankan_test():
    tests = [
        ("T1", hitung_rata_rata([80, 60, 90, 70]), 75.0),
        ("T2", hitung_rata_rata([100, 80]), 90.0),
        ("T3", status(60), "Lulus"),
        ("T4", status(59), "Tidak lulus"),
        ("T5", nilai_tertinggi([80, 60, 90, 70]), 90),
    ]

    for nama, aktual, expected in tests:
        hasil = "PASS" if aktual == expected else "FAIL"
        print(f"{nama}: {hasil} | Expected: {expected} | Actual: {aktual}")


jalankan_test()