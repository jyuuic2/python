""""
If running tarot cards works for you,
    then it must be magic.
Magic has its cost.
    So, be ready.
Only if you run very few times a day,
    if only it works,
        then it will work.
Else,
    it just will not work, not for you.
In another word:
    If you run many times a day,
        then it will not work.
    If it does not work for you,
        then it just will not work, not for you.
So, while the magic embraces you,
        embrace the magic.
    Else,
        move on,
        find magic elsewhere...
Written by Jay Yu at jyuuic2@gmail.com
"""

import datetime
import random

preface = '''If running tarot cards works for you,
    then it must be magic.
Magic has its cost.
    So, be ready.
Only if you run very few times a day,
    if only it works,
        then it will work.
Else,
    it just will not work, not for you.
In another word:
    If you run many times a day,
        then it will not work.
    If it does not work for you,
        then it just will not work, not for you.
So, while the magic embraces you,
        embrace the magic.
    Else,
        move on,
        find magic elsewhere...'''

print(preface)

#numbers of major arcana's
n_major_arcana = 22
n_minor_arcana_cups = 14
n_minor_arcana_pentacles = 14
n_minor_arcana_swords = 14
n_minor_arcana_wands = 14

#abbreviations
nma = n_major_arcana
nmac = n_minor_arcana_cups
nmap = n_minor_arcana_pentacles
nmas = n_minor_arcana_swords
nmaw = n_minor_arcana_wands
nmaa = nmac+nmap+nmas+nmaw
n_minor_arcana_all = nmaa
nmm = nma + nmaa

print('''
Introduction:

Tarot cards are:
    ''' + str(nma) + ''' Major Arcana cards
    ''' + str(nmaa) + ''' Minor Arcana cards, are:
        ''' + str(nmac) + ''' Cups
        ''' + str(nmap) + ''' Pentacles
        ''' + str(nmas) + ''' Swords
        ''' + str(nmaw) + ''' Wands
Total:  ''' + str(nmm) + ''' cards''')

print('''Here we use all the cards in reversed position too. So, total: ''' + str(nmm*2) + ''' cards''')

print('''
Firstly,    key in what you want to know, such as 'tarot cards and me'. Do NOT press ENTER yet.
Next,       take a moment to think in your mind, and/or pray.
Next,       press ENTER. The result will show instantly.''')

r = 'Reversed'
s1 = 'Cups'
s2 = 'Pentacles'
s3 = 'Swords'
s4 = 'Wands'

deck = {1: 'The Fool',
        2: 'The Fool, ' + r,
        3: 'The Magician',
        4: 'The Magician, ' + r,
        5: 'The High Priestess',
        6: 'The High Priestess, ' + r,
        7: 'The Empress',
        8: 'The Empress, ' + r,
        9: 'The Emperor',
        10: 'The Emperor, ' + r,
        11: 'The Hierophant',
        12: 'The Hierophant, ' + r,
        13: 'The Lovers',
        14: 'The Lovers, ' + r,
        15: 'The Chariot',
        16: 'The chariot, ' + r,
        17: 'Strength',
        18: 'Strength, ' + r,
        19: 'The Hermit',
        20: 'The Hermit, ' + r,
        21: 'Wheel of Fortune',
        22: 'Wheel of Fortune, ' + r,
        23: 'Justice',
        24: 'Justice, ' + r,
        25: 'The Hanged Man',
        26: 'The Hanged Man, ' + r,
        27: 'Death',
        28: 'Death, ' + r,
        29: 'Temperance',
        30: 'Temperance, ' + r,
        31: 'The Devil',
        32: 'The Devil, ' + r,
        33: 'The Tower',
        34: 'The Tower, ' + r,
        35: 'The Star',
        36: 'The Star, ' + r,
        37: 'The Moon',
        38: 'The Moon, ' + r,
        39: 'The Sun',
        40: 'The Sun, ' + r,
        41: 'Judgement',
        42: 'Judgement, ' + r,
        43: 'The World',
        44: 'The World, ' + r,
        45: s1 + ' 1',
        46: s1 + ' 1, ' + r,
        47: s1 + ' 2',
        48: s1 + ' 2, ' + r,
        49: s1 + ' 3',
        50: s1 + ' 3, ' + r,
        51: s1 + ' 4',
        52: s1 + ' 4, ' + r,
        53: s1 + ' 5',
        54: s1 + ' 5, ' + r,
        55: s1 + ' 6,',
        56: s1 + ' 6, ' + r,
        57: s1 + ' 7',
        58: s1 + ' 7, ' + r,
        59: s1 + ' 8',
        60: s1 + ' 8, ' + r,
        61: s1 + ' 9',
        62: s1 + ' 9, ' + r,
        63: s1 + ' 10',
        64: s1 + ' 10, ' + r,
        65: s1 + ' Page',
        66: s1 + ' Page, ' + r,
        67: s1 + ' Knight',
        68: s1 + ' Knight, ' + r,
        69: s1 + ' Queen',
        70: s1 + ' Queen, ' + r,
        71: s1 + ' King',
        72: s1 + ' King, ' + r,
        73: s1 + ' 1',
        74: s2 + ' 1, ' + r,
        75: s2 + ' 2',
        76: s2 + ' 2, ' + r,
        77: s2 + ' 3',
        78: s2 + ' 3, ' + r,
        79: s2 + ' 4',
        80: s2 + ' 4, ' + r,
        81: s2 + ' 5',
        82: s2+ ' 5, ' + r,
        83: s2 + ' 6,',
        84: s2 + ' 6, ' + r,
        85: s2 + ' 7',
        86: s2 + ' 7, ' + r,
        87: s2 + ' 8',
        88: s2 + ' 8, ' + r,
        89: s2 + ' 9',
        90: s2 + ' 9, ' + r,
        91: s2 + ' 10',
        92: s2 + ' 10, ' + r,
        93: s2 + ' Page',
        94: s2 + ' Page, ' + r,
        95: s2 + ' Knight',
        96: s2 + ' Knight, ' + r,
        97: s2 + ' Queen',
        98: s2 + ' Queen, ' + r,
        99: s2 + ' King',
        100: s2 + ' King, ' + r,
        101: s3 + ' 1',
        102: s3 + ' 1, ' + r,
        103: s3 + ' 2',
        104: s3 + ' 2, ' + r,
        105: s3 + ' 3',
        106: s3 + ' 3, ' + r,
        107: s3 + ' 4',
        108: s3 + ' 4, ' + r,
        109: s3 + ' 5',
        110: s3 + ' 5, ' + r,
        111: s3 + ' 6,',
        112: s3 + ' 6, ' + r,
        113: s3 + ' 7',
        114: s3 + ' 7, ' + r,
        115: s3 + ' 8',
        116: s3 + ' 8, ' + r,
        117: s3 + ' 9',
        118: s3 + ' 9, ' + r,
        119: s3 + ' 10',
        120: s3 + ' 10, ' + r,
        121: s3 + ' Page',
        122: s3 + ' Page, ' + r,
        123: s3 + ' Knight',
        124: s3 + ' Knight, ' + r,
        125: s3 + ' Queen',
        126: s3 + ' Queen, ' + r,
        127: s3 + ' King',
        128: s3 + ' King, ' + r,
        129: s4 + ' 1',
        130: s4 + ' 1, ' + r,
        131: s4 + ' 2',
        132: s4 + ' 2, ' + r,
        133: s4 + ' 3',
        134: s4 + ' 3, ' + r,
        135: s4 + ' 4',
        136: s4 + ' 4, ' + r,
        137: s4 + ' 5',
        138: s4 + ' 5, ' + r,
        139: s4 + ' 6,',
        140: s4 + ' 6, ' + r,
        141: s4 + ' 7',
        142: s4 + ' 7, ' + r,
        143: s4 + ' 8',
        144: s4 + ' 8, ' + r,
        145: s4 + ' 9',
        146: s4 + ' 9, ' + r,
        147: s4 + ' 10',
        148: s4 + ' 10, ' + r,
        149: s4 + ' Page',
        150: s4 + ' Page, ' + r,
        151: s4 + ' Knight',
        152: s4 + ' Knight, ' + r,
        153: s4 + ' Queen',
        154: s4 + ' Queen, ' + r,
        155: s4 + ' King',
        156: s4 + ' King, ' + r
        }
#print(deck[156])

q = input('What do you want to know? (Press q to exit)')
dt = datetime.datetime.now()
#print(dt)
me = 'jyuuic2@gmail.com'
c = 1

while c:
    if q == 'q' or q == 'Q':
        print('You pressed q to exit. Good bye! See you next time~')
        break
    else:
        print('''The results are:''')
        p1 = str(dt) + ' via ' + me + ' to know: ' + q  # a unique string
        p2 = ''.join(str(ord(p11)) for p11 in p1)  # convert string to ascii, unique
        p3 = int(p2)  # convert ascii to int, unique
        p4 = random.randint(1, p3)  # generate a random number within the range
        p_b = (p4 % 156) + 1  # generate a number between 1 and 156 from it, as base card, can be reused in deck
        p_p = (random.randint(1, p3) % 156) + 1  # past card, both positions, can not be reused in deck
        p_c = (random.randint(1, p3) % 156) + 1  # current/present card, both positions, can not be reused in deck
        while p_c == p_p or p_c == (p_p + 1) or (p_c + 1) == p_p:
            p_c = (random.randint(1, p3) % 156) + 1
        p_f = (random.randint(1, p3) % 156) + 1  # future card, end
        while p_f == p_c or p_f == (p_c + 1) or (p_f + 1) == p_c or p_f == p_p or p_f == (p_p + 1) or (p_f + 1) == p_p:
            p_f = (random.randint(1, p3) % 156) + 1
        print('Base (shadow) card: ' + deck[p_b])
        print('The Past: ' + deck[p_p])
        print('The Present: ' + deck[p_c])
        print('The Future: ' + deck[p_f])
        g = input('Very neat..., right? Press y to run it again. Press n or q to exit.')
        if g == 'y' or g == 'Y':
            c = 1
            q = input('What do you want to know? (Press q to exit)')
        elif g == 'n' or g == 'N' or g == 'q' or g == 'Q':
            c = 0
            print('You pressed n or q to exit. Good bye! See you next time~')
        else:
            print('Not a valid entry. Auto-restarted.')
            c = 1
            q = input('What do you want to know? (Press q to exit)')
