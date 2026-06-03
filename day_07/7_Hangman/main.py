import random
import hangman_words
import hangman_art
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
print(hangman_art.logo)
#Testing Code
#print(f"Pssst, the soluttion is {chosen_word}.")

#Create blanks
display = []
for i in range(word_length):
    display.append("_")
while True:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("Already Guessed Earlier.")
        continue
    c=0
    #Check guessed letter
    for i in chosen_word:
        if i == guess:
            display[c]=guess
        c+=1
    #If user is worng
    if guess not in chosen_word:
        lives -= 1
        print("Wrong Guess.")
    #If user is right
    else:
        print("Correct Guess.")
    #Join all the elements in the list and turn it into a String.
    print(hangman_art.stages[lives])
    if lives == 0:
        print("You Lose!")
        break
    print(f"{' '.join(display)}")
    #Check if user has got all letters.
    if display.count("_") == 0:
        print("You Win!")
        break