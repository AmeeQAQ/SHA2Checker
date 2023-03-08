import hashlib
import argparse

def parseargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--function", help="Which SHA-2 function you need to hash your file with (sha224/sha256/sha384/sha512).", required=True)
    parser.add_argument("-fi", "--file", help="file to be hashed. Use the absolute route if the file is not in the same directory as the script", required=True)
    parser.add_argument("-s", "--sum", help="Hash value issued by the file owner", required=True)
    return parser

def main():
    args = parseargs().parse_args()

    f = open(args.file, "rb")
    digest = hashlib.file_digest(f, args.function)
    f.close()
    hexdig = digest.hexdigest()
    print(hexdig)
    if hexdig == args.sum:
        print("File integrity sucessfully checked")
    else:
        print("File integrity check failed")


if __name__ == "__main__":
    main()



