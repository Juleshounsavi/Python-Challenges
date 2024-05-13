#Game of guessing the mystery number.

print("This is a game between two people, when the Player 1 will enter a certain number and the Player 2 will try to guess it to win. Player 2 just have five trials.")

num=int(input("Player 1, enter your mystery number:"))

num_bl=num-10
num_br=num+100
print("Player 2, try to guess the Player 1 number which is between {} and {}".format(num_bl,num_br))


for i in range(5):
    guess=int(input("Player 2, enter your answer:"))
    if guess == num:
        print("You wiiiiiiin!")
        break
    else:
        print("Fail, try again.")
    
