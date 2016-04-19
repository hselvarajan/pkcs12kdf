from nose.tools import assert_equals
from Crypto.Cipher import AES
import base64
import getpass
import hashlib
from pkcs12kdf import PKCS12KDF

KEY_MATERIAL = 1
IV_MATERIAL = 2

def test_generate_derived_parameters():
    key_size = 128
    iterations = 100000
    password = getpass.getpass()
    encoded_text = 'g9dHfFFwi5U5qE81RiaPjqQU8whYHHe7srwYo4F6XPCrwHNhkYu3zdSOeueX38Qg5egjytn1Qvx/jL71RXj+DQ=='

    enc = base64.b64decode(encoded_text)
    salt = enc[:16]
    cipher_text = enc[16:]

    kdf = PKCS12KDF(password, salt, iterations, "SHA256", key_size)
    (key, iv) = kdf.generate_key_and_iv()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    text = cipher.decrypt(cipher_text)

    print text

    assert_equals(text, 'This is a sample text for testing encryption\x04\x04\x04\x04')

test_generate_derived_parameters()