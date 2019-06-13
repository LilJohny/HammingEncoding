from encoding import Encoder


def main():
    encoder = Encoder()
    message = input("Type message to encode: ")
    encoded_message, encoding_table = encoder.encode_message(message)
    print("Encoding table :")
    print(encoding_table)
    print("Encoded message :")
    print(encoded_message)


if __name__ == "__main__":
    main()
