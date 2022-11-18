alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def encode(text, shift):
    encoded_text = ""
    alpha_len = len(alphabet) - 1
    for t in text:
        if (alphabet.__contains__(t)):
            index = alphabet.index(t)
            new_shift_index = int(index + shift)
            if (new_shift_index > alpha_len):
                new_shift_index = new_shift_index - alpha_len - 1
            encoded_text += alphabet[new_shift_index]
        else:
            encoded_text += t
    print(f"Here's the encoded result: {encoded_text}")
    again = input("Do you want to continue again ? Type yes or no \n")
    if again.lower() == 'yes':
        tryAgain()


def decode(text, shift):
    decoded_text = ""
    for t in text:
        if (alphabet.__contains__(t)):
            index = alphabet.index(t)
            new_shift_index = int(index - shift)
            decoded_text += alphabet[new_shift_index]
        else:
            decoded_text += t
    print(f"Here's the encoded result: {decoded_text}")
    again = input("Do you want to continue again ? Type yes or no \n")
    if again.lower() == 'yes':
        tryAgain()


def goEncode():
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encode(text, shift)


def goDecode():
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decode(text, shift)


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")


def tryAgain():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode':
        goEncode()
    elif direction == 'decode':
        goDecode()


if direction == 'encode':
    goEncode()
elif direction == 'decode':
    goDecode()

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
