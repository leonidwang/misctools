# misctools
Collection of random handy tools.

# Python
## cmdline-selection.py
This script uses the prompt_toolkit library to allow the user to interactively select strings from a list using a radio list or a checkbox list. 
Functions:
- select_from_radiolist(strings): 
    Prompts the user to select a single string from a list using a radio list. Returns the selected string.

- select_from_checkboxlist(strings): 
    Prompts the user to select one or more strings from a list using a checkbox list. Returns a list of selected strings.

## ping-network.py
Python script to ping all IPs in a range and report result(up/down) in a table.
- Ping each IP 3 times.
- 0 packet loss means it's up, otherwise it's down.
- multiprocess is used to do it in parallel.

## treemap.py
Parses letters in a file and present the occurances in a treemap.
- An interactive treemap will be rendered in web browser.
- An image file will be saved locally too.

The sample program parses itself.

# Bash
## namedpipe.sh
Assume you have an interactive program `your_program` which accepts stdin and sends response to stdout.
This simple script will setup a named pipe so that you can test it in batch.
- The inputs will be read from $input_dir, assuming a .txt file.
- Each output from the input will be write to $output_dir with _output append to the basename.