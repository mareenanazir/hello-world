class ValidatorClass:
    opening_parantheses_list=['(','{','[']
    closing_parantheses_list=[')','}',']']

    def __init__(self,expression):
        self.expression=expression
        self.parantheses_stack=[]

    def check_balance(self):
        for char in self.expression:
            if char in self.opening_parantheses_list:
                self.parantheses_stack.append(char)
            elif char in self.closing_parantheses_list:
                index=self.closing_parantheses_list.index(char)
                if len(self.parantheses_stack)!=0:
                    if self.opening_parantheses_list[index]==self.parantheses_stack[len(self.parantheses_stack)-1]:
                        self.parantheses_stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(self.parantheses_stack)==0:
            return True

def main():
    expression_one="(){}}"
    expression_two="(){}"
    validator_object_one=ValidatorClass(expression_one)
    validator_object_two=ValidatorClass(expression_two)
    #flag=validator_object_one.check_balance()
    print("%s : %r" % (expression_one,validator_object_one.check_balance()))
    print("%s : %r" % (expression_two,validator_object_two.check_balance()))

if __name__=='__main__':
    main()
