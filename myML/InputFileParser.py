import os

def InputFileParser(file_name):
    if os.path.exists(file_name):
        with open(file_name,"r") as f:
            content = f.read()
        return [[float(b) for b in a.split(',')] for a in content.strip().splitlines()]
    else:
        print("InputFileParser: File doesn't exist!")
        return None
