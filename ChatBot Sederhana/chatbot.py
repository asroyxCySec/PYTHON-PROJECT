def chatbot():
    print("Halo! Saya adalah chatbot sederhana.")
    print("Anda bisa bertanya hal-hal seperti:")
    print("- 'Apa kabar?'")
    print("- 'Siapa namamu?'")
    print("- 'Berapa umurmu?'")
    print("- 'Apa hobi kamu?'")
    print("- 'Keluar' untuk mengakhiri percakapan")

    while True:
        user_input = input("Anda: ").lower()

        if user_input == "apa kabar?":
            print("Chatbot: Saya baik, terima kasih! Bagaimana dengan Anda?")
        elif user_input == "siapa namamu?":
            print("Chatbot: Saya adalah chatbot sederhana.")
        elif user_input == "berapa umurmu?":
            print("Chatbot: Saya tidak memiliki umur, saya hanya kode.")
        elif user_input == "apa hobi kamu?":
            print("Chatbot: Hobi saya adalah membantu Anda dengan pertanyaan sederhana.")
        elif user_input == "keluar":
            print("Chatbot: Terima kasih telah berbicara dengan saya. Selamat tinggal!")
            break
        else:
            print("Chatbot: Maaf, saya tidak mengerti pertanyaan Anda.")

if __name__ == "__main__":
    chatbot()
