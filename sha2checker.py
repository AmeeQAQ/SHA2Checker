import hashlib, argparse, ntpath

def hashcheck(file, func, sum):
    if ntpath.isfile(file):
        f = open(file, "rb")
        digest = hashlib.file_digest(f, func)
        f.close()
        hexdig = digest.hexdigest()
        print(hexdig + " *" + ntpath.basename(file))
        if hexdig == sum:
            print("File integrity sucessfully checked")
        else:
            print("File integrity check failed")
    else:
        print("File not found")

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-fi", "--file", 
                        help="file to be hashed. Use the absolute route if the file is not in the same directory as the script", required=True)
    parser.add_argument("-f", "--function", 
                        help="Which SHA-2 function you need to hash your file with (sha224/sha256/sha384/sha512). The script also admits MD5 (md5) and **possibly** (untested) other hashing functions supported by hashlib.py", required=True)
    parser.add_argument("-s", "--sum", help="Hash value issued by the file owner", required=True)
    return parser

def main():
    args = parser().parse_args()

    hashcheck(args.file, args.function, args.sum)

if __name__ == "__main__":
    main()



