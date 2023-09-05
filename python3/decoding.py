# def decode_message(encoded_message):
#     rev_message = encoded_message[::1]
#     message = "".join(i for i in rev_message if i.isalpha() or i.isspace())

#     print("Decoded message: ", message)
# encoded_message = input("Enter message to decode: ")
# decode_message(encoded_message)

def encode_message(code):
    flipped = code[::-1]
    message = ""

    for i in flipped:
        if i.isalpha() or i == "":
            message += i
            return encode_message