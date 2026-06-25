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

    data = request.get_json(force=True)

    if not data:
        return jsonify({"error": "No se recibieron datos"}), 400

    try:
        p = int(data["p"])
        q = int(data["q"])
    except:
        return jsonify({"error": "Datos inválidos"}), 400

    return jsonify(generate_keys(p, q))


# -----------------------------------
# CIFRAR
# -----------------------------------

@app.route("/encrypt", methods=["POST"])
def encrypt_route():

    data = request.get_json(force=True)

    if not data:
        return jsonify({"error": "No se recibieron datos"}), 400

    try:
        message = data["message"]
        e = int(data["e"])
        n = int(data["n"])
    except:
        return jsonify({"error": "Datos inválidos"}), 400

    encrypted = encrypt(message, e, n)

    return jsonify({
        "encrypted": encrypted
    })


# -----------------------------------
# DESCIFRAR
# -----------------------------------

@app.route("/decrypt", methods=["POST"])
def decrypt_route():

    data = request.get_json(force=True)

    if not data:
        return jsonify({"error": "No se recibieron datos"}), 400

    try:
        encrypted_message = data["encrypted"]
        d = int(data["d"])
        n = int(data["n"])
    except:
        return jsonify({"error": "Datos inválidos"}), 400

    decrypted = decrypt(encrypted_message, d, n)

    return jsonify({
        "decrypted": decrypted
    })


# -----------------------------------
# FACTORIZAR
# -----------------------------------

@app.route("/factorize", methods=["POST"])
def factorize_route():

    data = request.get_json(force=True)

    if not data:
        return jsonify({"error": "No se recibieron datos"}), 400

    try:
        n = int(data["n"])
    except:
        return jsonify({"error": "Datos inválidos"}), 400

    return jsonify({
        "factors": factorize(n)
    })


# -----------------------------------

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        threaded=True
    )