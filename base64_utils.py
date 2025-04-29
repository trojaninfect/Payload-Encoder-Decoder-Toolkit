import base64

def run(mode, data):
    if mode == "encode":
        return base64.b64encode(data.encode()).decode()
    elif mode == "decode":
        return base64.b64decode(data.encode()).decode()
    else:
        raise ValueError("Invalid mode")
