from lexer import (
    TOKEN_APPEND, TOKEN_LIST, TOKEN_EXIT, TOKEN_PRINT, TOKEN_PRINTLENGTH, TOKEN_PRINTWORDS, TOKEN_PRINTWORDCOUNT,
    TOKEN_SET, TOKEN_REVERSE, TOKEN_CONSTANT, TOKEN_END, TOKEN_PLUS, TOKEN_ID, TOKEN_LITERAL
)

def parse_program(tokens):
    statements = []
    while tokens:
        statement = parse_statement(tokens)
        statements.append(statement)
    return statements

def parse_expression(tokens):
    values = []
    while tokens and tokens[0][0] != TOKEN_END:
        values.append(parse_value(tokens))
        if tokens and tokens[0][0] == TOKEN_PLUS:
            tokens.pop(0)  # Discard the plus token
    if tokens and tokens[0][0] == TOKEN_END:
        tokens.pop(0)  # Consume the semicolon
    return ('EXPRESSION', values)

def parse_statement(tokens):
    if not tokens:
        raise ValueError("Incomplete statement")
    
    token_type, value = tokens.pop(0)

    if token_type not in [TOKEN_APPEND, TOKEN_LIST, TOKEN_EXIT, TOKEN_PRINT, TOKEN_PRINTLENGTH, TOKEN_PRINTWORDS, TOKEN_PRINTWORDCOUNT, TOKEN_SET, TOKEN_REVERSE]:
        raise ValueError(f"Invalid statement start: {token_type}")

    if token_type == TOKEN_SET:
        if not tokens or tokens[0][0] != TOKEN_ID:
            raise ValueError("Expected identifier after 'set'")
        id_token = tokens.pop(0)
        expression = parse_expression(tokens)
        return ('SET', id_token[1], expression)
    elif token_type == TOKEN_APPEND:
        if not tokens or tokens[0][0] != TOKEN_ID:
            raise ValueError("Expected identifier after 'append'")
        id_token = tokens.pop(0)
        expression = parse_expression(tokens)
        return ('APPEND', id_token[1], expression)

    elif token_type == TOKEN_REVERSE:
        if not tokens or tokens[0][0] != TOKEN_ID:
            raise ValueError("Expected identifier after 'reverse'")
        id_token = tokens.pop(0)
        consume_end_token(tokens)
        return ('REVERSE', id_token[1])

    elif token_type == TOKEN_PRINT and tokens:
        expression = parse_expression(tokens)
        return (TOKEN_PRINT, expression)

    elif token_type == TOKEN_PRINTLENGTH and tokens:
        expression = parse_expression(tokens)
        return (TOKEN_PRINTLENGTH, expression)

    elif token_type == TOKEN_PRINTWORDS and tokens:
        expression = parse_expression(tokens)
        return (TOKEN_PRINTWORDS, expression)

    elif token_type == TOKEN_PRINTWORDCOUNT and tokens:
        expression = parse_expression(tokens)
        return (TOKEN_PRINTWORDCOUNT, expression)

    elif token_type == TOKEN_LIST:
        consume_end_token(tokens)
        return ('LIST',)

    elif token_type == TOKEN_EXIT:
        consume_end_token(tokens)
        return ('EXIT',)

    else:
        raise ValueError(f"Unhandled statement type: {token_type}")

def consume_end_token(tokens):
    if not tokens:
        raise ValueError("Missing statement terminator ';'")
    if tokens[0][0] != TOKEN_END:
        raise ValueError("Missing statement terminator ';'")
    tokens.pop(0)  # Consume the semicolon

def parse_value(tokens):
    if not tokens:
        raise ValueError("Incomplete value")
    token_type, value = tokens.pop(0)
    if token_type in [TOKEN_ID, TOKEN_CONSTANT, TOKEN_LITERAL]:
        return (token_type, value)
    else:
        raise ValueError(f"Invalid value: {token_type}")
