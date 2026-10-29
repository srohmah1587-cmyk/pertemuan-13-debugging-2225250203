# Kasus 03: Membaca File Nilai Mahasiswa
# Nama  : Siti Rohmah
# NIM   : 2225250203
# Kelas : 3A

from pathlib import Path


def baca_nilai(nama_file):
    data_nilai = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()

                # Lewati baris kosong
                if not baris:
                    continue

                bagian = baris.split(",")

                if len(bagian) != 2:
                    print(
                        f"Peringatan: Format salah pada baris "
                        f"{nomor_baris}."
                    )
                    continue

                nim = bagian[0].strip()
                nilai_teks = bagian[1].strip()

                try:
                    nilai = float(nilai_teks)
                except ValueError:
                    print(
                        f"Peringatan: Nilai tidak valid pada baris "
                        f"{nomor_baris}."
                    )
                    continue

                if not nim or not 0 <= nilai <= 100:
                    print(
                        f"Peringatan: Data tidak valid pada baris "
                        f"{nomor_baris}."
                    )
                    continue

                data_nilai.append((nim, nilai))

    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan.")
        return None

    return data_nilai


def rekap_nilai(data_nilai, batas_lulus=60):
    if not data_nilai:
        print("Tidak ada data nilai yang valid.")
        return

    daftar_nilai = [nilai for nim, nilai in data_nilai]
    rata_rata = sum(daftar_nilai) / len(daftar_nilai)
    tertinggi = max(daftar_nilai)
    terendah = min(daftar_nilai)
    jumlah_lulus = sum(
        1 for nilai in daftar_nilai if nilai >= batas_lulus
    )

    print("\nREKAP NILAI MAHASISWA")
    print("=====================")
    print(f"Jumlah mahasiswa : {len(data_nilai)}")
    print(f"Rata-rata nilai  : {rata_rata:.2f}")
    print(f"Nilai tertinggi  : {tertinggi:g}")
    print(f"Nilai terendah   : {terendah:g}")
    print(f"Jumlah lulus     : {jumlah_lulus}")
    print(f"Jumlah tidak lulus: {len(data_nilai) - jumlah_lulus}")

    print("\nDETAIL NILAI")
    print("============")
    for nim, nilai in data_nilai:
        status = "Lulus" if nilai >= batas_lulus else "Tidak lulus"
        print(f"{nim} | {nilai:g} | {status}")


if __name__ == "__main__":
    lokasi_file = Path(__file__).resolve().parent.parent / "data" / "nilai.txt"
    data = baca_nilai(lokasi_file)

    if data is not None:
        rekap_nilai(data)