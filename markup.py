keywords = ['bold', 'italic', 'underline', 'strike', 'h1', 'h2', 'h3',
            'h4', 'h5', 'h6', 'title', 'text', 'unorder', 'order', '-',
            'link', '!']
htmlWords = ['strong', 'em', 'u', 'strike', 'h1', 'h2', 'h3', 'h4', 'h5',
             'h6', 'title', 'p', 'ul', 'ol', 'li']

fileName = input("Enter file name of file to be read: ")
print("""
Available markup languages are:
    - HTML
""")
language = input("Enter markup language to transpile to: ")
language = language.lower()
file = open(fileName, 'r')
run = file.read()

def readFile():
    toRun = run.split("\n")

    for i in range(run.count("\n") + 1):
        command, value = toRun[i].split("|")
    
        keywordCheck = [e for e in keywords if e in command]

        if keywordCheck and language == 'html':
            if command == 'link':
                print("<a href=\""+value+"\">"+value+"</a>")
            else:
                for j in range(len(htmlWords)):
                    if command == keywords[j] and value == '{':
                        print("<"+htmlWords[j]+">")
                    elif command == keywords[j] and value == '}':
                        print("</"+htmlWords[j]+">")
                    elif command == keywords[j]:
                        print("<"+htmlWords[j]+">"+value+"</"+htmlWords[j]+">")
        else:
            raise Exception(command, "is not a valid command!")

readFile()
file.close()

end = input("Press enter to end the program: ")

