from lexer import lex
from parser_1 import parse_program
from interpreter import interpret
import re

def read_commands_from_file(filename):
    """
    Reads the entire content of a file.
    
    Args:
        filename (str): The name of the file to read.
        
    Returns:
        str: The content of the file.
    """
    with open(filename, 'r') as file:
        return file.read()

def process_commands(commands, symbol_table, output_file):
    """
    Processes and executes a series of commands.
    
    Args:
        commands (str): The commands to process.
        symbol_table (dict): The symbol table for storing variables.
        output_file (file object): The file to write output to.
    """
    lines = commands.splitlines()
    for line in lines:
        line = line.strip()
        if line and not line.endswith(';'):
            error_message = f"Error: Every input must end with a semicolon (;). Please fix the line: {line}"
            print(error_message)
            output_file.write(error_message + "\n")
            continue
        tokens = lex(line)
        if tokens:
            try:
                ast = parse_program(tokens)
                if interpret(ast, symbol_table, output_file) == 'EXIT':
                    return 'EXIT'
            except ValueError as e:
                error_message = f"Error in line '{line}': {str(e)}"
                print(error_message)
                output_file.write(error_message + "\n")

def get_output_filename(input_filename):
    """
    Generates an output filename based on the input filename.
    
    Args:
        input_filename (str): The input filename.
        
    Returns:
        str: The generated output filename.
    """
    match = re.match(r'(.*?)(\d+)(\.txt)', input_filename)
    if match:
        return f"output{match.group(2)}.txt"
    else:
        return "output.txt"

def main():
    """
    Main function to run the interpreter. Prints introductory information,
    reads commands from the user or a file, and processes them.
    """
    print("----------------------------------------")
    print(" 159.341 Assignment 1 Semester 1 2024 ")
    print(" Submitted by: Jamie Hughes, 2108715 ")
    print("----------------------------------------")
    print(" Input with Command Line with set <identifier> and <input>; ")
    print(" Input from File with set <filename>.txt, NOTE: THIS IS ONLY FOR TESTING") #ONLY FOR TESTING PURPOSE 
    print(" Make sure your input ends with ';' ")


    symbol_table = {}

    while True:
        input_string = input("> ").strip()
        if input_string.lower() == 'exit':
            print("Exiting the interpreter.")
            break
        
        # Check if the input is a command to read from a file
        if input_string.startswith('set ') and input_string.endswith('.txt'):
            filename = input_string.split(' ', 1)[1]
            try:
                commands = read_commands_from_file(filename)
                output_filename = get_output_filename(filename)
                with open(output_filename, 'w') as output_file:
                    print(f"Reading commands from {filename}...")
                    output_file.write(f"Reading commands from {filename}...\n")
                    if process_commands(commands, symbol_table, output_file) == 'EXIT':
                        break
            except FileNotFoundError:
                error_message = f"Error: File '{filename}' not found. Please try again."
                print(error_message)
        else:
            if not input_string.endswith(';'):
                error_message = "Error: Every input must end with a semicolon (;). Please try again."
                print(error_message)
                continue
            
            tokens = lex(input_string)
            if tokens:
                try:
                    ast = parse_program(tokens)
                    with open("output.txt", 'a') as output_file: #FOR TESTING 
                        if interpret(ast, symbol_table, output_file) == 'EXIT':
                            break
                except ValueError as e:
                    print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
