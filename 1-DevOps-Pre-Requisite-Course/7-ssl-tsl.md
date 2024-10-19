
A certificate is used to guarantee trust between 2 parties during a transaction. TLS certificate ensures the communication is encrypted.

## Symmetric Encryption
The data is encrypted using a key. They key is added to the data which encrypts it. The data is then sent to the server securely. A copy of the key must also be sent to the server to decrypt it.

## Asymmetric Encryption - SSH
Instead of using a single key to encrypt and decrypt, it uses a pair of keys:
- Private key
- Public key (Lock)

Anyone can access the lock (public key). But can only be opened with the key (private key). 

We generate a public and private key pair using:
```bash
ssh-keygen
```
It creates 2 files

![alt text](image-11.png)

We then blockk all access to the server using the lock i.e. the public key. Meaning anyone can see the lock but can only be opened with the (private) key.