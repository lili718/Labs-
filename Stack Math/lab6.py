#Interface Class for a Stack
#Only allows access to the
#Stack commands of the built in list
class Stack:
    #Create a New Empty Stack
    def __init__(self):
        self.__S = []
    #Display the Stack
    def __str__(self):
        return str(self.__S)
    #Add a new element to top of stack
    def push(self,x):
        self.__S.append(x)
    #Remove the top element from stack
    def pop(self):
        return self.__S.pop()
    #See what element is on top of stack
    #Leaves stack unchanged
    def top(self):
        return self.__S[-1]
#postfix function
def postfix(exp):
    op = Stack()
    signs = ["+","/","*","-"]
    temp = exp.split()
    for i in temp:
        if i in signs:
            y = float(op.top())
            op.pop()
            z = float(op.top())
            op.pop()
            if i == "+":
                op.push(str(y+z))
            if i == "/":
                op.push(str(y/z))
            if i == "*":
                op.push(str(y*z))
            if i == "-":
                op.push(str(y-z))
        else:
            op.push(i)
    final = float(op.top())
    return(final)

if __name__ == "__main__":
    print("Welcome to Postfix Calculator")
    print("Enter exit to quit.")
    rexp = input("Enter Expression:\n")
    while rexp.lower() != "exit":
        print("Result: " + str(postfix(rexp)))
        rexp = input("Enter Expression:\n")

    
        
