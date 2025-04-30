import argparse
import caesar
import morse


def main(args):
    with open (args.input_file, "r") as file:
        text = file.read()
    if args.code == "c":
        if args.option == "e":
            result = caesar.caesar_coding(text, args.n_lines, True)
        else:
            result = caesar.caesar_coding(text, args.n_lines, False)
    else:
        if args.option == "e":
            result = morse.morse_coding(text, True)
        else:
            result = morse.morse_coding(text, False)
    with open (args.output_file, "w") as file:
        file.write(result)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Description of the program")
    parser.add_argument("input_file", help="file to be read")
    parser.add_argument("output_file", help="file to save result")
    parser.add_argument("n_lines", type=int, default=3, nargs='?', help="Number of letters for the Ceasar cipher, default 3")
    parser.add_argument("-option", choices=["e", "d"], required=True, help="Choose an option: encryption or decryption")
    parser.add_argument("-code", choices=["c", "m"], required=True, help="Choose an option: Ceasar cipher or Morse code")
    args = parser.parse_args()
    main(args)