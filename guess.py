

user_word = ""
accurate_word = "asim"

limit = 4
count = 0

out_of_guesses = False

while (user_word != accurate_word ) and not (out_of_guesses):

    if count < limit :

        user_word = input("Guess the right word : \n ") 
        count = count + 1
    
    else :
        out_of_guesses = True

if out_of_guesses:
    print ("You are out of guesses")
else :
    print (" won")


