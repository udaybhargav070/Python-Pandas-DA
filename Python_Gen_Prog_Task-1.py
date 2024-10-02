
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ' ': '   '}

def morse_code_decoder(morse_code):
    morse_code = morse_code.split('   ')
    decoded_message = ''

    for word in morse_code:
        letters = word.split(' ')
        for letter in letters:
            for key, value in MORSE_CODE_DICT.items():
                if letter == value:
                    decoded_message += key
                    break
        decoded_message += ' '

    return decoded_message.rstrip()

# Example usage:
morse_code_input = '.- -   -.. .- .-- -.   .-.. --- --- -.-   - ---   - .... .   . .- ... -'
decoded_message = morse_code_decoder(morse_code_input)
print(decoded_message)
