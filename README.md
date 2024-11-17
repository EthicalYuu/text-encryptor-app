# Encryption and Decryption Application

## Overview
This application provides a simple interface for encrypting and decrypting messages using the Fernet symmetric encryption and RSA asymmetric encryption algorithms. It also allows users to generate encryption keys and encrypt or decrypt files. The application is built using Python's Tkinter for the graphical user interface and integrates the cryptography library for encryption and decryption.

## Features
- **Message Encryption**: Encrypt text messages using the Fernet encryption algorithm.
- **File Encryption/Decryption**: Encrypt and decrypt text files with a user-generated key.
- **Key Generation**: Generate secure Fernet encryption keys.
- **File Handling**: Open, save, and choose files for encryption and decryption.

## Installation
To run this application, follow these steps:

### Prerequisites
- Python 3.x
- Required libraries: `cryptography`, `tkinter`

### Step-by-Step Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/EthicalYuu/text-encryptor-app.git
    ```

2. Install dependencies:
    ```bash
    pip install cryptography
    ```

3. Run the application:
    ```bash
    python main.py
    ```

## Usage

### Key Generation
- **Generate a Key**: Click the "Generate Key" button to create a new encryption key.
- **Save the Key**: The generated key is copied to the clipboard automatically. Make sure to save it securely.

### File Encryption
1. **Select a file**: Click the "Encrypt Notepad File" button to select a text file for encryption.
2. **Enter the Key**: Paste or type the generated key in the "Key" field.
3. **Encrypt the File**: Click the "Encrypt" button to encrypt the file and save the encrypted content to a new file.

### File Decryption
1. **Select a file**: Click the "Decrypt Notepad File" button to select an encrypted text file.
2. **Enter the Key**: Paste or type the correct key in the "Key" field.
3. **Decrypt the File**: Click the "Decrypt" button to decrypt the file and save the decrypted content to a new file.

### Notes
- Ensure that you save the generated keys, as they cannot be recovered once lost.
- Make sure to use the correct key when decrypting files, otherwise, the decryption will fail.

## Further Improvements

While the current application provides basic functionality for encryption and decryption, there are several areas that can be enhanced or expanded. Some ideas for further improvements include:

### 1. **Code Refactoring**
   - The current code was written when I first started programming, and as such, it could benefit from refactoring. This would involve restructuring the code to make it cleaner, more efficient, and easier to maintain. The goal is to improve readability, reduce duplication, and ensure that the code follows best practices and modern software development standards.

### 2. **User Authentication**
   - Implement user authentication to secure access to the application. Only authorized users should be able to generate keys or decrypt sensitive information.

### 3. **Support for More Encryption Algorithms**
   - Expand the functionality to support additional encryption algorithms, such as AES or ECC (Elliptic Curve Cryptography), for more flexibility in choosing encryption methods.

### 4. **Key Management**
   - Integrate a secure key management system that allows users to store, retrieve, and manage their keys securely. This could include features like key expiration, rotation, and backup.

### 5. **File Format Support**
   - Extend the application to support encryption/decryption of various file types (e.g., PDFs, images, Word documents) rather than just text files.

### 6. **Error Handling and Validation**
   - Improve error handling to provide more user-friendly messages when invalid keys are entered or when files fail to decrypt.
   - Add input validation to ensure users are providing correct data formats (e.g., ensuring the key is valid).

### 7. **Cross-Platform Support**
   - Make the application cross-platform (Windows, macOS, Linux) by ensuring compatibility with different operating systems and creating packaged executable files.

### 8. **Graphical Improvements**
   - Improve the graphical user interface (GUI) with more intuitive design, additional themes, and better file handling features, such as drag-and-drop file selection.

### 9. **Batch Processing**
   - Add the ability to batch encrypt or decrypt multiple files at once to save time when dealing with a large number of files.

### 10. **Backup and Recovery**
   - Implement a backup feature for both the application and key storage, ensuring that users can recover encrypted data and keys in case of data loss.

### 11. **Cloud Integration**
   - Allow users to save encrypted files directly to cloud storage services such as Google Drive, Dropbox, or AWS S3, with encryption happening before the file is uploaded.
