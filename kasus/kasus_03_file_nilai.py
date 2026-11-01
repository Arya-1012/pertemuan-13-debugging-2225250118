# Kasus 3: File I/O dan error handling
# Program membaca nilai dari file nilai.txt.
# Buat file nilai.txt di folder yang sama, satu nilai per baris.

def baca_nilai(nama_file):
    nilai = []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                if baris:
                    nilai.append(float(baris))
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
    except ValueError:
        print("File berisi data yang bukan angka.")
    return nilai


if __name__ == "__main__":
    data = baca_nilai("nilai.txt")
    print("Data nilai:", data)
