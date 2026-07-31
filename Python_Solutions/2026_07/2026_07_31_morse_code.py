def decode_morse(code):

    def encode_word(word):
        return "".join([morse_code[c] for c in word.split()])

    morse_code = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z"
    }

    return " ".join([encode_word(w) for w in code.split("   ")])

# print(decode_morse("--.."))
# print(decode_morse("... --- ..."))
# print(decode_morse("..-. .-. . . -.-. --- -.. . -.-. .- -- .--."))
# print(decode_morse(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."))
# print(decode_morse("- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. . -..   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --."))