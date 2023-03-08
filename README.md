# SHA2Checker
Quick n' dirty SHA-2 file integrity checker script for any hash value generated by an SHA-2 function (224, 256, 384 &amp; 512), as well as MD5.  
Developed in Python 3.11 using the secure hash library [**hashlib**](https://docs.python.org/3/library/hashlib.html) and it's incredibly useful and convenient `file_digest()` function, as well as [**argparse**](https://docs.python.org/3/library/argparse.html) for the easy-to-implement command-line arguments.  
## Usage
Download the Python script available in this repository (`sha2checker.py`). Once downloaded, run it with `python` through your terminal.  
***WARNING: Be sure to have Python 3.11 installed. Otherwise, the script will not work***.  
You will have to define **3** parameters:  
>`-f`, `--function`: Which SHA-2 function you need to hash your file with (sha224/sha256/sha384/sha512). The script also admits MD5 (md5) and **possibly** (untested) other hashing functions supported by hashlib.py  
`-fi`, `--file`: file to be hashed. Use the absolute route if the file is not in the same directory as the script.  
`-s`, `--sum`: Hash value issued by the file owner.  
*Taken directly from each argument's help text*.

After that, you will be prompted with the hash generated alongisde the name of the digested file (a87b7d9f0... *foo.txt). The next prompt will be if both the checksum generated and the one provided as a parameter are equal or not.  
