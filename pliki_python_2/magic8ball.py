##
import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'To pewne'
    elif answerNumber == 2:
        return 'Zdecydowanie tak'
    elif answerNumber == 3:
        return 'Tak'
    elif answerNumber == 4:
        return 'Bla bla bla'
    elif answerNumber == 5:
        return 'Bla bla '
    elif answerNumber == 6:
        return 'Bla'
    elif answerNumber == 7:
        return 'nic'
    elif answerNumber == 8:
        return 'jprdl'

r = random.randint(1,8)
print(getAnswer(r))

