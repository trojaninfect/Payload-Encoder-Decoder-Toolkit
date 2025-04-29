def run(mode, data):
    if mode == "encode":
        return data.encode('rot_13')  # Python doesn't have rot13, but you can implement it or use external libraries
    elif mode == "decode":
        return data.decode('rot_13')
    else:
        raise ValueError("Invalid mode")
