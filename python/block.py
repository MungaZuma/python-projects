import hashlib

hash = hashlib.sha256("fall onto a sword and raise with the sun bleedby a stone on a moonlit night.".encode()).hexdigest()
print(hash)
