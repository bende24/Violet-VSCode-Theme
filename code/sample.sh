#!/bin/bash

echo "Hello, World!"

x=10
y=20
sum=$((x + y))
echo "Sum: $sum"

numbers=(1 2 3)
for number in "${numbers[@]}"; do
    echo "Number: $number"
done

# Conditional statements
if [ $x -eq 10 ]; then
    echo "x is 10"
else
    echo "x is not 10"
fi

# Functions
function greet {
    local name=$1
    echo "Hello, $name!"
}

greet "Alice"

# Reading input
read -p "Enter your name: " user_name
echo "Hello, $user_name!"
