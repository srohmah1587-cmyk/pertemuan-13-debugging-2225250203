
# Kasus 02: Menghitung Rata-rata Nilai
# Ketentuan: rata-rata dihitung dari jumlah nilai dibagi banyaknya data.

def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)


# Test case
test_cases = [
    ([80, 60, 90, 70], 75.0),
    ([100, 80], 90.0),
    ([60, 70, 80], 70.0),
    ([], 0),
]

print("PENGUJIAN RATA-RATA NILAI")
print("========================")

for data, expected in test_cases:
    actual = hitung_rata_rata(data)

    if actual == expected:
        status = "PASS"
    else:
        status = "FAIL"

    print(f"Data nilai: {data}")
    print(f"Expected: {expected}")
    print(f"Actual: {actual}")
    print(f"Status: {status}")
    print("------------------------")