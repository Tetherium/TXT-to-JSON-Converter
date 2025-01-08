import json

# Name of the input file
input_file = "words.txt"

# Name of the output file
output_file = "words.json"

# Read the text file and convert lines into a list
with open(input_file, "r", encoding="utf-8") as file:
    words = [line.strip() for line in file if line.strip()]

# Convert the list to JSON format and write to the file
with open(output_file, "w", encoding="utf-8") as file:
    json.dump({"words": words}, file, ensure_ascii=False, indent=2)

print(f"{output_file} has been successfully created!")
