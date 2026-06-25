from math import gcd, isqrt

# -----------------------------------
# Verificar si un número es primo
# -----------------------------------

def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, isqrt(n) + 1, 2):
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

    preferred = [65537, 257, 17, 5, 3]

    for e in preferred:
        if e < phi_n and gcd(e, phi_n) == 1:
            return e

    for e in range(3, phi_n, 2):
        if gcd(e, phi_n) == 1:
            return e

    return None


# -----------------------------------
# Encontrar d
# -----------------------------------

def find_d(e, phi_n):
    return pow(e, -1, phi_n)


# -----------------------------------
# Generar claves RSA
# -----------------------------------

def generate_keys(p, q):

    if not is_prime(p) or not is_prime(q):
        return {"error": "p y q deben ser números primos"}

    if p == q:
        return {"error": "p y q deben ser diferentes"}

    n = p * q

    phi_n = phi(p, q)

    e = find_e(phi_n)

    d = find_d(e, phi_n)

    return {

        # Números primos
        "p": p,
        "q": q,

        # Valores matemáticos
        "n": n,
        "phi": phi_n,
        "e": e,
        "d": d,

        # Claves
        "public_key": [e, n],
        "private_key": [d, n]
    }


# -----------------------------------
# Cifrar mensaje
# -----------------------------------

def encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]


# -----------------------------------
# Descifrar mensaje
# -----------------------------------

def decrypt(encrypted_message, d, n):
    return "".join(chr(pow(num, d, n)) for num in encrypted_message)


# -----------------------------------
# Factorización simple
# -----------------------------------

def factorize(n):

    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return [i, n // i]

    return []