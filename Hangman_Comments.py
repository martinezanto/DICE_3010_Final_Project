from Hangman import Hangman #Python will look in directory Hangman and import package named Hangman.
print("Welcome to Hangman!\n") #This is a print function that will show "Welcome to Hangman" when the game is first initialized.
play = input("Would you like to play a game? (y/N) ") #A input function is used here to ask the player if they would like to play a game. If the player wants to play game then type Y. If the the player does not, then type N.
if play.lower() != "y": #This is an if statement that checks if the user input is equal to y.
   print("Maybe later! Goodbye!") #If the input is not "Y", the message "Maybe Later! Goodbye!" will be printed on screen.
   exit() #This exit function exits the user from Python.
play_again = True #Once made past if statement, means that user wants to play. Which in this program is known as play_again. It is given value of TRUE to initiate game.
game = Hangman() # The variable Game is assigned the package Hangman() which contains the game itself.
game.initialize_file('words.dat') #The variable game use the "words.dat" file to collect words to use for the game.
while play_again and game.num_words_available > 0: #This is a while loop that executes a set of statements as long as a condition is true. In this case if the user is determined to play again from previous parts of program and their are words in the words.dat file, it will conduct this while loop.
   print("Starting game.") #In the case that this while loop is initiated, it will start by showing "Starting game." on screen.
   game.display_statistics() #This command tells the game which is the Hangman.py to dispay statistics about the game.
   print("\n") #This print function shows "/n" on the screen.
   game.new_word() #The variable game chooses a new number.
   while not game.game_over: #This is another while loop inside and already existing while loop. This while loop comes into effect when the game variable is not in the status of gameover it will run this loop.
      game.display_game() #In the case that the while loop is initiated, the game will display.
      user_guess = input("Enter a letter to guess. ") #The variable user_guess is assigned the value input, which is a function that asks the player to guess a letter.
      if not user_guess.isalpha(): #This is an if statement that checks to see if the value the player entered is a part of the alphabet.
         print("Sorry, I don't understand. That's not a letter. \n") #When the program has determined that the value is not alphabetical, it will use the print function to say on the game screen "Sorry, I don't understand. That's not a letter. \n".
      elif not game.guess(user_guess.upper()): #This elif statement is the next check in the program. Which is only done if the if statement above passes. This statement checks to see if the player has already chosen that letter.
         print("Sorry, you've alread guessed that letter. \n") #If the elif statement proves that that letter is already used, it will use a print function to post on the game screen "Sorry, you've alread guessed that letter. \n".
   game.reveal_word() #The variable game then reveals the word.
   game.display_statistics() #The variable game then shows the statistics for the most recent game. 
   game.game_over = False #The varibale game has its value set back to false.
   again = input("Would you like to play again? (y/N)") #The variable again is assigned an input function asking the user if they would like to play again.
   if again.lower() != "y": #This is a if statement that checks to see if the again variable is equal to Y.
      play_again = False #The game has recieved that the player does not want to play because the if statent did not find a Y.
   
print("Thanks for playing! Goodbye!") #A print function then displays "Thanks for playing! Goodbye!" on the game screen.
exit() #The program ends and eits out of Python.
