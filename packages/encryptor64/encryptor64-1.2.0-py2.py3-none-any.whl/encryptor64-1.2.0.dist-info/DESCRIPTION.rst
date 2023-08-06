# py-encryption
Python package for encryption strings by merging some key and string throw base64encode.

Example:
```python
# coding=utf-8
# Encoding
from encryption.encryption import *
some_key = "3jdg472666HJA83jJA723lL"
encrypt = Encryption(key=some_key)
encoded_string = encrypt.encode("my_string_for_encode")
print (encoded_string)

# Decoding
from encryption.encryption import *
some_key = "3jdg472666HJA83jJA723lL"
encrypt = Encryption(key=some_key)
decoded_string = encrypt.decode(encoded_string)
print (decoded_string)
```


