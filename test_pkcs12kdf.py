from nose.tools import assert_equals
from Crypto.Cipher import AES
import base64
import pkcs12kdf

KEY_MATERIAL = 1
IV_MATERIAL = 2

def test_generate_derived_parameters():
  key_size = 128
  iv_size = 128
  iterations = 100000
  password = 'test'
  encodedtext = 'g9dHfFFwi5U5qE81RiaPjqQU8whYHHe7srwYo4F6XPCrwHNhkYu3zdSOeueX38Qg5egjytn1Qvx/jL71RXj+DQ=='

  enc = base64.b64decode(encodedtext)
  salt = enc[:16]
  cipher_text = enc[16:]
      
  key = pkcs12kdf.generate_derived_parameters(password, salt, iterations, KEY_MATERIAL, key_size / 8)
  iv = pkcs12kdf.generate_derived_parameters(password, salt, iterations, IV_MATERIAL, iv_size / 8)

  cipher = AES.new(key, AES.MODE_CBC, iv)
  text = cipher.decrypt(cipher_text)

  assert_equals(text, 'This is a sample text for testing encryption\x04\x04\x04\x04')
