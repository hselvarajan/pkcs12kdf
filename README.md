A python implementation of the [PKCS12](https://tools.ietf.org/html/rfc7292#appendix-B) Key Derivation Function (KDF).

**The PKCS12 KDF is deprecated and the use of a more modern Key Derivation Function like [PBKDF2](https://tools.ietf.org/html/rfc2898#section-5.2) is recommended. This library exists for compatibility with existing KDF schemes based on PKCS12**.

To use this library:

* Get the password from the user, preferably using `getpass()`
* Create an instance of the PKCS12KDF object, passing the following parameters:
    * password
    * salt
    * iteration count for the hash function
    * block length of the hash function, in bits (SHA-256 has a block length of 512 bits/32 bytes)
    * Desired key length in bits
* Call `generate_key_and_iv` on the `PKCS12KDF` instance, which will return a `(key,iv)` tuple
