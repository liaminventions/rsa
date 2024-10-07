#!/bin/python
#!!WARNING!! requires pyasn1
#https://pypi.org/project/pyasn1

import base64
import textwrap

from pyasn1.codec.der import encoder
from pyasn1.type.univ import Sequence, Integer

PEM_TEMPLATE = (
    '-----BEGIN RSA PRIVATE KEY-----\n'
    '%s\n'
    '-----END RSA PRIVATE KEY-----\n'
)

def to_der(key):
    seq=Sequence()
    for idx,x in enumerate(
        [0,key[2][5],key[2][3],key[2][4],key[2][0],key[2][1],key[3][0],key[3][1],key[3][2]]
    ):
        seq.setComponentByPosition(idx,Integer(x))
    return encoder.encode(seq)

def to_pem(key):
    # return OpenSSL-compatible PEM encoded key
    b64 = base64.b64encode(to_der(key)).decode()
    b64w = "\n".join(textwrap.wrap(b64, 64))
    return (PEM_TEMPLATE % b64w).encode()
