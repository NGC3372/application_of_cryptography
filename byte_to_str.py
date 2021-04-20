import base64


def bytes_to_str(byte: bytes):
    b64 = base64.encodebytes(byte)
    s = bytes.decode(b64)
    return s


def str_to_bytes(s: str):
    b64 = str.encode(s)
    byte = base64.decodebytes(b64)
    return byte


