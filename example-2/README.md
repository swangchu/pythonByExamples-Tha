**Example 2**


1. **checkType folder** contains example for use of Python's type function.

        Syntax
        type(variable)
    
    - Checking Type of Data
    - To check the data type of a variable type() function is used.
    - The variable to be checked need to be placed in the bracket.

2. **comments folder** contains example for use of comments in Python.

        Syntax
        # for single line comment
        """
        This is
        multiline
        comments
        """
    
    - We use comments to leave notes for the reader. 
    - Comments are not executed by Python. 
    - Comments helps the reader to understand your code.
    - There are two types of comments. 
    - Single line comments starts with #
    - Multiline comments are included in triple quotes; """.

3. **arithmetic folder** contains example for use of aithmetic operators in Python.

        Syntax
        5 % 3 
        # 5 modulo 3 which will give us 2
        # since 2 is the remainder
    
    - Arithmetic Operators operators like +, - , / and * have their usual meaning.
    - Modulo % gives the reminder part of a division.

4. **assignment folder** contains example for use of assignment operator in Python.

        Syntax
        variableName = value
    
    - A single = is called assignment operator. 
    - It assigns values to a variable.
    
5. **comparision folder** contains example for use of comparision operators in Python.

        Syntax
        Comparison Operators
                These operators are used to compare.
                == is equality
                != not equal to
                > greater than
                < less than
                >= greater than or equal to <= less than equal to
6. **if folder** contains example for use of if statement in Python.

        Syntax
        if condition :
                # body of the if statment
    
    - If test a condition whether true or false. 
    - If true, the indented code will be executed, 
    - if not it will be skipped.

7. **else folder** contains example for use of if-else statement  in Python.

        Syntax
        if condition :
                # body of the if statment
        else:
                # body of the else
    
    - The body of the else will be executed if a condition is false.
    - The else part does not have condition.
 
 8. **elif folder** contains example for use of if-elif-else statement in Python.

        Syntax
        if condition :
                # body of the if statment
        elif condition:
                # body of the elif
        else:
                #body of else
    - If we need to use condition in the else part then elif must be used. 
    - If the condition is true then rest of the conditions are skipped.
    - The elif part does need condition.

9. **logical folder** contains example for use of logical operator(and) in Python.

        Operator | Description          | Expression
        --------------------------------------------
           and   |True if both          |   x and y
                 | operands are true    |
        ----------------------------------------------
            or   | True if either of the| x or y
                 | operands is true     |
        ---------------------------------------------
            not  |True if the operand is| not x
                 | false                |
        ----------------------------------------------

    - The logical operators are used to check multiple conditions at once.
    - The logical expression either results true or false.

10. **orNot folder** contains example for use of 'or' and 'not' logical operator in Python.

    Or and not Operators
    - The or logical operator returns true if one of the conditions is true.
    - The logical operator not returns true if the condition is false.


**PROJECT 2**

Get the average marks form the user to categorize the result of a student.

                100 - 80 |      Distinction
                80 - 70  |      First Division
                70 - 60  |      Second Division
                60 - 40  |      Third Division
                Less 40  |      Repeat

If the student failed, ask whether to repeat or not. Incase the student wants to repeat show a welcome back message.

