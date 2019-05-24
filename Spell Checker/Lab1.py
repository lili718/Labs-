from spellchecker import spellchecker
openfile=""
SP= spellchecker("english_words.txt")
        
def get_file():
    file = input("Enter the name of the file to read:\n")
    try:
        openfile = open(file, "r")
        return openfile
    except:
        print("Could not open file.")
        get_file()

def readfile(file_name):
    true=0
    false=0
    lines=file_name.readlines()
    for line in lines:
        for currword in line.split():
            cword= SP.check(currword)
            if cword == False:
                print("Possible Spelling Error on line ", lines.index(line)+1, ":", currword)
                false=false+1
            else:
                true=true+1
    percent =  (true/(true+false))*100
    print(true, "words passed the spell checker.")
    print(false, "words failed the spell checker.")
    print(round(percent,2), "% of words passed.")
if __name__=="__main__":
    print("Welcome to the Text File Spellchecker")
    openfile=get_file()            
    readfile(openfile)  