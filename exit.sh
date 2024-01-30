#!/bin/bash

# Read input from standard input (pipe)
read input

# Check the value of input and perform actions accordingly
case "$input" in
  "Enable radio")
    radio-py Fallout && clear
    # Add your code for handling input 0 here
    ;;
  "Log")
    journal && clear
    ;;
  "Manual command input")
    clear
    # Add your code for handling input 2 here
    ;;
  *)
    echo "Input is not 0, 1, or 2."
    ;;
esac
