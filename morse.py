dictionary = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "Ą": ".-.-",
    "Ć": "—.—..",
    "Ę": "..—..",
    "Ł": ".—..—",
    "Ń": "——.——",
    "Ó": "———.",
    "Ś": "...—...",
    "Ż": "——..—.",
    "Ź": "——..—",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    " ": "",
    "\n": "\n"
}
rev_dict = {v: k for k, v in dictionary.items()}

def morse_coding(string, cipher):
    """Function to cipher or decipher a message from/into morse code. Put cipher=True to cipher into morse code."""
    if cipher:
        result = ""
        for i in range(len(string) - 1):
            result += dictionary[string[i]] + " "
        result += dictionary[string[len(string) - 1]]
        return (result)
    else:
        result = ""
        i = 0
        temp = ""
        while i <= len(string) - 2:
            if string[i] == string[i + 1] and string[i + 1] == " ":
                result += rev_dict[temp]
                i += 1
                result += " "
                temp = ""
            elif string[i] == " ":
                result += rev_dict[temp]
                temp = ""
            else:
                temp += string[i]
            i += 1
        temp += string[i]
        result += rev_dict[temp]
        return (result)

if __name__ == "__main__":
    print(morse_coding("HELLO WORLD",cipher=True))
    print(morse_coding(".... . .-.. .-.. ---  .-- --- .-. .-.. -..",cipher=False))
    print(morse_coding("PRZYKŁADOWE ZDANIE",cipher=True))
    print(morse_coding(".--. .-. --.. -.-- -.- .—..— .- -.. --- .-- .  --.. -.. .- -. .. .",cipher=False))