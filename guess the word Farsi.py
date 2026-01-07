import random

word_list = ["ایران", "ترکیه", "عراق", "هلند", "لبنان"]


def guess_the_word_farsi ():

    while True:

        Persian_letters = input("یک حرف وارد کنید: ")
        if len(Persian_letters) == 1 and 'ا' <= Persian_letters <= 'ی':

            return Persian_letters
        else:

            print("لطفاً یک حرف معتبر وارد کنید.")

def display_word(word,guess_the_word_farsi):
    displayed = "".join([Persian_letters if Persian_letters in
    guess_the_word_farsi else "_" for Persian_letters in word])
    print("کلمه: ", displayed)

    return displayed


def play_game():
    word = random.choice(word_list)
    Persian_letters = set( )
    attempts = 5

    print("بازی حدس کلمه را شروع کنید!")
    display_word(word, Persian_letters)

    while attempts > 0:
        letter = guess_the_word_farsi()

        if letter in word:

            Persian_letters.add(letter)
            print("حرف درست بود✔!")

        else:

            attempts -= 1
            print("حرف اشتباه بود❌!")
        displayed_word = display_word(word, Persian_letters)


        if "_" not in displayed_word:

            print("تبریک! شما کلمه را حدس زدی.")
            break

        print(f"تعداد حدس‌های باقی‌مانده: {attempts}")
    if attempts == 0:
        print(f"بازی تمام شد! کلمه مورد نظر '{word}' بود.")


play_game()