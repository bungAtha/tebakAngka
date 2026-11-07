import random


def tebakAngka():
    print("Ini adalah game tebak angka mulai dari angka 1 sampai 100")

    angka_rahasia = random.randint(1, 100)
    tebakan = 0
    jumlah_tebakan = 0

    while tebakan != angka_rahasia:
        try:
            tebakan = int(input("Masukkan angka anda : "))
            jumlah_tebakan += 1

            if tebakan < angka_rahasia:
                print("Angka anda terlalu rendah, Coba lagi!")
            elif tebakan > angka_rahasia:
                print("Angka anda terlalu besar, Coba lagi!")
            else:
                print(
                    f"Selamat Anda berhasil menebak angka {angka_rahasia} dari {jumlah_tebakan} percobaan"
                )
        except ValueError:
            print("Peringatan: Harap masukkan Angka yang sesuai!")


while True:
    tebakAngka()

    pilihan = input(
        "\nApakah Anda ingin bermain lagi? (Ketik 'y' untuk Ya, dan 't' untuk Tidak)"
    ).lower()

    if pilihan != "y":
        print("Terima Kasih telah bermain sampai jumpa!")
        break
