class Validator:
    parantheses_dict={
                    '(':')',
                    '{':'}',
                    '[':']'
                    }

    def check_parantheses_balance(self,expression):
        parantheses_stack=[]
        for char in expression:
            if char in self.parantheses_dict.keys():
                parantheses_stack.append(char)
            elif char in self.parantheses_dict.values():
                if len(parantheses_stack)!=0:
                    popped_parentheses=parantheses_stack.pop()
                    if self.parantheses_dict[popped_parentheses]!=char:
                        return False
                else:
                    return False
        return len(parantheses_stack)==0

def main():
    expression_one="(){}}"
    expression_two="(){}"
    validator_object=Validator()
    print("{} : {}".format(expression_one,validator_object.check_parantheses_balance(expression_one)))
    print("{} : {}".format(expression_two,validator_object.check_parantheses_balance(expression_two)))

if __name__=='__main__':
    main()
