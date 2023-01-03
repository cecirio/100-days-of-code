# Day 1 - Working with Variables in Python to Manage Data

## Band Name Generator

![](band_name_generator.gif)

[Replit (@RD3NI) - Band Name Generator](https://replit.com/@RD3NI/band-name-generator?v=1)

## Exercises
### Exercise 1 - Printing
**Instructions:** 
- Write a program in main.py that prints the same notes from the previous lesson using what you have learnt about the Python print function.

**Output:**
```
Day 1 - Python Print Function
The function is declared like this:
print('what to print')
```
> This is what the output should print

**Code**
<details><summary>Solution</summary>
<p>

```Python
#Write your code below this line 👇
print("Day 1 - Python Print Function\nThe function is declared like this:")
print("print(\'what to print\')")
```
</p>
</details>

#

### Exercise 2 - Debugging Practice
**Instructions:**
- Fix the following code so that it runs without errors.

```Python
#Fix the code below 👇

print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
  print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")
```

**Output:**
```
Day 1 - String Manipulation
String Concatenation is done with the "+" sign.
e.g. print("Hello " + "world")
New lines can be created with a backslash and n.
```
> This is what the output should print

**Code**
<details><summary>Solution</summary>
<p>
  
**Errors Encountered**
  - SyntaxError: invalid syntax
  - IndentationError: unexpected indent
  - SyntaxError: unexpected EOF while parsing
  
```Python
# Missing double quotes before word "Day".
print("Day 1 - String Manipulation")
# Add backslash to escape double quotes within the string or replace outer double quotes with single quotes.
print("String Concatenation is done with the \"+\" sign.")
# Remove extra indentation
print('e.g. print("Hello " + "world")')
# Extra "(" in the beginning of print function
print("New lines can be created with a backslash and n.")
```
</p>
</details>

#

### Exercise 3 - Input Function
**Instructions:**
- Write a program that prints the number of characters in a user's name. 
  > What is a function that calculates the length of a string?
- Functions can be inside other functions.
- Try to not print anything other than the length.
- The program should work with any input length/name.

**Input:**

```
Jim
```

**Output:**

```
3
```

**Code**
<details><summary>Solution</summary>
<p>

```Python
# Write your code below this line 👇
print(len(input("What is your name?"))) 
```
  
</p>
</details>

#

### Exercise 4 - Variables
**Instructions**
- Write a program that switches the values stored in the variables a and b.
- The program should work for different inputs. e.g. any value of a and b.

**Input Example:**

```
a: 7
b: 2
```

**Output Example:**

```
a: 2
b: 7
```

**Code**
<details><summary>Solution</summary>
<p>
   
```Python
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = a  
a = b
b = c 
#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
```
> This one required a great deal of logical thinking (⊙.☉)7 <br>
> (╯°□°）╯︵ ┻━┻

</p>
</details>
