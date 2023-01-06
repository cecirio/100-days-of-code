# Day 2 - Understanding Data Types and How to Manipulate Strings

## Tip Calculator

![](tip_calculator.gif)

[Replit (@RD3NI) - Tip Calculator](https://replit.com/@RD3NI/tip-calculator?v=1)

## Exercises
### Exercise 1 - Data Types
**Istructions:**
- Write a program that adds the digits in a 2 digit number.
- The program should work for different inputs. e.g. any two-digit number.
- Find the data type of two_digit_number
- Put subscripting into practice
- Use type conversion

**Input Example:**
```
39
```

**Output Example:**
```
3 + 9 = 12
12
```

**Code**
<details><summary>Solution</summary>
<p>

```Python
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(int(two_digit_number[0]) + int(two_digit_number[1]))
```

</p>
</details>

#

### Exercise 2 - BMI Calculator
**Instructions:**
- Write a program that calculates the Body Mass Index (BMI) from a user's weight and height. 
- The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
- The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

```math
BMI = {weight(kg) \over height^2(m^2)}
```
> NOTE: Convert the result to a whole number.
- Check the data type of the inputs.
- Try to use the exponent operator in your code.
- Remember PEMDAS.
- Remember to convert the result to a whole number (int).

**Input Example:**
```
weight = 80
height = 1.75
```

**Output Example:**
```
80 ÷ (1.75 x 1.75) = 26.122448979591837
26
```
**Code**
<details><summary>Solution</summary>
<p>

```Python
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

h = float(height)
w = int(weight)

r = w / (h ** 2)
result = int(r)

print(result)
```

</p>
</details>

#

### Exercise 3 - Life in Weeks
**Instructions:**
- Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
- Based on an article by Tim Urban: [Your Life in Weeks](https://waitbutwhy.com/2014/05/life-weeks.html).
- It will take your current age as the input and output a message with our time left in this format:
```
You have x days, y weeks, and z months left.
```
> NOTE: x, y and z are replaced with the actual calculated numbers.
- The output should match the Output Example format exactly, even the positions of the commas and full stops.

**Input Example:**
```
56
```

**Output Example:**
```
You have 12410 days, 1768 weeks, and 408 months left.
```
> NOTE: There are 365 days in a year, 52 weeks in a year and 12 months in a year.

**Code**
<details><summary>Solution</summary>
<p>

```Python
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
a = int(age) #years

d = (90 * 365) - (a * 365)
w = (90 * 52) - (a * 52)
m = (90 * 12) - (a * 12)

print(f"You have {d} days, {w} weeks, and {m} months left.")
```

</p>
</details>
