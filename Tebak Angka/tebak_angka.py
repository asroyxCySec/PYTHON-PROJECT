import random #menggunakan modul random untuk memilih angka

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    number_of_attempts = 0
    guessed = False

    print("Selamat datang di Game Tebak Angka!")
    print("Saya telah memilih sebuah angka antara 1 dan 100.")
    print("Cobalah tebak angka tersebut.")

    while not guessed:
        guess = input("Masukkan tebakan Anda: ")
        
        try:
            guess = int(guess)
            number_of_attempts += 1

            if guess < number_to_guess:
                print("Tebakan Anda terlalu rendah. Coba lagi.")
            elif guess > number_to_guess:
                print("Tebakan Anda terlalu tinggi. Coba lagi.")
            else:
                guessed = True
                print(f"Selamat! Anda telah menebak angka yang benar dalam {number_of_attempts} kali percobaan.")
        except ValueError:
            print("Harap masukkan angka yang valid.")

if __name__ == "__main__":
    guess_the_number()

