byte_string = b'Hello \xff World'  # Byte sequence with invalid UTF-8 character
try:
    decoded_string = byte_string.decode('utf-8')
    print("Decoded string:", decoded_string)
except UnicodeDecodeError as e:
    print("Error decoding byte string:", e)
