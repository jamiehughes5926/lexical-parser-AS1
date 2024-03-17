import re

# Token definitions
TOKEN_APPEND = 'APPEND'
TOKEN_LIST = 'LIST'
TOKEN_EXIT = 'EXIT'
TOKEN_PRINT = 'PRINT'
TOKEN_PRINTLENGTH = 'PRINTLENGTH'
TOKEN_PRINTWORDS = 'PRINTWORDS'
TOKEN_PRINTWORDCOUNT = 'PRINTWORDCOUNT'
TOKEN_SET = 'SET'
TOKEN_REVERSE = 'REVERSE'
TOKEN_CONSTANT = 'CONSTANT'
TOKEN_END = 'END'
TOKEN_PLUS = 'PLUS'
TOKEN_ID = 'ID'
TOKEN_LITERAL = 'LITERAL'

# Regular expressions for tokens
token_patterns = [
    (r'append', TOKEN_APPEND),
    (r'printwordcount', TOKEN_PRINTWORDCOUNT),
    (r'printwords', TOKEN_PRINTWORDS),
    (r'printlength', TOKEN_PRINTLENGTH),
    (r'list', TOKEN_LIST),
    (r'exit', TOKEN_EXIT),
    (r'print', TOKEN_PRINT),
    (r'set', TOKEN_SET),
    (r'reverse', TOKEN_REVERSE),
    (r'SPACE|TAB|NEWLINE', TOKEN_CONSTANT),
    (r';', TOKEN_END),
    (r'\+', TOKEN_PLUS),
    (r'"(?:\\.|[^"\\])*"', TOKEN_LITERAL),
    (r'[a-zA-Z][a-zA-Z0-9]*', TOKEN_ID),
]

def lex(input_string):
    """
    Lexer that tokenizes an input string based on predefined patterns.
    
    Args:
        input_string (str): The input string to tokenize.
        
    Returns:
        list: A list of tokens.
    """
    tokens = []
    while input_string:
        match = None
        for pattern, token_type in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(input_string)
            if match:
                value = match.group(0)
                if token_type == TOKEN_LITERAL:
                    value = value[1:-1]  # Remove surrounding quotes
                    value = re.sub(r'\\(.)', r'\1', value)  # Unescape characters
                tokens.append((token_type, value))
                input_string = input_string[len(value):]  # Move past the matched value
                input_string = input_string.lstrip()  # Strip leading whitespace
                break
        if not match:
            input_string = input_string[1:]  # Skip invalid characters
    return tokens
