def xor_cipher(data, key, mode='encode'):
    if mode == 'decode':  # XOR decode is identical to encode
        return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))
    elif mode == 'encode':  # XOR encode
        return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))
    else:
        raise ValueError("Invalid mode. Use 'encode' or 'decode'.")
