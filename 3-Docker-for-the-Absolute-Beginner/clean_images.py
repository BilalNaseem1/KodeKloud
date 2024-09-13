import re
import glob

# Get a list of all markdown files in the current directory
markdown_files = glob.glob("*.md")

for file_name in markdown_files:
    # Read the content of the file
    with open(file_name, "r") as file:
        content = file.read()

    # Replace "image*" with "images/image*"
    updated_content = re.sub(r'\bimage([^\s]*)', r'images/image\1', content)

    # Write the updated content back to the file
    with open(file_name, "w") as file:
        file.write(updated_content)

    print(f"Replacements done successfully for {file_name}.")
