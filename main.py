import random
import string

def generate_key():
    alphabet = list(string.ascii_lowercase)
    shuffled = random.sample(alphabet, len(alphabet))
    key = dict(zip(alphabet, shuffled))
    reverse_key = {v: k for k, v in key.items()}
    return key, reverse_key

def clean_text(text, remove_spaces=False):
    if remove_spaces:
        cleaned_text = ''.join([char.lower() for char in text if char.isalpha()])  
    else:
        cleaned_text = ''.join([char.lower() for char in text if char.isalpha() or char == ' '])  
    return cleaned_text

def encrypt(plaintext, key):
    return ''.join(key.get(char.lower(), char) for char in plaintext)


def decrypt(ciphertext, reverse_key):
    return ''.join(reverse_key.get(char.lower(), char) for char in ciphertext)

def frequency_analysis(text, key):
    encrypted_text = encrypt(text, key)
    
    text = ''.join(char.lower() for char in encrypted_text if char.isalpha())
    letter_counts = {letter: text.count(letter) for letter in string.ascii_lowercase}
    total_letters = sum(letter_counts.values())
    
    # Calculate the frequency percentages
    letter_freqs = [(letter, (count / total_letters) * 100) for letter, count in letter_counts.items()]
    letter_freqs.sort(key=lambda x: x[1], reverse=True)
    
    return letter_freqs

def test_drive():
    key, reverse_key = generate_key()  
    print("\nKey for encryption:")
    key_output = ' | '.join([f"{original} -> {encrypted}" for original, encrypted in key.items()])
    print(key_output)
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Frequency analysis")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            plaintext = input("Enter a string to encrypt: ")
            encrypted_message = encrypt(plaintext, key)
            print("Encrypted Message:", encrypted_message)
        
        elif choice == '2':
            ciphertext = input("Enter a string to decrypt: ")
            decrypted_message = decrypt(ciphertext, reverse_key)
            print("Decrypted Message:", decrypted_message)
        
        elif choice == '3':
            print("Enter or paste your text for frequency analysis.")
            print("Type or paste '###END###' on a new line when finished:")
            corpus = ""
            while True:
                line = input()
                if line.strip() == "###END###":
                    break
                corpus += line + "\n"
            
            if corpus.strip():
                letter_freqs = frequency_analysis(corpus, key)
                print("\nLetter frequencies in the encrypted text (%):")
                for letter, freq in letter_freqs:
                    print(f"{letter} -> {freq:.2f}%")
                
                english_freq = 'etaoinshrdlcumwfgypbvkjxqz'
                potential_key = {}
                for i, (cipher_letter, _) in enumerate(letter_freqs):
                    if i < len(english_freq):
                        potential_key[cipher_letter] = english_freq[i]
                
                print("\nPotential key pairings based on frequency analysis:")
                key_output = ' | '.join([f"{cipher} -> {plain}" for cipher, plain in potential_key.items()])
                print(key_output)
            else:
                print("No text entered for analysis.")
        
        elif choice == '4':
            print("Goodbye! :D")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

test_drive()
