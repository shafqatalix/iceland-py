from application import generate
import sys

if(__name__=="__main__"):
    print("Args: "+ ', '.join(sys.argv[1:]))
    connectionStringArg= sys.argv[1].split("=")[1]    
    generate(connectionStringArg)