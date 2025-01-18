import re
import hashlib

# Input and output file names
input_file = 'users.sql'
output_file = 'users_hashed.sql'

# Function to hash a given password with MD5
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Read the input file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Process each line and replace the password with its MD5 hash
updated_lines = []
for line in lines:
    match = re.match(r"insert into users \(name, email, password\) values \('.*?', '.*?', '(.*?)'\);", line)
    if match:
        original_password = match.group(1)
        hashed_password = hash_password(original_password)
        updated_line = line.replace(original_password, hashed_password)
        updated_lines.append(updated_line)
    else:
        updated_lines.append(line)  # Keep the line unchanged if no match

# Write the updated SQL statements to the output file
with open(output_file, 'w') as file:
    file.writelines(updated_lines)

print(f"Passwords have been hashed and saved to {output_file}")
