from flask import Flask, request, jsonify
from flask_cors import CORS

from rsa_utils import *

app = Flask(__name__)

CORS(app)

# -----------------------------------
# HOME
# -----------------------------------

@app.route("/")
def home():
    return jsonify({
        "message": "RSA LAB API RUNNING"
    })


# -----------------------------------
# GENERAR CLAVES
# -----------------------------------

@app.route("/generate", methods=["POST"])
def generate():

    data = request.json

    p = int(data["p"])
    q = int(data["q"])

    keys = generate_keys(p, q)

    return jsonify(keys)


# -----------------------------------
# CIFRAR
# -----------------------------------

@app.route("/encrypt", methods=["POST"])
def encrypt_route():

    data = request.json

    message = data["message"]
    e = int(data["e"])
    n = int(data["n"])

    encrypted = encrypt(message, e, n)

    return jsonify({
        "encrypted": encrypted
    })


# -----------------------------------
# DESCIFRAR
# -----------------------------------

@app.route("/decrypt", methods=["POST"])
def decrypt_route():

    data = request.json

    encrypted_message = data["encrypted"]
    d = int(data["d"])
    n = int(data["n"])

    decrypted = decrypt(encrypted_message, d, n)

    return jsonify({
        "decrypted": decrypted
    })


# -----------------------------------
# FACTORIZAR
# -----------------------------------

@app.route("/factorize", methods=["POST"])
def factorize_route():

    data = request.json

    n = int(data["n"])

    factors = factorize(n)

    return jsonify({
        "factors": factors
    })


# -----------------------------------

if __name__ == "__main__":
    app.run(debug=True)