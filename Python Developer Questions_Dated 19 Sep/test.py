# File path
file_path = "example.txt"

# Read the existing content from the file
with open(file_path, "r") as file:
    existing_content = file.read()
    print("Existing content:\n", existing_content)

# Modify the content
modified_content = existing_content.replace("old", "new")

# Write the modified content back to the file
with open(file_path, "w") as file:
    file.write(modified_content)

print("Content modified and written to the file successfully.")
