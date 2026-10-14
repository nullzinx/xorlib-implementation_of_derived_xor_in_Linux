# xorlib - implementation_of_derived_xor_in_Linux
this is a small implementation of xor  cipher using derived keys

## how it work?
The XOR operation has the following property: (A ⊕ K) ⊕ K = A.
This means that data encrypted with XOR can be decrypted using the same key.
The program also allows you to derive a key from your Linux system.

## usage 
two functions un the library 
*get_fingerprint()* - create derived key
*xor_cipher(data,key)* - encrypted and decrypted with XOR

### exemple
```python
from xorlib import get_fingerprint,xor_cipher


sinsible_data = "nuclear_launch_codes"
key = get_fingerprint()
print("your derivate key:",key)

encrypted_data = xor_cipher(sinsible_data.encode(),key.encode())
print("data encrypted by xorlib:",encrypted_data.decode())
decrypt_data = xor_cipher(encrypted_data,key) 
print("data decrypt by xorlib:",decrypt_data.decode())

```
*waring*:For serious projects, use more robust libraries and algorithms. The derived key is not unique to each device.

