def rata_rata(data):
    total = sum(data)
    return total / 5

print(rata_rata([80, 90, 70]))

#perbaikan kode python
def rata_rata(data):
    if len(data) == 0:
        return "List kosong, rata-rata tidak dapat dihitung"

    total = sum(data)
    return total / len(data)


print(rata_rata([80, 90, 70]))
print(rata_rata([60, 80]))
print(rata_rata([70, 80, 90, 100, 60]))
print(rata_rata([]))