# Prog07: Create a program that ask the user to input a complete 
# statement. Print the number of words in the input.

# Example:
# Input: We will weather the weather whatever the weather whether we like it or not
# Output: 14

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that counts the number of words in user input.
# - Scope: Command-line application that accepts a statement and outputs the word count.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept a complete statement from the user via command line
#     - Count the number of words in the input
#     - Handle multiple spaces between words correctly
#     - Display the word count

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input user's complete statement
#     2. Split the input by whitespace and count the resulting items
#     3. Display number of words in the statement

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Program to count the number of words in user input
statement = input("Enter a complete statement: ")
word_count = len(statement.split())
print(f"Output: {word_count}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "We will weather the weather whatever the weather whether we like it or not"
# - Expected Output: 14

# Test Case 2:
# - Input: "Hello! Mike Kaizen"
# - Expected Output: 3

# Test Case 3:
# - Input: "John Mike is grinding so hard in python codes."
# - Expected Output: 9

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 5

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike