
#Lexer & Parser

#Name: Xavier Jordan Strang

class Lexer:
    def __init__(self, code):
        #given code, intializing code and the postion to 0
        self.code = code
        self.position = 0

    #Function to deal with blank spaces
    def blankSpace(self):
        #variable for readability
        code = self.code

        #While the length of the code is greater than the postion
        while len(code) > self.position:

            #If the current postion is not a space leave the loop
            if not code[self.position].isspace():
                break

            #if the current positon is a space move the postion by 1
            if code[self.position].isspace():
                self.position += 1

            #Fail safe case, returning an error has occured
            else:
                return ("Error, In Blankspace")

    # move the lexer position and identify next possible tokens.
    def get_token(self):
        
        #Key word variable helper function
        def keywordVariable(self):
            #defines the keywords
            self.keywords = ['while', 'if', 'else']

            #variables for easy readiablity
            code = self.code
            posi = self.position

            #if the position is in the alphabet
            if code[posi].isalpha():

                #Loop from the current positon
                for alpha in code[posi:]:

                    #if the position is alphanumeric move the positon by 1
                    if alpha.isalnum():
                        self.position += 1

                    #if the positon is not alphanumeric leave the loop
                    else:
                        break
                
                #if the current postions is in the defined keywords, make it all uppercase. If the current postion is not defined in the keywords
                #then it is a variable and not one of the defined keywords "while, if, else"
                return code[posi:self.position].upper() if code[posi:self.position] in self.keywords else 'Vari', code[posi:self.position]
            
            #Fail safe case, returning an error has occured
            else:
                return ("Error, In Keyword Variable (Get Token)")


        #Helper funciton for numvbers
        def number(self):
            #variables for easy readiblity
            code = self.code
            posi = self.position
            
            #if the current position is a digit
            if code[posi].isdigit():

                #Loop from the current position
                for dig in code[posi:]:

                    #if the charact is a digit move the positon by 1
                    if dig.isdigit():
                        self.position += 1

                    #if the charachter is not a digit leave the loop    
                    else:
                        break

                #Return the numb and the current position after the loop has completed
                return 'Numb', code[posi:self.position]
            
            #fail safe case, returning an error has occured
            else:
                return ("Error, In number (Get Token)")

        #Helper function for operator
        def operator(self):
            #variables for easy readiablity
            code = self.code
            posi = self.position
            oper = self.operator

            #if the current position is in the oper
            if code[posi] in oper:
                #if the current position is in oper and lenght of 1
                if code[posi:posi + 1] in oper:
                    #move the postion by 1
                    self.position += 1

                #if the current positon is in oper and lenght of 2
                elif code[posi:posi + 2] in oper:
                    #move the positon by 2
                    self.position += 2

                #Fail safe case, returning an error has occured
                else:
                    return ("Error, In Operator (Get Token)")

                #Returns an empty string 
                return '', code[posi:self.position]
            
            #fail safe, case returning an error has occured
            else:
                return ("Error, In Operator (Get Token)")

        #Helper function for arithmetic
        def arithmetic(self):
            #set the oper to the current postion in the code
            oper = self.code[self.position]

            #increments the positon by one, moving to the next character
            self.position += 1

            #if it is an operator
            if oper in ('=', '(', ')', '+', '-', '*', '/'):

                #if the operator is =
                if oper == '=':
                    #return the truple equal
                    output = 'Equal', oper
                    return output
                
                #if the operator is (
                if oper == '(':
                    #return the truple leftPara
                    output = 'LeftPara', oper
                    return output
                
                #if the operator )
                elif oper == ')':
                    #return the truple rightPara
                    output = 'RightPara', oper
                    return output

                #if the operator is +
                if oper in ('+'):
                    #return the truple Addit/Subtr
                    output = 'Addit/Subtr', oper
                    return output
                
                #If the operator is -
                elif oper in ('-'):
                    #return the truple Addit/Subtr
                    output = 'Addit/Subtr', oper
                    return output

                #if the operator is *
                if oper in ('*'):
                    #return the truple Multi/Divi
                    output = 'Multi/Divi', oper
                    return output
                
                #if the operator is /
                elif oper in ('/'):
                    #return the truple Multi/Divi
                    output = 'Multi/Divi', oper
                    return output
                
            #fail safe case, returning an error has occured
            else:
                return ("Error, In get Token")
     

        #Defines the sets of arithmetic and operators
        self.arithmetic = ['=', '(', ')', '+', '-', '*', '/']
        self.operator = ['>=' , '<=' , '<' , '>' , '!=' , '==']
        #Variable
        code = self.code

        #Calls the blank space helper function
        self.blankSpace()

        #if the length of the code is less than the postion return an empty string
        if len(code) <= self.position: 
            return '', None
        
        #if the length of the code is more than the positon
        elif len(code) > self.position:

            #If the current position is in the alphabet
            if code[self.position].isalpha():
                #Call the keywordvariable helper function and return the output
                output = keywordVariable(self)
                return output
            
            #if the current position is a digit 
            elif code[self.position].isdigit():
                #call the number helper function and return the output
                output = number(self)
                return output
            
            #If the current position is an operator
            elif code[self.position] in self.operator:
                #call the operator heleper fucntion and return the output
                output = operator(self)
                return output
            
            #if the current positions is an arithmetic 
            elif code[self.position] in self.arithmetic:
                #call the arithmetic helper fucntion and return the output
                output = arithmetic(self)
                return output
            
        #fail safe case, returning an error has occured
        else:
            return ("Error, in get Token")

class Parser:
    #Given code 
    def __init__(self, lexer):
        #Initalized the current token to none and initializes lexer
        self.lexer = lexer
        self.current_token = None

    # function to parse the entire program
    def parse(self):
        #parses the program
        setattr(self, 'program', self.program())
        program = getattr(self, 'program', None) 
        #returns the value of program
        return program
        
    # move to the next token.
    def advance(self):
        #A call to advance the token
        setattr(self, 'current_token', self.lexer.get_token())



    #Program; statement*
    # parse the one or multiple statements
    def program(self):

        #Helper function handles parsing
        def recurs():
            #sets the current token equal to token
            setattr(self, 'token', self.current_token[1])
            token = getattr(self, 'token', None) 

            #if the token is equal to nothing return and empty string
            if token == None:
                return ''
            
            #If the token is not equal to nothing call statment and call recurs
            elif token != None:
                return self.statement() + recurs()
            
            #Fail safe case, returning an error has occured
            else:
                return ("Error, In recurs (Program)")

        #advance the token
        self.advance()

        #Returns the final products after the helper function recurs has run
        return recurs()
        
    
    #Statment; expression | if_statement | while_loop
    # parse if, while, assignment statement.
    def statement(self):

        #Recursive helper function
        def recurs():
            #Sets the current token equal to token
            setattr(self, 'token', self.current_token[0])
            token = getattr(self, 'token', None) 

            if token == 'Vari' or 'WHILE' or 'IF':
                #if the token is Vari, call assignment and return the output
                if token == 'Vari':
                    return self.assignment()
            
                #If the token is WHILE, call while loop and return the output
                elif token == 'WHILE':
                    return self.while_loop()
            
                #If the token is IF, call statment and return the output
                elif token == 'IF':
                    return self.if_statement()
            
                #Fail safe case, returns an error has occured
                else:
                    return ("Error, Input is not a token type in statment method")
            
            #Fail Safe case, returingin an error has occured
            else:
                return ("Error, Input is not a token type in statment method")

        #Returns the output of the helper function as the final product
        return recurs()


    # parse assignment statements; 
    def assignment(self):

        #Sets token equal to the current token
        setattr(self, 'token', self.current_token[1])
        token = getattr(self, 'token', None) 

        #advances the token
        self.advance()

        #sets token 2 to the new current toek 
        setattr(self, 'token2', self.current_token[1])
        token2 = getattr(self, 'token2', None) 

        #calls the artihmetic expression function and sets it equal to arith_exp
        setattr(self, 'arith_exp', self.arithmetic_expression())
        arith_exp = getattr(self, 'arith_exp', None) 

        #return the formatted output with the new current token, current token, and the arithmetic expression
        return "('{}', '{}', {})".format(token2, token, arith_exp)


    #parse arithmetic experessions; term (('+' | '-') term)*
    def arithmetic_expression(self): 

        #sets element equal to the first term
        element = self.term()

        #Formatting helper function
        def operator(token1, element, element2):
            #formats the + output before returning it
            if token1 == "+":
                return "('{}', {}, {})".format(token1, element, element2)
            
            #Formats the - output before returning it
            elif token1 == "-":
                return "('{}', {}, {})".format(token1, element, element2)
            
            #Fail safe case, that returns an error has occured
            else:
                return ("Error, In Arithmetic Expression (Operator)")

        #Helper function for expression that handles parsing
        def expression(element):
            #Sets token0 equal to the current token
            setattr(self, 'token0', self.current_token[0])
            token0 = getattr(self, 'token0', None)

            #If the current token is not - or + then return the first term
            if token0 != "Addit/Subtr":
                return element
            
            #If the current token is - or +
            elif token0 == "Addit/Subtr":
                #set token1 equal to the current token
                setattr(self, 'token1', self.current_token[1])
                token1 = getattr(self, 'token1', None) 

                #advances the token
                self.advance()

                #sets element 2 equal to term call and call the formatting helper function, operator
                element2 = self.term()
                newElement = operator(token1, element, element2)

                #Returns the formatted output
                return expression(newElement)
    
        #Call the helper function expression wich does the parsing
        output = expression(element)

        #Check to see if the current tokeen is a right parathense ')'
        if self.current_token[0] == 'RightPara':
            #if so advance the token
            self.advance()

        #Returns the final ouput after the helper functions have run
        return output


    #Term; factor (('*' | '/') factor)*
    def term(self):

        #sets element to the first factor
        element = self.factor()
    
        #Helper function for formatting the outputs
        def operator(token1, element, element2):
            #Formats the * output before returning its product
            if token1 == "*":
                return "('{}', {}, {})".format(token1, element, element2)
            
            #Formats the / output before returning its product
            elif token1 == "/":
                return "('{}', {}, {})".format(token1, element, element2)
            
            #Fail safe case, returning an error has occured
            else:
                return ("Error, In Term (Operator)")

        #Helper function for term that handles the parsing
        def termHelp(element):
            #Sets the current token equal to token0
            setattr(self, 'token0', self.current_token[0])
            token0 = getattr(self, 'token0', None) 

            #If token0 is not * or / return the factor
            if token0 != "Multi/Divi":
                return element
            
            #If token0 is * or /
            elif token0 == "Multi/Divi":
                #Set token1 equla to the current token
                setattr(self, 'token1', self.current_token[1])
                token1 = getattr(self, 'token1', None)            

                #advance the token
                self.advance()

                #set element2 to the factor call and call the operator function, wich formats
                element2 = self.factor()
                newElement = operator(token1, element, element2)

                #return the formatted ouput
                return termHelp(newElement)
            
            #Fail safe case, returning an error has occured
            else:
                return ("Error, In term (termHelp)")

        #calls the term help function wich does the parsing
        output = termHelp(element)

        #returns the final output after the helper function have run
        return output


    #The factor function; number | variable | '(' arithmetic_expression ')'
    def factor(self):
        
        #Variable helper function
        def FactVar(self):
            #Set variable equal to the current token
            Vari = self.current_token[1]
            #advances the token
            self.advance()
            #Formats the variable into a string before returning it
            return "'{}'".format(Vari)
        
        #Number helper function
        def FactNumb(self):
            #Sets numb equal to the current token
            Numb = self.current_token[1]
            #advances the token
            self.advance()
            #returns the final product
            return Numb

        #Expression helper function
        def FactExp(self):
            #advance to next token
            self.advance()
            #output a call to arithmetic expression
            return self.arithmetic_expression()  
    
        #Sets token equal to the current token
        setattr(self, 'token', self.current_token[0])
        token = getattr(self, 'token', None) 

        #If the current token is numb
        if token == "Numb":
            #go to the factnum helper funciton
            output = FactNumb(self)
            #Outputs the final product
            return output
        
        #If the current token is Vari
        elif token == "Vari":
            #go to the factvar helper function
            output = FactVar(self)
            return output
        
        #if the current token is not numb 
        elif token != "Numb":
            #go to the factexp function
            output = FactExp(self)
            return output
        
        #if the current token is not Vari 
        elif token != "Vari":
            #go to the factexp function
            output = FactExp(self)
            return output
        
        #Fail safe case, returning an error
        else:
            return ("Error, In Factor")


    #If statment; 'if' condition 'then' statement ('else' statement)?
    # parse if statement, you can handle then and else part here.
    # you also have to check for condition.
    def if_statement(self):

        #Calls the condition function and sets it equal to cond
        cond = self.condition()
        #Advances to the next token
        self.advance()
        #Calls the statment function and sets it equal to state
        State = self.statement()

        #Sets token to be the current token
        setattr(self, 'token', self.current_token[0])
        token = getattr(self, 'token', None)

        #If the token is not equal to the current token, Not equal to ELSE
        if token != "ELSE":
            #Formats the ouput as an if statment with the condition and statement
            output = "('if', {}, {})".format(cond, State)
            return output
        #IF the current token is ELSE 
        elif token == "ELSE":
            #Advance to the next token from the current token
            self.advance()
            #Formats the output as an if statment with the condition, statment, and else statment
            output = "('if', {}, {}, {})".format(cond, State, self.statement())
            return output
        else:
            #Fail safe case, returning an error has occured
            return ("Error, In if_statement")


    
    #While Loop; 'while' condition 'do' statement
    # implement while statment, check for condition
    # possibly make a call to statement?
    def while_loop(self):
        #Call the condition and sets it equal to cond to be used
        cond = self.condition()
        #Advances to the next statment
        self.advance()
        
        #Formats the statement into a string
        State = "[{}]".format(self.statement())

        #Takes the statment string and removes the apostrophes around it
        while '"' in State:
            State = ''.join(remove for remove in State 
                               if remove != ('"'))
            
        #Formats the output so that it can be read 
        output = "('while', {}, {})".format(cond, State)
        #Returns the final output
        return output

       
    
    #Condition for 2 arithmetic expressions; arithmetic_expression ('==' | '!=' | '<' | '>' | '<=' | '>=') arithmetic_expression
    def condition(self):
        #Calls artithmetic expressions and sets it equal to expr0
        expr0 = self.arithmetic_expression()

        #Sets the variable token equal to the current token
        setattr(self, 'token', self.current_token[1])
        token = getattr(self, 'token', None)

        #If the token does not equal nothing 
        if token != None:
            #formats the token, placing apostrophes on either side of the token
            token = "'{}'".format(token)
        #If the token is equal to nothing 
        elif token == None:
            #Keep token as nothing 
            token = None
        #A fail safe case that returns an error has occured
        else:
            return ("Error, In Condition")

        #moves on to the next token from the current token
        self.advance()
        #Calls arithmetic expressions and sets it equal to expr1
        expr1 = self.arithmetic_expression()

        #Formats the output so that it is easy to read
        output = "({}, {}, {})".format(token, expr0, expr1)
        #Returns the final output 
        return output