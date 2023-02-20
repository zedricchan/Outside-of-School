def shift_down(char):
    if char == 'z':
        return 'a'
    elif char.islower():
        return chr(ord(char)+1)
    else:
        return char

def encrypt(message, positions):
    encrypted_message = ''
    for char in message:
        encrypted_char = char
        for j in range(positions):
            encrypted_char = shift_down(encrypted_char)
        encrypted_message = encrypted_message + encrypted_char
    return encrypted_message

def shift_up(char):
    if char == 'a':
        return 'z'
    elif char.islower():
        return chr(ord(char)-1)
    else:
        return char

def decrypt(ciphertext, positions):
    decrypted_message = ''
    for char in ciphertext:
        decrypted_char = char
        for j in range(positions):
            decrypted_char = shift_up(decrypted_char)
        decrypted_message = decrypted_message + decrypted_char
    return decrypted_message

choice = ''
while choice != 'E' and choice != 'D':
    choice = (input("Please enter 'E' to encrypt or 'D' to decrypt: ")).upper()
text = input("Please enter the message or the ciphertext: ")
p = 'a'
while not p.isdigit():
    p = input("Please enter number of positions: ")
p = int(p)

if choice == 'E':
    print("The encrypted text is ' " + encrypt(text,p) + "'")
elif choice == 'D':
    print("The decrypted text is ' " + decrypt(text,p) + "'")
