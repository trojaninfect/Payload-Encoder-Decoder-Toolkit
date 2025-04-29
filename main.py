import argparse
from encoders import base64_utils, hex_utils, rot_utils, custom

def encode_file(input_file, output_file, encoding_type, key=None):
    with open(input_file, 'r') as file:
        data = file.read()
    
    if encoding_type == 'base64':
        result = base64_utils.run('encode', data)
    elif encoding_type == 'hex':
        result = hex_utils.run('encode', data)
    elif encoding_type == 'rot13':
        result = rot_utils.run('encode', data)
    elif encoding_type == 'xor' and key:
        result = custom.xor_cipher(data, key, mode='encode')
    else:
        raise ValueError("Unsupported encoding type or missing key for XOR.")

    with open(output_file, 'w') as file:
        file.write(result)

def decode_file(input_file, output_file, encoding_type, key=None):
    with open(input_file, 'r') as file:
        data = file.read()
    
    if encoding_type == 'base64':
        result = base64_utils.run('decode', data)
    elif encoding_type == 'hex':
        result = hex_utils.run('decode', data)
    elif encoding_type == 'rot13':
        result = rot_utils.run('decode', data)
    elif encoding_type == 'xor' and key:
        result = custom.xor_cipher(data, key, mode='decode')
    else:
        raise ValueError("Unsupported encoding type or missing key for XOR.")

    with open(output_file, 'w') as file:
        file.write(result)

def main():
    parser = argparse.ArgumentParser(description="Payload Encoder/Decoder Toolkit")
    parser.add_argument("mode", choices=["encode", "decode"], help="Mode: encode or decode")
    parser.add_argument("type", choices=["base64", "hex", "rot13", "xor"], help="Encoding type")
    parser.add_argument("data", help="Input string or file path")
    parser.add_argument("--key", help="Key (required for XOR)", default=None)
    parser.add_argument("--file", action="store_true", help="Indicate if you are encoding/decoding a file")

    args = parser.parse_args()

    if args.file:
        # File handling
        if args.mode == "encode":
            encode_file(args.data, "encoded_output.txt", args.type, args.key)
            print(f"Encoded file saved to 'encoded_output.txt'")
        elif args.mode == "decode":
            decode_file(args.data, "decoded_output.txt", args.type, args.key)
            print(f"Decoded file saved to 'decoded_output.txt'")
    else:
        # String handling
        if args.type == "base64":
            result = base64_utils.run(args.mode, args.data)
        elif args.type == "hex":
            result = hex_utils.run(args.mode, args.data)
        elif args.type == "rot13":
            result = rot_utils.run(args.mode, args.data)
        elif args.type == "xor":
            if not args.key:
                raise ValueError("XOR encoding requires --key argument.")
            result = custom.xor_cipher(args.data, args.key, mode=args.mode)

        print(result)

if __name__ == "__main__":
    main()
