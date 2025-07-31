import random
import time

def game_mengingat_100_kartu():
    
    kartu_list = [i+1 for i in range(100)]  
    
    random.shuffle(kartu_list)
    
    print("Selamat datang di permainan Menghafal 100 Kartu!")
    print("Saya akan menunjukkan 100 kartu selama 1 menit.")
    print("Berikut kartu yang muncul:")
    
    for kartu in kartu_list:
        print(f'Kartu {kartu}')
    
    print("\nKartu akan hilang dalam 1 menit...")
    time.sleep(60)
    
    print("\033c", end="") 
    
    print("Kartu telah hilang. Sekarang, pilih kartu yang Anda ingat.")
    print("Masukkan nomor kartu yang Anda ingat (pisahkan dengan koma, misal: 1, 5, 10, ...):")

    tebakan = input("Masukkan daftar nomor kartu yang Anda ingat: ")
    
    try:
        tebakan_list = [int(tebak.strip()) for tebak in tebakan.split(',')]
    except ValueError:
        print("Input tidak valid. Harap masukkan hanya nomor yang valid.")
        return
    
    benar = set(tebakan_list) & set(kartu_list)  
    
    print(f"\nTebakan Anda: {', '.join(map(str, tebakan_list))}")
    print(f"Kartu yang benar: {', '.join(map(str, benar))}")
    print(f"\nAnda mengingat {len(benar)} kartu dengan benar!")
    
    if len(benar) == len(kartu_list):
        print("Selamat! Anda mengingat semua kartu dengan benar!")
    else:
        print("Coba lagi, Anda bisa lebih baik!")

game_mengingat_100_kartu()
