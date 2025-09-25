def interact(text, mode, k):
    """
    This function interacts with the user to type in the key and then calls the function,
    whether it should be encrypted or decrypted

    Args:
        text (string): Input the user wants to hash
        mode (int): Number 1-3, 1 - encrypt, 2 - decrypt,
            and 3 - brute force, that is only available to caesar cipher
        k (int): Key to use

    Returns:
        str: The encrypted/decrypted text
    """
    k = int(k % 95)
    if mode == 3:
        return brute_force(text)

    if mode == 1:
        return encrypt(text, k)
    elif mode == 2:
        return decrypt(text, k)
    else:
        return None

def encrypt(text, k):
    """
    This function encrypts the input string using caesar cipher with the given key

    Args:
        text (string): Text the user wants to encrypt
        k (int): Key that will be used to encrypt the string

    Returns:
        str: The encrypted text
    """
    res = ''
    for char in text:
        # Printable characters are from 32 to 126 - 95 in total
        char_to_replace = chr(((ord(char) - 32 + k) % 95) + 32)
        res += char_to_replace

    return res

def decrypt(text, k):
    """
    This function decrypts the input string using caesar cipher with the given key

    Args:
        text (string): Text the user wants to decrypt
        k (int): Key that will be used to decrypt the string

    Returns:
        str: The decrypted text
    """
    res = ''
    for char in text:
        char_to_replace = chr(((ord(char) - 32 - k) % 95) + 32)
        res += char_to_replace

    return res

def brute_force(text):
    """
    This function tries to brute force the decryption algorithm by trying all 128 possible keys.

    Args:
        text (string): Input the user wants to hash

    Returns:
        str: The decrypted text of all possible combinations, separated by a new line
    """
    res = ''
    for i in range(95):
        res += decrypt(text, i)
        res += '\n'

    return res