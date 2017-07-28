"""pew pew pew"""

import pyperclip

noBullets = pyperclip.paste()

noBulletsList = noBullets.split('\n')

bullets = []

for i, line in enumerate(noBulletsList):
    line = list(noBulletsList[i])
    line.insert(0, '* ')
    line = ''.join(line)
    bullets.append(line)

bullets = '\n'.join(bullets)

# print(bullets)

pyperclip.copy(bullets)

# * Lists of animals
# * Lists of aquarium life
# * Lists of biologists by author abbreviation
# * Lists of cultivars
