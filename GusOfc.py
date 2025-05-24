import os
import time

# Login
user = "GusOfc"
pw = "dream"

os.system("clear")
print("==== LOGIN GUSxOFC ====")
username = input("USERNAME: ")
password = input("PASSWORD: ")

if username != user or password != pw:
    print("Login Gagal!")
    exit()

# Animasi loading
for i in range(3):
    os.system("clear")
    print("Memuat GUSxOFC" + "." * i)
    time.sleep(0.5)

# Menu utama
while True:
    os.system("clear")
    print("""
\033[1;32m╔═══════════════════════════════╗
║     \033[1;31mGUSxOFC - Version 1.0\033[1;32m       ║
║     Owner: GUSxOFC             ║
║     Dibuat pada: 2025          ║
╚═══════════════════════════════╝
\033[0m
[1] Ambil Info Website
[2] Lagu Sad Vibes
[3] Track IP Address
[4] Doxin Nomor
[5] Track NIK KTP
[6] Mode Heker
[7] Ping - Cek IP Web
[8] Info IP Website (Wappalyzer)
[9] pantun Anak Goblog
[10] Ambil ID TikTok
[11] Banned ID TikTok
[0] Keluar
""")
    pilih = input("Pilih fitur >> ")

    if pilih == "1":
        domain = input("Masukkan domain (contoh: google.com): ")
        os.system(f"whois {domain} | head -n 30")

    elif pilih == "2":
        sad_lyrics = '''
Judul: Kehilangan - Firman

Aku harus jujur padamu tentang perasaanku
Terlalu lama aku memendam semua ini
Dan kini kau pergi, meninggalkan aku sendiri
Menyesal kini, ku tak pernah ungkapkan

Kau adalah yang terindah dalam hidupku
Tapi aku terlambat menyadarinya
Kini ku hanya bisa mengenang bayangmu
Dalam sepi dan air mata...
'''
        os.system("clear")
        for baris in sad_lyrics.splitlines():
            print(f"\033[1;35m{baris}\033[0m")
            time.sleep(1)

    elif pilih == "3":
        ip = input("Masukkan IP: ")
        os.system(f"curl -s https://ipinfo.io/{ip} | jq")

    elif pilih == "4":
        nomor = input("Masukkan Nomor (contoh: 08xxxx): ")
        os.system(f"curl -s https://api.zerobyte.id/dox?nomor={nomor}")

    elif pilih == "5":
        nik = input("Masukkan NIK KTP: ")
        os.system(f"curl -s https://api.zerobyte.id/ktp?nik={nik}")

    elif pilih == "6":
        os.system("clear")
        print("\033[1;32;40m")
        for i in range(100):
            print("GUSxOFC MODE GACOR, AWASI SYSTEM ANDA👿!")
            time.sleep(0.05)
        os.system("cmatrix")

    elif pilih == "7":
        host = input("Masukkan domain/IP: ")
        os.system(f"ping -c 4 {host}")

    elif pilih == "8":
        ip = input("Masukkan IP atau domain: ")
        print("Sedang mengambil info teknologi dari website...")
        os.system(f"curl -sL https://api.builtwith.com/free1/api.json?KEY=demo&LOOKUP={ip}")

    elif pilih == "9":
        os.system("clear")
        teks = "2 3 makan protokol - muka lu kayak kontol"
        for huruf in teks:
            print(huruf, end='', flush=True)
            time.sleep(0.1)
        print("\nSANTUN BOS!")

    elif pilih == "10":
        username = input("Masukkan username TikTok: ")
        os.system(f"curl -s https://api.zerobyte.id/tiktok?username={username}")

    elif pilih == "11":
        tiktok_id = input("Masukkan ID TikTok: ")
        print("Proses banned akun TikTok...")
        os.system(f"curl -X POST https://api.zerobyte.id/tiktok-ban -d 'id={tiktok_id}'")

    elif pilih == "0":
        print("Keluar...")
        break
    else:
        print("Pilihan tidak valid!")
    input("\nTekan ENTER untuk kembali...")
    
