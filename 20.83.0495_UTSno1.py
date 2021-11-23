import random

print('=' * 40)
print('Silahkan tebak angka antara 1 - 100 !')
print('=' * 40)

while True:
    angka = random.randint(1, 100)
    percobaan = int(input("Berapa kali Anda akan menebak : "))
    for i in range(percobaan):
        jawaban = int(input("\nMasukkan angka tebakan Anda :"))
        if jawaban == angka:
            print("Selamat, tebakanmu benar !")
            break
        elif jawaban > angka and jawaban < 101:
            print("Tebakan terlalu besar !")
        elif jawaban < angka and jawaban > 0:
            print("Tebakan terlalu kecil !")
        else :
            print("Jawaban tidak valid")
    else :
        print("\nSayang sekali, kamu sudah salah menebak sebanyak ",percobaan, " kali")
        print("Tebakan yang benar adalah : ",angka)
    menu = input("\nApakah akan mengulang permainan (y/n) ? ")
    if menu == "y" or menu == "Y":
        continue
    else:
        break
