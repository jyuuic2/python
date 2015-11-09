""""Find PI to the Nth Digit -
Enter a number and have the program generate PI up to that many decimal places.
Keep a limit to how far the program will go.
Written by Jay Yu at jyuuic2@gmail.com"""

import math

l=50
print('Friendly reminder: Enter 0 to '+ str(l) + ' only. Press q anytime to exit.')
p=input('For PI, How many decimal places would you like?')
c=1

while c:
    try:
        a=int(p)
    except ValueError:
        if p=='q' or p=='Q':
            print('You pressed q to exit. Good bye! See you next time~')
            break
        else:
            print('Not a valid number. Enter 0 to ' + str(l) + ' only. Press q anytime to exit.')
            p=input('For PI, How many decimal places would you like?')
            c=1
    else:
        if int(p)>l or int(p)<0:
            print('Number out of range. Enter 0 to ' + str(l) + ' only. Press q anytime to exit.')
            p=input('For PI, How many decimal places would you like?')
        else:
            b='{:.'+ str(p) + 'f}'
            print('PI = ' + b.format(math.pi))
            w=input('Very neat..., right? Press y to run it again. Press n or q to exit.')
            if w=='y' or w=='Y':
                c=1
                p=input('For PI, How many decimal places would you like?')
            elif w=='n' or w=='N' or w=='q' or w=='Q':
                c=0
                print('You pressed n or q to exit. Good bye! See you next time~')
            else:
                print('Not a valid entry. Auto-restarted. Enter 0 to ' + str(l) + ' only. Press q anytime to exit.')
                c=1
                p=input('For PI, How many decimal places would you like?')


