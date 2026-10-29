
# Kasus 01: Batas Kelulusan
# Ketentuan: nilai >= 60 dinyatakan lulus

def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


# Test case
test_cases = [
    (59, "Tidak lulus"),
    (60, "Lulus"),
    (61, "Lulus"),
]

print("PENGUJIAN BATAS KELULUSAN")
print("=========================")

for nilai, expected in test_cases:
    actual = status_lulus(nilai)

    if actual == expected:
        status = "PASS"
    else:
        status = "FAIL"

    print(f"Nilai: {nilai}")
    print(f"Expected: {expected}")
    print(f"Actual: {actual}")
    print(f"Status: {status}")
    print("-------------------------")