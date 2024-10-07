#!/bin/python
import argparse
import pickle

def rsa_decode(c,privatekey):
  # m = (c ** d) % n
  output=[1 for i in range(len(c))]
  for i in range(len(c)):
        output[i]=pow(c[i],privatekey[0],privatekey[1])
  return(output)

def writefile(name,data):
    with open(name,'wb') as f:
        pickle.dump(data,f)

def readfile(name):
    with open(name,'rb') as f:
        return pickle.load(f)

def main():
    parser=argparse.ArgumentParser(description="Decodes a RSA-encoded file via RSA private key.\nprivate key is in .secret format ([d,n] saved using pickle) and input file is each encrypted byte in a list saved using pickle.")
    parser.add_argument('encryptedfile')
    parser.add_argument('-p','--privatekey',help='private key file (optional), defualt: priv.secret',required=False,default="priv.secret")
    parser.add_argument('-o','--outputfile',help='output file (optional), defualt: prints to STDOUT',required=False,default="")
    
    args=parser.parse_args()

    privatekey=readfile(args.privatekey)

    d=rsa_decode(readfile(args.encryptedfile),privatekey)

    if (args.outputfile==""):
        out=''
        for i in d:
            out+=chr(i)
        print(out)
    else:
        with open(args.outputfile,'wb') as f:
            f.write(bytes(d))

if __name__ == "__main__":
    main()
