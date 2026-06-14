from math import gcd

# -----------------------------------
# Verificar si un número es primo
# -----------------------------------

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


# -----------------------------------
# Función de Euler
# -----------------------------------

def phi(p, q):
    return (p - 1) * (q - 1)


# -----------------------------------
# Encontrar e
# -----------------------------------

def find_e(phi_n):

    for e in range(2, phi_n):
        if gcd(e, phi_n) == 1:
            return e

    return None


# -----------------------------------
# Encontrar d
# -----------------------------------

def find_d(e, phi_n):

    d = 1

    while (e * d) % phi_n != 1:
        d += 1

    return d


# -----------------------------------
# Generar claves RSA
# -----------------------------------

def generate_keys(p, q):

    if not is_prime(p) or not is_prime(q):
        return {"error": "p y q deben ser números primos"}

    n = p * q

    phi_n = phi(p, q)

    e = find_e(phi_n)

    d = find_d(e, phi_n)

    return {
        "p": p,
        "q": q,
        "n": n,
        "phi": phi_n,
        "e": e,
        "d": d,
        "public_key": [e, n],
        "private_key": [d, n]
    }


# -----------------------------------
# Cifrar mensaje
# -----------------------------------

def encrypt(message, e, n):

    encrypted = []

    for char in message:
        encrypted_char = pow(ord(char), e, n)
        encrypted.append(encrypted_char)

    return encrypted


# -----------------------------------
# Descifrar mensaje
# -----------------------------------

def decrypt(encrypted_message, d, n):

    decrypted = ""

    for num in encrypted_message:
        decrypted += chr(pow(num, d, n))

    return decrypted


# -----------------------------------
# Factorización simple
# -----------------------------------

def factorize(n):

    factors = []

    for i in range(2, int(n**0.5) + 1):

        if n % i == 0:
            factors.append(i)
            factors.append(n // i)
            break

    return factors