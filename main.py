import subprocess, sys

def main():
    command = sys.argv[1:]
    output = subprocess.run(command)
    return output.returncode

if __name__=="__main__":
    returnCode = main()
    sys.exit(returnCode)