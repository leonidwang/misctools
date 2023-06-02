#!/bin/bash
# Assume you have an interactive program $your_program
# It accepts stdin and sends response to stdout.
# This simple script will setup a named pipe so that you can test it in batch
# The inputs will be read from $input_dir, assuming a .txt file
# Each output from the input will be write to $output_dir with _output append to the basename.

# Create a named pipe
mkfifo mypipe

# Start your program in the background, reading from the named pipe
./your_program < mypipe &

# Directory where your input files are stored
input_dir="/path/to/input/files"

# Directory where you want to store output files
output_dir="/path/to/output/files"

# Loop over all input files in the directory
for input_file in "$input_dir"/*.txt
do
  # Extract the base name of the file (without the directory or extension)
  base_name=$(basename "$input_file" .txt)

  # Feed the input file to your program through the named pipe, and capture the output
  cat "$input_file" > mypipe > "$output_dir/$base_name"_output.txt
done

# Clean up the named pipe
rm mypipe
