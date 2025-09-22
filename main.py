from cryptokit import caesar

intro_text = """
Crypto Toolkit
Please select an algorithm
1 - Caesar Cipher
"""

def decide_algorithm(algorithm, text, mode, k):
    """
    This function decides the encryption/decryption algorithm that will be used.

    Args:
        algorithm (int): Number 1-6, each corresponding to a different algorithm
        text (string): Input the user wants to hash
        mode (int): Number 1-3, 1 - encrypt, 2 - decrypt,
            and 3 - brute force, that is only available to caesar cipher
        k (int): Key to use

    Returns:
        str: The encrypted/decrypted text
    """
    if algorithm == 1:
        return caesar.interact(text, mode, k)
    else:
        return "N/A"

def interaction():
    """
    This function manages the interaction with the user and the assignment of the variables the user types in.
    """
    print(intro_text)
    algorithm = int(input("Enter your choice (1-6): "))
    text = input("Enter your input: ")
    mode = int(input("Encrypt (1), Decrypt (2) or BruteForce (3 - Bruteforce only available to Caesar Cipher!)?: "))
    if mode == 3:
        print(decide_algorithm(algorithm, text, mode, 0))
    else:
        k = int(input("Enter your key as an integer: "))
        print(decide_algorithm(algorithm, text, mode, k))

def main():
    interaction()

if __name__ == "__main__":
    main()