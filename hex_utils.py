def run(mode, data):
    if mode == "encode":
        return data.encode().hex()
    elif mode == "decode":
        return bytes.fromhex(data).decode()
    else:
        raise ValueError("Invalid mode")
