
import random 
user_guess =''

while user_guess not in ('head','tail'):
    print('Guess  coin toss - head or tail')
    user_guess = input()
# 0 is head, 1 is tail
value = random.randint(0,1)
if value == 0:
    toss = 'head'
else:
    toss = 'tail'
if toss == user_guess:
    print('You win')
else:
    print('You lose ! One more chance')
    user_guess = input()
    if toss == user_guess:
        print('You win')
    else:
        print('You lose !')