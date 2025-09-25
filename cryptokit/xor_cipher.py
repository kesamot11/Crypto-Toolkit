import base64

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
    key = adjust_key_length(k, len(text))
    if mode == 1:
        return encrypt(text, key)
    elif mode == 2:
        return decrypt(text, key)
    else:
        return None

def adjust_key_length(key, length):
    """
    This function adjusts the length of the key to match the length of the text

    Args:
        text (string): Text the user wants to encrypt/decrypt
        key (string): Key that will be used to encrypt/decrypt the string

    Returns:
        str: The adjusted key
    """
    res = ''
    key_length = len(key)
    for i in range(length):
        res += key[i % key_length]
    return res

def encrypt(text, key):
    """
    This function encrypts the input string using xor cipher with the given key

    Args:
        text (string): Text the user wants to encrypt
        key (string): Key that will be used to encrypt the string

    Returns:
        str: The encrypted text
    """
    # convert text and key to bytes
    byte_text = text.encode('utf-8')
    byte_key = key.encode('utf-8')
    byte_array = []
    for t,k in zip(byte_text, byte_key):
        byte_array.append(t ^ k)

    xorred_bytes = bytes(byte_array)
    res = base64.b64encode(xorred_bytes).decode("utf-8")
    return res

def decrypt(text, key):
    """
    This function decrypts the input string using xor cipher with the given key

    Args:
        text (string): Text the user wants to decrypt
        key (string): Key that will be used to decrypt the string

    Returns:
        str: The decrypted text
    """
    byte_text = base64.b64decode(text.encode("utf-8"))
    byte_key = key.encode('utf-8')
    byte_array = []
    for t, k in zip(byte_text, byte_key):
        byte_array.append(t ^ k)

    xorred_bytes = bytes(byte_array)
    res = xorred_bytes.decode("utf-8")
    return res