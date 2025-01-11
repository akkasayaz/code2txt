import os
import sys

def process_python_files(root_dir, output_file):
    with open(output_file, 'w') as txt_file:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith('.py'):
                    full_path = os.path.join(dirpath, filename)
                    relative_path = os.path.relpath(full_path, root_dir)
                    
                    with open(full_path, 'r') as py_file:
                        content = py_file.read()
                    
                    txt_file.write(f"# {relative_path}\n")
                    txt_file.write(content)
                    txt_file.write("\n\n")  # Add spacing between files

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print("Error: Please provide a valid directory path")
        sys.exit(1)
    
    output_file = "python_files.txt"
    process_python_files(folder_path, output_file)
