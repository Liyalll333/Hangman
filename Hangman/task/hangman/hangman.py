import random

print("H A N G M A N  # 8 attempts")
print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
action = input()
win = 0
loose = 0

while action != 'exit':

    if action == 'play':
        list_of_words = ["python", "java", "swift", "javascript"]
        random_choices = list_of_words[random.randrange(0, 4)]
        user_attempts = 8
        a_word_to_guess = list(random_choices)
        list_with_lettrs = ["-" for _ in range(len(a_word_to_guess))]
        marker = ""
        tries = list()
        while user_attempts > 0:
            print()

            print("".join(list_with_lettrs))
            user_inp = input("Input a letter: ")

            if len(user_inp) != 1:
                print('Please, input a single letter.')
                tries.append(user_inp)
                continue

            if not user_inp.isalpha() or not user_inp.islower() or not user_inp.isalnum():
                print('Please, enter a lowercase letter from the English alphabet.')
                tries.append(user_inp)
                continue

            if user_inp in list_with_lettrs or user_inp in tries:
                print("You've already guessed this letter.")

            for chr in range(len(a_word_to_guess)):
                if a_word_to_guess[chr] == user_inp:
                    list_with_lettrs[chr] = user_inp

                    if list_with_lettrs.count(list_with_lettrs[chr]) == 1:
                        marker = "Yes"

            if not user_inp in a_word_to_guess:
                user_attempts -= 1
                tries.append(user_inp)
                print(f"# {user_attempts} attempts That letter doesn't appear in the word.")

            if list_with_lettrs == a_word_to_guess:
                win += 1
                print()
                print(f"\nYou guessed the word {random_choices}!\nYou survived!".format("".join(list_with_lettrs)))
                print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
                action = input()
                break

            elif user_attempts == 0:
                if a_word_to_guess == list_with_lettrs:
                    win += 1
                    print()
                    print(f"\nYou guessed the word {random_choices}!\nYou survived!".format("".join(list_with_lettrs)))
                    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
                    action = input()
                else:
                    loose += 1
                    print("\nYou lost!")
                    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
                    action = input()

    if action == 'results':
        print(f'You won: {win} times.')
        print(f'You lost: {loose} times.')
        print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
        action = input()


