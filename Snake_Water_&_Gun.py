import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        if you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        if you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        if you == 'w':
            return True
    pass

print("Computer Turn: Snake(s) Water(w) or Gun(g) ?")

r = random.randint(1,3)

if r == 1:
    comp = 's'
elif r == 2:
    comp = 'w'
elif r == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g) ?")

print(f"Computer Choose {comp}")
print(f"Your Choose {you}")

game = gamewin(comp,you)

if game == None:
    print("Game is Tie!!")
elif game:
    print("You Win! ")
else:
    print("You Lose! ")
