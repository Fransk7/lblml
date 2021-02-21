keywords = ['bold', 'italic', 'underline', 'strike', 'h1', 'h2', 'h3',
            'h4', 'h5', 'h6', 'title', 'text', 'unorder', 'order', '-',
            'link', '!']
htmlWords = ['strong', 'em', 'u', 'strike', 'h1', 'h2', 'h3', 'h4', 'h5',
             'h6', 'title', 'p', 'ul', 'ol', 'li']

fileName = input("Enter file name of file to be read: ")
writeName = input("Enter file name of file to be written to: ")

file = open(fileName, 'r')
writeFile = open(writeName, 'a')
run = file.read()

def readFile():
    toRun = run.split("\n")

    writeFile.write("<!DOCTYPE html>\n<html>\n<body>")
    
    for i in range(run.count("\n") + 1):
        command, value = toRun[i].split("|")
    
        keywordCheck = [e for e in keywords if e in command]

        if keywordCheck:
            if command == 'link':
                writeFile.write("\n<a href=\""+value+"\">"+value+"</a>")
            else:
                for j in range(len(htmlWords)):
                    if command == keywords[j] and value == '{':
                        writeFile.write("\n<"+htmlWords[j]+">")
                    elif command == keywords[j] and value == '}':
                        writeFile.write("\n</"+htmlWords[j]+">")
                    elif command == keywords[j]:
                        writeFile.write("\n<"+htmlWords[j]+">"+value+"</"+htmlWords[j]+">")
        else:
            raise Exception(command, "is not a valid command!")
        
    writeFile.write("\n</body>\n</html>")

readFile()
file.close()
writeFile.close()

end = input("Press enter to end the program: ")

