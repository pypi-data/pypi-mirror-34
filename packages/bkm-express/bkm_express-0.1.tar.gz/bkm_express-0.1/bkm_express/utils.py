import textwrap
import settings
from base64 import b64decode, b64encode

from client_exceptions import EncryptionError

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as crypto_signature
from Crypto.Hash import SHA256

from Crypto.Cipher import PKCS1_v1_5 as crypto_cipher


def create_signature(data, private_key):
    try:
        rsa_key = RSA.importKey(private_key)
        signer = crypto_signature.new(rsa_key)
        digest = SHA256.new()
        digest.update(data)
        signature = signer.sign(digest)
    except Exception as e:
        raise EncryptionError("[Encryption Error] An error occured while encrypt your data:".format(e.message))

    return b64encode(signature)


def format_key(key, key_type='private'):
    line_character = 64 if key_type == 'public' else 65

    wrapped_key = textwrap.wrap(key, line_character)
    formatted_key = ''
    for wrap in wrapped_key:
        formatted_key = formatted_key + wrap + "\n"

    if key_type == 'public':
        formatted_key = '-----BEGIN PUBLIC KEY-----\n' + formatted_key + '-----END PUBLIC KEY-----'
    else:
        formatted_key = '-----BEGIN RSA PRIVATE KEY-----\n' + formatted_key + '-----END RSA PRIVATE KEY-----'
    return formatted_key


def verify_signature(ticket_id, signature):
    try:
        public_key = settings.BKM_PUBLIC_KEY

        rsakey = RSA.importKey(format_key(public_key, key_type='public'))
        signer = crypto_signature.new(rsakey)
        digest = SHA256.new()
        digest.update(ticket_id)

        verified = signer.verify(digest, b64decode(signature))
    except Exception as e:
        raise EncryptionError("[Encryption Error] An error occured while encrypt your data:".format(e.message))

    if not verified:
        raise EncryptionError("[Encryption Error] signature could not verified with ticked id")

    return True


def encrypt_vpos_configuration(data):
    encrypted_vpos = []
    wrapped_data = textwrap.wrap(data, 245)
    for chunk in wrapped_data:
        encrypted_chunk = encrypt_data(chunk)
        encrypted_vpos.append(encrypted_chunk)

    return '|:*:|'.join(encrypted_vpos)


def encrypt_data(data):
    try:
        public_key = settings.BKM_PUBLIC_KEY
        rsa = RSA.importKey(format_key(public_key, key_type='public'))
        cipher = crypto_cipher.new(rsa)
        data = data.replace(' ', '')
        encrypted_data = cipher.encrypt(data)
    except Exception:
        raise EncryptionError("[Encryption Error] An error occured while decrypting your data")
    return b64encode(encrypted_data)
