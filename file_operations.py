def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as input_file:
            # Read the contents of the file
            content = input_file.read()
        
        # Modify the content (for example, convert it to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"Content from {input_filename} has been modified and written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except IOError:
        print(f"Error: An error occurred while reading or writing the file.")

def handle_file_errors():
    # Ask the user for the filename
    input_filename = input("Enter the filename you want to read: ")

    try:
        # Attempt to open the file
        with open(input_filename, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except IOError:
        print(f"Error: An error occurred while reading the file.")

def main():
    # Ask user for the input and output filenames
    input_filename = input("Enter the filename to read: ")
    output_filename = input("Enter the filename to write to: ")
    
    # Step 1: Handle file reading and modification
    read_and_modify_file(input_filename, output_filename)
    
    # Step 2: Handle file error checking
    handle_file_errors()

if __name__ == "__main__":
    main()
