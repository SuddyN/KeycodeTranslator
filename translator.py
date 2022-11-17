import sys

def makeLines(filename):
    lines: list[str] = []
    for line in open(filename, "r"):
        if len(line) == 0:
            continue
        lines.append(line.strip())
    return lines

def main():
    # Check stdin
    if len(sys.argv) < 3:
        print("Usage:  %s keyLogFilename keyDictFilename" % sys.argv[0])
        return
    # Initialize the KeyDict
    keyDict: dict = {}
    # Fill the KeyDict
    for entry in makeLines(sys.argv[2]):
        num = int(''.join(filter(str.isdigit, entry[:entry.find(" =")])))
        entry = entry[entry.find(" = ") + 3:]
        keyDict[num] = entry[:entry.find(" ")]
    # Process KeyLog
    for log in makeLines(sys.argv[1]):
        numStr = ''.join(filter(str.isdigit, log))
        print(log.replace(numStr, "[" + keyDict[int(numStr)] + "]"))
    return
    
if __name__ == "__main__":
    main()