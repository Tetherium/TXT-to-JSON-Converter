# TXT-to-JSON-Converter

   Explanation of the Code
This Python script reads a text file containing words (one word per line) and converts it into a JSON file. Here's how it works:

 1- Input and Output Files:

The script uses kelimeler.txt as the input file, which should contain one word per line.
It creates an output file named words.json.

 2- Reading the Input File:

The script reads all lines from the input file and strips whitespace from each line.
Empty lines are ignored during this process.

 3- JSON Conversion:

The list of words is encapsulated within a JSON object under the key "words".
The resulting JSON object is formatted with proper indentation for readability.

 4-Writing to the Output File:

The JSON object is written to words.json using UTF-8 encoding, ensuring compatibility with non-ASCII characters.

 5- Success Message:

Once the process is complete, a success message is printed to indicate that the output file has been created.

   How to Use
   
1- Create a text file named kelimeler.txt in the same directory as the script. Add one word per line.

2- Run the script using Python (python script_name.py).

3- After execution, you will find a file named words.json in the same directory. This file will contain the words from the input file structured in JSON format as:


    {
    "words": [
       "word1",
       "word2",
       "word3"
       ]
     }
