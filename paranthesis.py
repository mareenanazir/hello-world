openingParanthesisList=['(','{','[']
closingParanthesisList=[')','}',']']
def checkBalance(expression):
    stack=[]
    for char in expression:
        if char in openingParanthesisList:
            stack.append(char)
        elif char in closingParanthesisList:
            index=closingParanthesisList.index(char)
            if len(stack)!=0:
                if openingParanthesisList[index]==stack[len(stack)-1]:
                    stack.pop()
                else:
                    return "Not Valid"
            else:
                return "Not Valid"
    if len(stack)==0:
        return "Valid"

def main():
    expression1="(){}}"
    expression2="(){}"
    print expression1, ": ", checkBalance(expression1)
    print expression2, ": ", checkBalance(expression2)

if __name__=='__main__':
    main()
