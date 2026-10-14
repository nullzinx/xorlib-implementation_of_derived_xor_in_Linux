import hashlib
import subprocess

PROPERTIES = (
    "ro.product.brand",
    "ro.product.model",
    "ro.product.device",
)

def getprop(name):
    result = subprocess.run(
        ["getprop", name],
        capture_output=True,
        text=True,
        timeout=2,
        check=True,
    )
    return result.stdout.strip()

def get_fingerprint():
    values = [
        f"{name}={getprop(name)}"
        for name in PROPERTIES
    ]

    source = "\n".join(values).encode()
    return hashlib.sha256(source).digest()

def xor_cipher(data: bytes, key: bytes) -> bytes:
    return bytes(
        byte ^ key[i % len(key)]
        for i, byte in enumerate(data)
    )
if __name__ == "__main_":
    fingerprint = get_fingerprint()
    result = xor_derived(b"xorlib by nullzinx",fingerprint,)
    print(result.hex())
    print(xor_derived(result,fingerprint))
