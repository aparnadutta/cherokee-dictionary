import sys

# Dictionary mapping syllabary to simple phonetics values.
simple_phone_dict = {'Ꭰ': 'a', 'Ꭱ': 'e', 'Ꭲ': 'i', 'Ꭳ': 'o',
                     'Ꭴ': 'u', 'Ꭵ': 'v', 'Ꭶ': 'ga', 'Ꭷ': 'ka',
                     'Ꭸ': 'ge', 'Ꭹ': 'gi', 'Ꭺ': 'go', 'Ꭻ': 'gu',
                     'Ꭼ': 'gv', 'Ꭽ': 'ha', 'Ꭾ': 'he', 'Ꭿ': 'hi',
                     'Ꮀ': 'ho', 'Ꮁ': 'hu', 'Ꮂ': 'hv', 'Ꮃ': 'la',
                     'Ꮄ': 'le', 'Ꮅ': 'li', 'Ꮆ': 'lo', 'Ꮇ': 'lu',
                     'Ꮈ': 'lv', 'Ꮉ': 'ma', 'Ꮊ': 'me', 'Ꮋ': 'mi',
                     'Ꮌ': 'mo', 'Ꮍ': 'mu', 'Ꮎ': 'na', 'Ꮏ': 'hna',
                     'Ꮐ': 'nah', 'Ꮑ': 'ne', 'Ꮒ': 'ni', 'Ꮓ': 'no',
                     'Ꮔ': 'nu', 'Ꮕ': 'nv', 'Ꮖ': 'gwa', 'Ꮗ': 'gwe',
                     'Ꮘ': 'gwi', 'Ꮙ': 'gwo', 'Ꮚ': 'gwu', 'Ꮛ': 'gwv',
                     'Ꮜ': 'sa', 'Ꮝ': 's', 'Ꮞ': 'se', 'Ꮟ': 'si',
                     'Ꮠ': 'so', 'Ꮡ': 'su', 'Ꮢ': 'sv', 'Ꮣ': 'da',
                     'Ꮤ': 'ta', 'Ꮥ': 'de', 'Ꮦ': 'te', 'Ꮧ': 'di',
                     'Ꮨ': 'ti', 'Ꮩ': 'do', 'Ꮪ': 'du', 'Ꮫ': 'dv',
                     'Ꮬ': 'dla', 'Ꮭ': 'tla', 'Ꮮ': 'tle', 'Ꮯ': 'tli',
                     'Ꮰ': 'tlo', 'Ꮱ': 'tlu', 'Ꮲ': 'tlv', 'Ꮳ': 'ja',
                     'Ꮴ': 'je', 'Ꮵ': 'ji', 'Ꮶ': 'jo', 'Ꮷ': 'ju',
                     'Ꮸ': 'jv', 'Ꮹ': 'wa', 'Ꮺ': 'we', 'Ꮻ': 'wi',
                     'Ꮼ': 'wo', 'Ꮽ': 'wu', 'Ꮾ': 'wv', 'Ꮿ': 'ya',
                     'Ᏸ': 'ye', 'Ᏹ': 'yi', 'Ᏺ': 'yo', 'Ᏻ': 'yu', 'Ᏼ': 'yv',
                     ' ': ' '}

# String representing vowel values of transliterated Cherokee.
vowels = 'aeiouv'


# Converts syllabary to transliterated simple phonetics.
def convert(syllabary: str):
    # translit is the string converted into simple phonetics
    translit = "".join([simple_phone_dict[char] for char in syllabary])
    final = []
    for i, letter in enumerate(translit):
        # Inserts a glottal stop between two vowels.
        if i != 0:
            if letter in vowels and translit[i - 1] in vowels:
                final.append('ʔ')
        final.append(letter)
    print("".join(final))


# Calls convert function on second command line element.
if __name__ == '__main__':
    convert(sys.argv[1])
