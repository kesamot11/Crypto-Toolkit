# Crypto Toolkit

A simple Python project for experimenting with classical ciphers.  
Currently implemented: **Caesar Cipher** with encryption, decryption, and brute-force attack.

## Features

- Interactive command-line interface.
- Caesar Cipher:
  - Encryption with a user-defined key.
  - Decryption with a user-defined key.
  - Brute-force mode that tries all possible shifts across printable ASCII.
- Supports printable ASCII characters (range `32–126`).
- Modular structure (`cryptokit/caesar.py` contains the cipher logic, `main.py` handles the CLI).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kesamot11/Crypto-Toolkit.git
   cd crypto-toolkit
   
2. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
    source .venv/bin/activate   # Linux / macOS
    .venv\Scripts\activate      # Windows

3. Run the program:
   ```bash
   python main.py
   
## Usage
- When prompted, choose an algorithm (currently only Caesar Cipher).  
- Enter the text you want to process.  
- Choose the mode:  
  - `1` → Encrypt  
  - `2` → Decrypt  
  - `3` → Brute-force attack (no key needed)  
- Enter the key (only required for encrypt/decrypt).  

### Example
Crypto Toolkit
Please select an algorithm
1 - Caesar Cipher

Enter your choice (1-6): 1

Enter your input: hello

Encrypt (1), Decrypt (2) or BruteForce (3 - Caesar only)?: 1

Enter your key as an integer: 3

=== RESULT ===

khoor

## Project Structure

    ```bash
    crypto-toolkit/
    │
    ├── main.py                # CLI entry point
    └── cryptokit/
        └── caesar.py          # Caesar Cipher implementation


