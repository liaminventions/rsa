#!/bin/python
## !! https://www.geeksforgeeks.org/how-to-generate-large-prime-numbers-for-rsa-algorithm/ !!
## !!TODO!! consolidate and understand

import pickle
import argparse
import pem

DEFUALT_E=65537

# Large Prime Generation for RSA
from random import SystemRandom

# Pre generated primes
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]

cryptogen = SystemRandom()

def nBitRandom(n):
    return cryptogen.randrange(2**(n-1)+1, 2**n - 1)


def getLowLevelPrime(n):
    '''Generate a prime candidate divisible
    by first primes'''
    while True:
        # Obtain a random number
        pc = nBitRandom(n)

        # Test divisibility by pre-generated
        # primes
        for divisor in first_primes_list:
            if pc % divisor == 0 and divisor**2 <= pc:
                break
        else:
            return pc


def isMillerRabinPassed(mrc):
    '''Run 20 iterations of Rabin Miller Primality test'''
    maxDivisionsByTwo = 0
    ec = mrc-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == mrc-1)

    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                return False
        return True

    # Set number of trials here
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = cryptogen.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True


#if __name__ == '__main__':
#    while True:
#        n = 1024
#        prime_candidate = getLowLevelPrime(n)
#        if not isMillerRabinPassed(prime_candidate):
#            continue
#        else:
#            print(n, "bit prime is: \n", prime_candidate)
#            break

def getPrime(n=1024):
  while True:
    prime_candidate = getLowLevelPrime(n)
    if not isMillerRabinPassed(prime_candidate):
      continue
    else:
      return(prime_candidate)
      break

def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp

## END OF CODE THAT IDK

# Extended Euclidean Algorithm 
def eea(x,m):
    a, b, u = 0, m, 1
    # aka a=0;b=m;u=1
    while x > 0:
        q = b // x  # integer division
        x, a, b, u = b % x, u, x, a - q * u
        # aka:
        # x=b%x;a=u;b=x;u=a-q*u 
    if b == 1:
        return a % m
    raise ValueError("must be coprime")

def findInverse(num, mod):
  listA = [mod,0]; listB = [num,1]
  factor = listA[0]//listB[0]
  listC = [listA[0]-(factor)*listB[0],listA[1]-listB[1]*(factor)]
  while listC[0] > 1:
    listA = listB; listB = listC
    factor = listA[0]//listB[0]
    listC = [listA[0]-(factor)*listB[0],listA[1]-listB[1]*(factor)]
  return listC[1]

#def findModInverse(num, mod):
#  for i in range(mod):
#    if (num*i)%mod==1:
#      return(i)
#  raise ValueError("no inverse")

def rsa_keygen(bits):
  # generate p, q, n, tot(n) ((p-1)(q-1)), e, d
  # p,q are large primes        (SECRET)
  # n = pq                      (PUBLIC)(SECRET)
  # tot(n) = (p-1)*(q-1)        (SECRET)
  # e (e,tot(n) are rel. prime) (PUBLIC)(SECRET)
  # d = findInverse(e,tot(n))   (SECRET)
  p=getPrime(bits); q=getPrime(bits)
  while(q==p):
      q=getPrime(bits)
  n=p*q
  t1,t2=(p-1),(q-1)
  tot=t1*t2
  e=DEFUALT_E
  d=eea(e,tot)
  dP=d%(p-1)
  dQ=d%(q-1)
  qInv=findInverse(q,p)
  private=[d,n]
  public=[e,n]
  other=[p,q,tot,e,d,n]
  sign=[dP,dQ,qInv]
  return[private,public,other,sign]

def writefile(name,data):
    with open(name,'wb') as f:
        pickle.dump(data,f)

def readfile(name):
    with open(name,'rb') as f:
        return pickle.load(f)

def main():
    parser=argparse.ArgumentParser(description="Generates a RSA key-pair of specified size.\nthe keys are saved using pickle; e.g. publickey=[e,n], privatekey=[d,n].")
    parser.add_argument('-b','--bits',help="how many bits large the primes are (optional), defualt: 2048 (RSA2048)",required=False,default=2048)
    parser.add_argument('-priv','--privatekey',help='private key output file (optional), defualt: priv.secret',required=False,default='priv.secret')
    parser.add_argument('-pub','--publickey',help='public key output file (optional), defualt: pub.pk',required=False,default='pub.pk')
    parser.add_argument('--pem',help='.pem/ASN.1 mode',action="store_true")

    args=parser.parse_args()

    bits=int(args.bits)

    key=rsa_keygen(bits)

    #Private key
    writefile(args.privatekey,key[0])
   
    #Public key
    if not(args.pem): 
        #write keys to file    
        writefile(args.publickey,key[1])
    else:
        args.publickey+='.pem'
        with open(args.publickey,"wb") as f:
            f.write(pem.to_pem(key))
if __name__ == "__main__":
    main()
