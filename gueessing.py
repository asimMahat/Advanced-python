
user_word = ""
exact_word = "coding"

count = 0
limit = 3
out_of_guesses = False

while user_word != exact_word and not(out_of_guesses):
    if count < limit :
        user_word = input(" Guess the right word : \n")
        count = count +1 
    
    else  :
        out_of_guesses =True

         

if out_of_guesses:
    print("you are out of guesses")
else :
    print ("you have won")




