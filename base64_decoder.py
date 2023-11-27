import base64
def encode_to_base64(words):
    encoded_words = [base64.b64encode(word.encode()).decode() for word in words]
    return encoded_words

def main(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            words = [line.strip() for line in file.readlines()]

        encoded_words = encode_to_base64(words)

        with open(output_file, 'w') as file:
            for encoded_word in encoded_words:
                file.write(encoded_word + '\n')

        print(f"Encoding successful. Results written to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_file = "input.txt"  # Replace with your input file path
    output_file = "output.txt"  # Replace with your desired output file path

    main(input_file, output_file)
