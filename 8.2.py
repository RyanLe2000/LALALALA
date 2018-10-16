def main():
    digits = ['0', '1', '2', 'A', 'B', 'C', '3', 'D', 'E', 'F', '4', 'G', 'H', 'I', '5', 'J', 'K', 'L', '6', 'M', 'N',
         'O', '7', 'P', 'Q', 'R', 'S', '8', 'T', 'U', 'V', '9', 'W', 'X', 'Y', 'Z', '-']

    alpha = ['0', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5',
          '6', '6', '6', '6', '7', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '9', '-']

    phrase = input(' input word to be chiphered ')
    print(len(phrase))
    alpha_final = ""
    for letter in phrase:
        for item in range(0, len(digits)):
            if letter.upper() == digits[item]:
                alpha_final += (alpha[item] + " ")


    print(alpha_final)
main()
