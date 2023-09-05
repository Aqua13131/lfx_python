# Function to replace even occurrences with "pathetic" and odd occurrences with "marvellous"
def replace_even_odd(text):
    words = text.split()
    count_terrible = 0

    for i in range(len(words)):
        if words[i] == "terrible":
            count_terrible += 1
            if count_terrible % 2 == 0:
                words[i] = "pathetic"
            else:
                words[i] = "marvellous"

    return ' '.join(words)

# Read the input file
with open("file_to_read.txt", "r") as file:
    content = file.read()

# Count the occurrences of "terrible"
terrible_count = content.count("terrible")

# Replace even and odd occurrences and write to result.txt
modified_content = replace_even_odd(content)

with open("result.txt", "w") as result_file:
    result_file.write(modified_content)

# Display the total count of "terrible"
print(f"Total occurrences of 'terrible': {terrible_count}")
