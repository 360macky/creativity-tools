# Get the file from arguments
import sys
input_file = sys.argv[1]

# Open the input file in read mode and the output file in write mode
with open(input_file, 'r') as input_file, open('newsubtitles.srt', 'w') as output_file:
    # Iterate over the lines in the input file
    for line in input_file:
        # If the line only contains a number, write a newline character to the output file before the line
        if line.strip().isdigit():
            output_file.write('\n')
        # Write the line to the output file
        output_file.write(line)

