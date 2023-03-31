from colorama import init, Fore

# Inisialisasi colorama
init()

# Fungsi untuk membuat tabel
def tabel(listFilm):
    lebarNo = len(str(len(listFilm))) + 2
    lebarJudul = max(len(film[0]) for film in listFilm) + 2
    lebarSutradara = max(len(film[1]) for film in listFilm) + 2
    lebarJadwal = max(len(film[2]) for film in listFilm) + 2
    lebarAktor = max(len(film[3]) for film in listFilm) + 2

    # Header tabel dengan warna biru
    header = f"{Fore.BLUE}{'No':<{lebarNo}} | {'Judul Film':<{lebarJudul}} | {'Sutradara':<{lebarSutradara}} | {'Jadwal Tayang':<{lebarJadwal}} | {'Aktor Utama':<{lebarAktor}}{Fore.RESET}"
    separator = f"{'-' * lebarNo} | {'-' * lebarJudul} | {'-' * lebarSutradara} | {'-' * lebarJadwal} | {'-' * lebarAktor}"
    rows = []
    for index, film in enumerate(listFilm):
        row = f"{index+1:<{lebarNo}} | {film[0]:<{lebarJudul}} | {film[1]:<{lebarSutradara}} | {film[2]:<{lebarJadwal}} | {film[3]:<{lebarAktor}}"
        # Memberikan warna pada setiap baris data
        if index % 2 == 0:
            rows.append(f"{Fore.RESET}{row}")
        else:
            rows.append(f"{Fore.GREEN}{row}{Fore.RESET}")
    return '\n'.join([header, separator] + rows)


listFilm = []

while True:
    judulFilm = input("Masukkan Judul Film: ")
    sutradara = input("Masukkan Nama Sutradara: ")
    jadwalTayang = input("Masukkan Jadwal Tayang: ")
    aktorUtama = input("Masukkan Aktor Utama: ")

    dataFilm = [judulFilm, sutradara, jadwalTayang, aktorUtama]
    listFilm.append(dataFilm)

    # Menampilkan tabel
    print(tabel(listFilm))

    # Validasi input
    while True:
        pilihan = input("\nApakah anda ingin menginput data lagi? (y/n)\n")
        if pilihan == "y" or pilihan == "n":
            break
        else:
            print("Input tidak valid, silahkan masukkan 'y' atau 'n'")

    if pilihan == "n":
        break
