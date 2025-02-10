🔐 Flask AES Encryption & Decryption
📌 Project Overview
This project is a simple Flask-based text encryption and decryption tool using AES
encryption (CBC mode). It allows users to securely encrypt messages and decrypt them
using a unique key.

🚀 Features
AES-CBC Encryption
Random Key & IV Generation for each session
Flask API for encrypting & decrypting messages
Authenticated Encryption (AEAD) to prevent tampering
Web UI with a Green theme


Install Dependencies
pip install -r requirements.txt
Run the Flask App
python app.py
Then open your browser and go to: http://127.0.0.1:5000/
🔑 Usage
🔹 Encrypt a Message
Enter a plaintext message in the input field.
Click "Encrypt" to get the encrypted text & key.

🔹 Decrypt a Message
Enter the ciphertext and key.
Click "Decrypt" to retrieve the original message.

🛠 Technologies Used
Python (Flask)
Crypto.Cipher (AES-CBC)
HTML/CSS
Base64 Encoding

📝 Future Improvements
✅ File encryption support
✅ User authentication
✅ Store keys securely in a database
✅ Deploy on a web server

🚀 Developed by Pragadeeshwaran | Encryption Project

Dig into AES --> https://www.geeksforgeeks.org/advanced-encryption-standard-aes/
