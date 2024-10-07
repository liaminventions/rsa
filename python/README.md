[rsa-keygen.py](https://github.com/liaminventions/rsa/blob/main/python/rsa-keygen.py)
```
usage: rsa-keygen.py [-h] [-b BITS] [-priv PRIVATEKEY] [-pub PUBLICKEY]

Generates a RSA key-pair of specified size. the keys are saved using pickle;
e.g. publickey=[e,n], privatekey=[d,n].

options:
  -h, --help            show this help message and exit
  -b BITS, --bits BITS  how many bits large the primes are (optional), defualt:
                        2048 (RSA2048)
  -priv PRIVATEKEY, --privatekey PRIVATEKEY
                        private key output file (optional), defualt:
                        priv.secret
  -pub PUBLICKEY, --publickey PUBLICKEY
                        public key output file (optional), defualt: pub.pk
```
[rsa-encode.py](https://github.com/liaminventions/rsa/blob/main/python/rsa-encode.py)
```
usage: rsa-encode.py [-h] [-o OUTPUT] [-p PUBLICKEY] infile

Encodes a file via RSA public key. public key is in .pk format ([e,n] saved
using pickle) and output file is each encrypted byte in a list saved using
pickle.

positional arguments:
  infile

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output file (optional), defualt: encrypted.bin
  -p PUBLICKEY, --publickey PUBLICKEY
                        public key file (optional), defualt: pub.pk
```
[rsa-decode.py](https://github.com/liaminventions/rsa/blob/main/python/rsa-decode.py)
```
usage: rsa-decode.py [-h] [-p PRIVATEKEY] [-o OUTPUTFILE] encryptedfile

Decodes a RSA-encoded file via RSA private key. private key is in .secret
format ([d,n] saved using pickle) and input file is each encrypted byte in a
list saved using pickle.

positional arguments:
  encryptedfile

options:
  -h, --help            show this help message and exit
  -p PRIVATEKEY, --privatekey PRIVATEKEY
                        private key file (optional), defualt: priv.secret
  -o OUTPUTFILE, --outputfile OUTPUTFILE
                        output file (optional), defualt: prints to STDOUT
```
[rsa-cat.py](https://github.com/liaminventions/rsa/blob/main/python/rsa-cat.py)
```
usage: rsa-cat.py [-h] input

Reads a pickle formatted file and prints the contents to STDOUT. example uses:
rsa-cat.py pub.pk, rsa-cat.py encrypted.bin

positional arguments:
  input       input file.

options:
  -h, --help  show this help message and exit
```
