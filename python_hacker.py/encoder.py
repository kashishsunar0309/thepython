import base64

def user(password):
    encoding_text = base64.b64encode(password.encode())
    print(encoding_text.decode())
    
user_password = input("Enter the password: ")
user(user_password)