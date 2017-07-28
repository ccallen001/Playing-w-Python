"""classy songs"""

def spaces(stuff):
    """@decorator"""
    print('')
    print(stuff)
    print('')

class Song(object):
    """song class"""

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        """sing it"""

        spaces('\n'.join(self.lyrics))


    def backwards(self):
        for line in self.lyrics[::-1]:
            print(line)

hbd_lyrics = [
    'Happy Bday to you',
    'happy Bday to you',
    'oh happy Bday to you!'
]

happy_birthday = Song(hbd_lyrics)

print(isinstance(happy_birthday, Song))

happy_birthday.backwards()

fuck_it = Song([
    'fuck this shit',
    'fuck it all',
    'fuck all this shit'
])

fuck_it.sing()
