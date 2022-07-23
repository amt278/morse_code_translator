import time
from playsound import playsound

def play_morse_code(message):
    for c in message:
        if c == '.':
            playsound('shortMorse.wav')
            time.sleep(0.3)
        elif c == '-':
            playsound('longMorse.wav')
            time.sleep(0.3)
        else:
            time.sleep(0.5)


morse_code_dict = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-', ' ':'/'
}
reverse_dict = {v:k for k, v in morse_code_dict.items()}

message = 'adham'
message = " ".join(morse_code_dict[c] for c in message.upper())

morse_message = "".join(reverse_dict[c] for c in message.split(" "))

print(message)
print(morse_message)
play_morse_code(message)