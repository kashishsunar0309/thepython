import base64

def decode_pass(password):
    decoded_bytes = base64.b64decode(password)
    decoded_date = decoded_bytes.decode("utf-8")
    print(f"Decoded password: {decoded_date}")
    
    
encode_string = input("Enter your password: ")
decode_pass(encode_string)