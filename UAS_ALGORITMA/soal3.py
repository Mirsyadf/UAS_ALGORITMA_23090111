from collections import deque

class QueueSystem:
    def __init__(self):
        self.antrian = deque()
    
    def enqueue(self):
        pesanan = input('Masukkan nama pesanan: ')
        self.antrian.append(pesanan)
        print(f'Pesanan {pesanan} berhasil ditambahkan ke antrian.')

    def dequeue(self):
        if len(self.antrian) == 0:
            print('Antrian kosong.')
        else:
            pesanan = self.antrian.popleft()
            print(f'antrian {pesanan} telah diambil dari antrian.')
            if len(self.antrian) == 0:
                print('Antrian sekarang kosong.')
            else:
                if len(self.antrian) == 1:
                    print('Tidak ada antrian selanjutnya.')
                else:
                    print(f'antrian selanjutnya: {self.antrian[1]}')

    def lihat_antrian(self):
        if len(self.antrian) == 0:
            print('Antrian kosong.')
        else:
            print(f'Daftar antrian: {list(self.antrian)}')

def main():
    queue_system = QueueSystem()
    
    while True:
        print(f'\nJumlah Antrian: {len(queue_system.antrian)}')
        print("Pilihan: ")
        print("1. Tambah pesanan ")
        print("2. Ambil antrian")
        print("3. Lihat antrian")
        print("4. Keluar")

        pilihan = int(input('Pilih operasi (1, 2, 3, 4): '))
        if pilihan == 1:
            queue_system.enqueue()
        elif pilihan == 2:
            queue_system.dequeue()
        elif pilihan == 3:
            queue_system.lihat_antrian()
        elif pilihan == 4:
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-4.")

if __name__ == "__main__":
    main()
