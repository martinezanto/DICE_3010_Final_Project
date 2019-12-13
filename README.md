# DICE_3010_Final_Project
This is my attempt at making a Twitter Bot
This is my .py code, I have tried it on pythonanywhere.com but it does not seem to work. There is an error when using the keys and secrets
to access Twitter. I am thinking it may because I did not use Tweepy. I installed Tweepy at the beginning of program, but when trying the
tweepy way of accessing developer account it did not work. So I tried this way and it still did not work. I think it may be because I am 
unsure how to assign twitter an API in the way it wants for the program to run.

First you have to import the pip files mentioned in the .txt file.
Each time you run this code, it was suppose to be done manually not automated on a timer. I did not want to spam everyone indefinately.
After importing pip files change directory to the Final_Project.py in Bash
then type python3 Final_Project.py to run program
After that there should be no other human interaction, if the program worked it would do it on its own.

It would get access to Twitter through the keys and secrets obtained from the developer account access.
A function is then defined to do a search.
Then a general search for the term "#teamapple", shows the most recent tweets witht the term "#teamapple".
The program then queues them and begins a for loop through one tweet at a time.
The program then favorites status, sends friend request, and then posts a reply to their tweet saying "ueser name", "Check out these Apples!"
With a link to a Google Images Search of apples
