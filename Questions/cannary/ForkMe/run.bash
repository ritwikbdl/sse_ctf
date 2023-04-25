#!/bin/bash

# Run the python script solve.py with input 104 and save this out put in a variable called result

result=$(echo 104 | python solve.py)
#echo $result
# check if the result contains the string  stack smashing detected ***: terminated
if [[ $result == *"stack smashing detected ***: terminated"* ]]; then
    echo "Stack smashing detected"
else
    echo "No stack smashing detected"
fi


