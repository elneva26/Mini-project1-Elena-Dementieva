print("Nama: Elena Dementieva")
print("Kelas: Sistem Informasi 25 A")
print("NIM: 2509116008")
print("Mini Project 1 - Sistem Manajemen Jadwal Cougar Basketball Club")
print("="*80)

from datetime import datetime

# ===== Memvalidasi Waktu =====
def Tanggal_valid(s):
    try: datetime.strptime(s, "%d-%m-%Y"); return True
    except: return False

def Bulan_valid(s):
    try: datetime.strptime(s, "%m-%Y"); return True
    except: return False

def Waktu_valid(s):
    try:
        a, b = s.split("-")
        return datetime.strptime(a.strip(), "%H:%M") < datetime.strptime(b.strip(), "%H:%M")
    except: return False

# ===== Jadwal Utama =====

Jadwal = [
    ("15-09-2025","17:00-18:00","Latihan Fisik","Lapangan PKK"),
    ("16-09-2025","16:30-18:00","Latihan Skill","Lapangan Dispora"),
    ("17-09-2025","17:00-20:00","Pertandingan Fun game","Lapangan Dispora"),
    ("18-09-2025","16:30-18:00","Latihan Fisik","Gor Kadrie Oening"),
    ("19-09-2025","17:00-19:00","Latihan Skill","Lapangan Perbama"),
]

# ===== Menampilkan Jadwal =====
def tampilkan():
    print("======================= Jadwal Pelatihan dan Pertandingan ==========================")
    print(f"{'No':<1} | {'Tanggal':<10} | {'Waktu':<11} | {'Kegiatan':<20} | {'Lokasi':<20} ")
    print(f"{'-'*2}+{'-'*13}+{'-'*13}+{'-'*27}+{'-'*15}")

    print(f"{'1':<1} |  {Jadwal[0][0]:<5} | {Jadwal[0][1]:<8} | {Jadwal[0][2]:<10}          | {Jadwal[0][3]:<15}")
    print(f"{'2':<1} |  {Jadwal[1][0]:<5} | {Jadwal[1][1]:<8} | {Jadwal[1][2]:<10}          | {Jadwal[1][3]:<15}")
    print(f"{'3':<1} |  {Jadwal[2][0]:<5} | {Jadwal[2][1]:<8} | {Jadwal[2][2]:<10}  | {Jadwal[2][3]:<15}")
    print(f"{'4':<1} |  {Jadwal[3][0]:<5} | {Jadwal[3][1]:<8} | {Jadwal[3][2]:<10}          | {Jadwal[3][3]:<15}")
    print(f"{'5':<1} |  {Jadwal[4][0]:<5} | {Jadwal[4][1]:<8} | {Jadwal[4][2]:<10}          | {Jadwal[4][3]:<15}")
    print("-"*80)
    

# ======= Header: No |Tanggal | Waktu | Kegiatan | Lokasi =======
print(f"{'No':<1} | {'Tanggal':<9} | {'Waktu':<10} | {'Kegiatan':<25} | {'Lokasi':<20}")
print("-"*80)

print(f"1.| {Jadwal[0][0]} |{Jadwal[0][1]} | {Jadwal[0][2]}             |   {Jadwal[0][3]}")
print(f"2.| {Jadwal[1][0]} |{Jadwal[1][1]} | {Jadwal[1][2]}             |   {Jadwal[1][3]}")
print(f"3.| {Jadwal[2][0]} |{Jadwal[2][1]} | {Jadwal[2][2]}     |   {Jadwal[2][3]}")
print(f"4.| {Jadwal[3][0]} |{Jadwal[3][1]} | {Jadwal[3][2]}             |   {Jadwal[3][3]}")
print(f"5.| {Jadwal[4][0]} |{Jadwal[4][1]} | {Jadwal[4][2]}             |   {Jadwal[4][3]}")

#===== Mengubah Jadwal =====
def ubah(no):
    Jadwal=[
    ("20-09-2025","16:30-18:00","Latihan skill","Lapangan Dispora"),
    ("21-09-2025","16:00-17:00","Latihan fisik","Gor Kadrie Oening"),
    ("22-09-2025","17:00-20:00","Pertandingan Fun game","Lapangan PKK"),
    ("23-09-2025","16:30-18:00","Latihan skill","Lapangan Dispora"),
    ("24-09-2025","17:00-19:00","Latihan Fisik","Gor Sempaja"),
    ]

def tampilkan():
    print("\n=== Jadwal Pelatihan dan Pertandingan ===")
    print("="*80)
    print("No | Tanggal     | Waktu        | Kegiatan             | Lokasi")
    print("-- + ----------- + ------------ + ------------------- + -------------------")
    print(f"1  | {Jadwal[0][0]:<11} | {Jadwal[0][1]:<12} | {Jadwal[0][2]:<19} | {Jadwal[0][3]:<19}")
    print(f"2  | {Jadwal[1][0]:<11} | {Jadwal[1][1]:<12} | {Jadwal[1][2]:<19} | {Jadwal[1][3]:<19}")
    print(f"3  | {Jadwal[2][0]:<11} | {Jadwal[2][1]:<12} | {Jadwal[2][2]:<19} | {Jadwal[2][3]:<19}")
    print(f"4  | {Jadwal[3][0]:<11} | {Jadwal[3][1]:<12} | {Jadwal[3][2]:<19} | {Jadwal[3][3]:<19}")
    print(f"5  | {Jadwal[4][0]:<11} | {Jadwal[4][1]:<12} | {Jadwal[4][2]:<19} | {Jadwal[4][3]:<19}")
    print("-"*80)
def ubah(no):
    global Jadwal  # agar mengubah Jadwal global
    tgl = input("Masukkan tanggal (DD-MM-YYYY): ")
    wkt = input("Masukkan waktu (HH:MM-HH:MM): ")
    keg = input("Masukkan kegiatan: ")
    lok = input("Masukkan lokasi: ")

    if 1 <= no <= len(Jadwal):
        Jadwal[no-1] = (tgl, wkt, keg, lok)
    else:
        print("Nomor jadwal tidak ditemukan")

# ===== Menampilkan Jadwal Setelah di Ubah =====
print("=== Jadwal Awal ===")
tampilkan()

print("\n--- Jadwal Setelah Diubah ---")
tampilkan()
    
#===== Membuat Jadwal ======
def tambah(no):
    Jadwal=[
    ("20-09-2025","16:30-18:00","Latihan skill","Lapangan Dispora"),
    ("21-09-2025","16:00-17:00","Latihan fisik","Gor Kadrie Oening"),
    ("22-09-2025","17:00-20:00","Pertandingan Fun game","Lapangan PKK"),
    ("23-09-2025","16:30-18:00","Latihan skill","Lapangan Dispora"),
    ("24-09-2025","17:00-19:00","Latihan Fisik","Gor Sempaja"),
    ]
def tampilkan():
    print("\n=== Jadwal Pelatihan dan Pertandingan ===")
    print("="*80)
    print("No | Tanggal     | Waktu        | Kegiatan             | Lokasi")
    print("-- + ----------- + ------------ + ------------------- + -------------------")
    print(f"1  | {Jadwal[0][0]:<11} | {Jadwal[0][1]:<12} | {Jadwal[0][2]:<19} | {Jadwal[0][3]:<19}")
    print(f"2  | {Jadwal[1][0]:<11} | {Jadwal[1][1]:<12} | {Jadwal[1][2]:<19} | {Jadwal[1][3]:<19}")
    print(f"3  | {Jadwal[2][0]:<11} | {Jadwal[2][1]:<12} | {Jadwal[2][2]:<19} | {Jadwal[2][3]:<19}")
    print(f"4  | {Jadwal[3][0]:<11} | {Jadwal[3][1]:<12} | {Jadwal[3][2]:<19} | {Jadwal[3][3]:<19}")
    print(f"5  | {Jadwal[4][0]:<11} | {Jadwal[4][1]:<12} | {Jadwal[4][2]:<19} | {Jadwal[4][3]:<19}")
    print("-"*80)
def tambah(no):
    global Jadwal  # agar mengubah Jadwal global
    tgl = input("Masukkan tanggal (DD-MM-YYYY): ")
    wkt = input("Masukkan waktu (HH:MM-HH:MM): ")
    keg = input("Masukkan kegiatan: ")
    lok = input("Masukkan lokasi: ")

    if 1 <= no <= len(Jadwal):
        Jadwal[no-1] = (tgl, wkt, keg, lok)
    else:
        print("Nomor jadwal tidak ditemukan")

#==== Menampilkan Jadwal setelah ditambahkan ====
print("=== Jadwal Awal ===")
tampilkan()

print("\n--- Jadwal Setelah Ditambah ---")
tampilkan()

#===== Menghapus Jadwal =====
def hapus(no):
    Jadwal=("15-09-2025","17:00-18:00","Latihan Fisik","Lapangan PKK"),
    ("16-09-2025","16:30-18:00","Latihan Skill","Lapangan Dispora"),
    ("17-09-2025","17:00-20:00","Pertandingan Fun game","Lapangan Dispora"),
    ("18-09-2025","16:30-18:00","Latihan Fisik","Gor Kadrie Oening"),
    ("19-09-2025","17:00-19:00","Latihan Skill","Lapangan Perbama"),
def tampilkan():
    print("\n=== Jadwal Pelatihan dan Pertandingan ===")
    print("No | Tanggal      | Waktu        | Kegiatan              | Lokasi")
    print("-- + ------------ + ----------- + -------------------- + -------------------")
    
    if len(Jadwal) >= 1:
        print(f"1 | {Jadwal[0][0]:<11} | {Jadwal[0][1]:<11} | {Jadwal[0][2]:<20} | {Jadwal[0][3]:<20}")
    if len(Jadwal) >= 2:
        print(f"2 | {Jadwal[1][0]:<11} | {Jadwal[1][1]:<11} | {Jadwal[1][2]:<20} | {Jadwal[1][3]:<20}")
    if len(Jadwal) >= 3:
        print(f"3 | {Jadwal[2][0]:<11} | {Jadwal[2][1]:<11} | {Jadwal[2][2]:<20} | {Jadwal[2][3]:<20}")
    if len(Jadwal) >= 4:
        print(f"4 | {Jadwal[3][0]:<11} | {Jadwal[3][1]:<11} | {Jadwal[3][2]:<20} | {Jadwal[3][3]:<20}")
    if len(Jadwal) >= 5:
        print(f"5 | {Jadwal[4][0]:<11} | {Jadwal[4][1]:<11} | {Jadwal[4][2]:<20} | {Jadwal[4][3]:<20}")
        
def hapus(no):
    global Jadwal  # agar mengubah Jadwal global
    tgl = input("Masukkan tanggal (DD-MM-YYYY): ")
    wkt = input("Masukkan waktu (HH:MM-HH:MM): ")
    keg = input("Masukkan kegiatan: ")
    lok = input("Masukkan lokasi: ")

def hapus(no):
    global Jadwal
    if 1 <= no <= len(Jadwal):
        # Menghapus elemen sesuai nomor
        Jadwal.pop(no-1)
        print(f"\nJadwal nomor {no} berhasil dihapus.")
    else:
        print("\nNomor jadwal tidak ditemukan")

#==== Menampilkan Jadwal setelah dihapus ====
print("=== Jadwal Awal ===")
tampilkan()

print("\n--- Jadwal Setelah Dihapus ---")
tampilkan()

#===== Menu Utama =====
print("==== sistem manajemen jadwal cougar basketball club ====")
print("1. Lihat Jadwal")
print("2. Tambah Jadwal")
print("3. Ubah Jadwal")
print("4. Hapus Jadwal")
print("5. Keluar")

pilih = input("Pilih (1-5): ")
if pilih == "1":
    tampilkan()
elif pilih == "2":
    no = int(input("Pilih nomor jadwal (1-5) untuk ditambah/diisi: "))
    tambah(1)
    tampilkan()
elif pilih == "3":
    no = int(input("Pilih nomor jadwal (1-5) untuk diubah/diisi: "))
    ubah(1)
    tampilkan()
elif pilih == "4":
    no = int(input("Pilih nomor jadwal yang ingin dihapus:"))
    hapus(no)
    print("\n=== Jadwal setelah Dihapus ===")
    tampilkan()
elif pilih == "5":
    no = int(input("Yakin ingin keluar? (1=Ya, 2=Tidak): "))
else:
    print("Pilihan tidak valid.")

print("Terima kasih telah menggunakan sistem manajemen Cougar Basketball Club.")









