keywords = ['bold', 'italic', 'underline', 'strike', 'h1', 'h2', 'h3',
            'h4', 'h5', 'h6', 'title', 'text', 'unorder', 'order', '-',
            'link', 'color', 'bgcolor', '!']
htmlWords = ['strong', 'em', 'u', 'strike', 'h1', 'h2', 'h3', 'h4', 'h5',
             'h6', 'title', 'p', 'ul', 'ol', 'li']

print("Welcome to the LBLML Transpiler\nPlease include the file extension (e.g. \'.txt\') when inputing file names")
fileName = input("\n\nEnter name of file to be read: ")
writeName = input("Enter name of file to be written to (if it doesn't exist, one will be created): ")

file = open(fileName, 'r')
writeFile = open(writeName, 'a')
run = file.read()

def readWriteFile():
    toRun = run.split("\n")

    writeFile.write("<!DOCTYPE html>\n<html>\n<body>")
    
    for i in range(run.count("\n") + 1):
        command, value = toRun[i].split("|")
    
        keywordCheck = [e for e in keywords if e in command]

        if keywordCheck:
            if command == 'link':
                writeFile.write("\n<a href=\""+value+"\">"+value+"</a>")
            elif command == 'color':
                writeFile.write("\n<style>\nbody {\n\tcolor: "+value+";\n}\n</style>")
            elif command == 'bgcolor':
                writeFile.write("\n<style>\nbody {\n\tbackground-color: "+value+";\n}\n</style>")
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

readWriteFile()
file.close()
writeFile.close()

end = input("Press enter to end the program: ")

