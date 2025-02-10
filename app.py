from flask import Flask, render_template, request, jsonify
from encryption import encrypt, decrypt

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/encrypt', methods=['POST'])
def encrypt_text():
    data = request.json.get("plaintext", "")
    if not data:
        return jsonify({"error": "No text provided"}), 400

    encrypted_text = encrypt(data)
    return jsonify({"ciphertext": encrypted_text})


@app.route('/decrypt', methods=['POST'])
def decrypt_text():
    data = request.json.get("ciphertext", "")
    if not data:
        return jsonify({"error": "No ciphertext provided"}), 400

    decrypted_text = decrypt(data)
    return jsonify({"plaintext": decrypted_text})


if __name__ == '__main__':
    app.run(debug=True)
