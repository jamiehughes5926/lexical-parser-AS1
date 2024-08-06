## README

### Project Description
This project is an interpreter for a custom scripting language. It includes lexical analysis, parsing, and execution of commands that manipulate variables and output results.

### Files and Modules
- **lexer.py:** Contains the lexer that tokenizes input strings.
- **parser_1.py:** Contains the parser that creates an abstract syntax tree (AST) from tokens.
- **interpreter.py:** Contains the interpreter that executes the AST.
- **main.py:** The main entry point for running the interpreter.

### Token Definitions
- **TOKEN_APPEND:** 'APPEND'
- **TOKEN_LIST:** 'LIST'
- **TOKEN_EXIT:** 'EXIT'
- **TOKEN_PRINT:** 'PRINT'
- **TOKEN_PRINTLENGTH:** 'PRINTLENGTH'
- **TOKEN_PRINTWORDS:** 'PRINTWORDS'
- **TOKEN_PRINTWORDCOUNT:** 'PRINTWORDCOUNT'
- **TOKEN_SET:** 'SET'
- **TOKEN_REVERSE:** 'REVERSE'
- **TOKEN_CONSTANT:** 'CONSTANT'
- **TOKEN_END:** 'END'
- **TOKEN_ID:** 'ID'
- **TOKEN_LITERAL:** 'LITERAL'

### Lexical Analysis
The lexer tokenizes the input string based on predefined patterns. It recognizes keywords, identifiers, literals, and special characters.

### Parsing
The parser converts the list of tokens into an abstract syntax tree (AST) that represents the program structure.

### Interpreter Functions
- **interpret:** Executes the AST by processing each statement and updating the symbol table.
- **evaluate_expression:** Evaluates expressions and returns their values.
- **evaluate_value:** Evaluates individual values, such as identifiers and literals.
- **get_words:** Extracts words from a string using regular expressions.

### Main Function
The main function reads commands from the user or a file, processes them, and executes the interpreter.

### Usage
To run the interpreter, execute the following command:
```bash
python main.py
