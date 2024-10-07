#!/bin/python
import pickle
import argparse

def rsa_encode(m,publickey):
  # c = (m ** e) % n
  output=[1 for i in range(len(m))]
  for i in range(len(m)):
        output[i]=pow(m[i],publickey[0],publickey[1])
  return output

def writefile(name,data):
    with open(name,'wb') as f:
        pickle.dump(data,f)

def readfile(name):
    with open(name,'rb') as f:
        return pickle.load(f)
  
def main():
    parser=argparse.ArgumentParser(description="Encodes a file via RSA public key.\npublic key is in .pk format ([e,n] saved using pickle) and output file is each encrypted byte in a list saved using pickle.")
    parser.add_argument('infile')
    parser.add_argument('-o','--output',help="output file (optional), defualt: encrypted.bin",required=False,default="encrypted.bin")
    parser.add_argument('-p','--publickey',help="public key file (optional), defualt: pub.pk",required=False,default="pub.pk")
    
    args=parser.parse_args()
    
    with open(args.infile,'rb') as f:
        message=f.read()
    
    publickey=readfile(args.publickey)
    writefile(args.output,rsa_encode(message,publickey))

if __name__ == "__main__":
    main()
