from lexer import (
    TOKEN_APPEND, TOKEN_LIST, TOKEN_EXIT, TOKEN_PRINT, TOKEN_PRINTLENGTH, TOKEN_PRINTWORDS,
    TOKEN_PRINTWORDCOUNT, TOKEN_SET, TOKEN_REVERSE, TOKEN_CONSTANT, TOKEN_END, TOKEN_ID, TOKEN_LITERAL
)
import re

def interpret(ast, symbol_table, output_file):
    """
    Interprets and executes a list of statements (AST nodes).
    
    Args:
        ast (list): The abstract syntax tree representing the program.
        symbol_table (dict): The symbol table storing variable values.
        output_file (file object): The file to write output to.
        
    Returns:
        str: 'EXIT' if an exit statement is encountered, otherwise None.
    """
    i = 0
    while i < len(ast):
        statement = ast[i]
        try:
            if statement[0] == 'APPEND':
                var_name, expression = statement[1], statement[2]
                value = evaluate_expression(expression, symbol_table)
                if var_name in symbol_table:
                    symbol_table[var_name] += value
                else:
                    symbol_table[var_name] = value
            elif statement[0] == 'LIST':
                output = f"Identifier list ({len(symbol_table)}):\n"
                for var_name, value in symbol_table.items():
                    output += f"{var_name}: {value}\n"
                print(output.strip())
                output_file.write(output)
            elif statement[0] == 'EXIT':
                output = "Exiting the interpreter."
                print(output)
                output_file.write(output + "\n")
                return 'EXIT'
            elif statement[0] == TOKEN_PRINT:
                expression = statement[1]
                value = evaluate_expression(expression, symbol_table)
                print(value)
                output_file.write(value + "\n")
            elif statement[0] == TOKEN_PRINTLENGTH:
                expression = statement[1]
                value = evaluate_expression(expression, symbol_table)
                output = f"Length is: {len(value)}"
                print(output)
                output_file.write(output + "\n")
            elif statement[0] == TOKEN_PRINTWORDS:
                expression = statement[1]
                value = evaluate_expression(expression, symbol_table)
                words = get_words(value)
                output = "Words are:\n" + "\n".join(words)
                print(output)
                output_file.write(output + "\n")
            elif statement[0] == TOKEN_PRINTWORDCOUNT:
                expression = statement[1]
                value = evaluate_expression(expression, symbol_table)
                words = get_words(value)
                output = f"Wordcount is: {len(words)}"
                print(output)
                output_file.write(output + "\n")
            elif statement[0] == 'SET':
                var_name, expression = statement[1], statement[2]
                value = evaluate_expression(expression, symbol_table)
                symbol_table[var_name] = value
            elif statement[0] == 'REVERSE':
                var_name = statement[1]
                if var_name in symbol_table:
                    words = get_words(symbol_table[var_name])
                    reversed_words = list(reversed(words))
                    symbol_table[var_name] = ' '.join(reversed_words)
                else:
                    raise ValueError(f"Undefined variable: {var_name}")
            i += 1  # Move to the next statement
        except Exception as e:
            error_message = f"Error: {str(e)}"
            print(error_message)
            output_file.write(error_message + "\n")
            # Skip to the next statement ending with a semicolon
            while i < len(ast) and ast[i][0] != TOKEN_END:
                i += 1

def evaluate_expression(expression, symbol_table):
    """
    Evaluates an expression and returns its value.
    
    Args:
        expression (tuple): The expression to evaluate.
        symbol_table (dict): The symbol table storing variable values.
        
    Returns:
        str: The evaluated value of the expression.
    """
    if expression[0] == 'EXPRESSION':
        values = [evaluate_value(value, symbol_table) for value in expression[1]]
        return ''.join(values)
    elif expression[0] == 'ID':
        return evaluate_value(expression, symbol_table)
    else:
        raise ValueError(f"Invalid expression: {expression[0]}")
    
def evaluate_value(value, symbol_table):
    """
    Evaluates a value and returns its string representation.
    
    Args:
        value (tuple): The value to evaluate.
        symbol_table (dict): The symbol table storing variable values.
        
    Returns:
        str: The string representation of the value.
    """
    token_type, token_value = value
    if token_type == TOKEN_ID:
        if token_value in symbol_table:
            return symbol_table[token_value]
        else:
            return ""  # Return an empty string for undefined variables
    elif token_type == TOKEN_CONSTANT:
        if token_value == 'SPACE':
            return ' '
        elif token_value == 'TAB':
            return '\t'
        elif token_value == 'NEWLINE':
            return '\n'
    elif token_type == TOKEN_LITERAL:
        return token_value
    else:
        raise ValueError(f"Invalid value: {token_type}")

def get_words(string):
    """
    Extracts words from a string.
    
    Args:
        string (str): The input string.
        
    Returns:
        list: A list of words found in the input string.
    """
    return re.findall(r"[a-zA-Z0-9]+(?:[-'][a-zA-Z0-9]+)*", string)
