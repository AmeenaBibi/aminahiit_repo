def decode_message(encoded_message):
    rev_message = encoded_message[::-1]
    message = ""

    for i in rev_message:
        if i.isalpha() or i.isspace():
            message += i

    return message

encoded_message = input("Enter message to decode: ")
hidden_message = decode_message(encoded_message)
print("Decoded message: ", hidden_message)