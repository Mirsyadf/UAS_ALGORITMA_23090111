mahasiswa = []

while True:
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    mahasiswa.append({"NIM": nim, "Nama": nama})
    maulagi = input("Apakah ingin menambahkan data lagi? (ya/tidak): ").lower()

    if maulagi != "ya":
        break

print("\nData Mahasiswa:")
for data in mahasiswa:
    print(f"NIM: {data['NIM']}, Nama: {data['Nama']}")
