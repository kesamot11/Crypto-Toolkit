from cryptokit import caesar

def interact(text, mode, k):
    """
    This function interacts with the user to type in the key and then calls the function,
    whether it should be encrypted or decrypted

    Args:
        text (string): Input the user wants to hash
        mode (int): Number 1-3, 1 - encrypt, 2 - decrypt,
            and 3 - brute force, that is only available to caesar cipher
        k (string): Key to use

    Returns:
        str: The encrypted/decrypted text
    """
    key_array = convert_to_numbers(k, text)

    if mode == 1:
        return encrypt(text, key_array)
    elif mode == 2:
        return decrypt(text, key_array)
    else:
        return None

def convert_to_numbers(key, text):
    """
    This function converts the key string to an array of integers, corresponding to the letters

    Args:
        key (string): Key to be converted to an array of integers
        text (string): To obtain the length of the text for the array of integers

    Returns:
        array: Array of integers, each corresponding to a letter in the alphabet - 1 (a = 0, b = 1, ...)
    """
    key = key.lower()
    res = []
    key_length = len(key)
    text_length = len(text)
    for i in range(text_length):
        number_to_append = (ord(key[i % key_length]) - 97)
        res.append(number_to_append)

    return res

def encrypt(text: object, key_array: object) -> str:
    """
    This function encrypts the input string using vigenere cipher with the given key

    Args:
        text (string): Text the user wants to encrypt
        key_array (array): Array of integers, each corresponding to a letter - 1

    Returns:
        str: The encrypted text
    """
    length = len(text)
    res = ''
    for i in range(length):
        res += caesar.encrypt(text[i], key_array[i])

    return res

def decrypt(text, key_array):
    """
    This function decrypts the input string using vigenere cipher with the given key
    
    Args:
        text (string): Text the user wants to decrypt
        key_array (array): Array of integers, each corresponding to a letter - 1
    
    Returns:
        str: The decrypted text
    """
    length = len(text)
    res = ''
    for i in range(length):
        res += caesar.decrypt(text[i], key_array[i])

    return res
