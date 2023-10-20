# Day 24 - Files Directories and Paths
## Mail Merge Project

![](mail_merge.gif)


## Exercises
### Open a file
- If a file is opened within python, it must be manually closed as well.
- Otherwise, use the "with" keyword to open a file
- The default mode to open a file is "read" ("r") only.
- To write to a file the "write" ("w") mode has to be enabled. It will replace everything within the file with the new text.
- To add to a file without overwriting the content, use the "append" ("a") mode.
- If you try to open a file that does not exist, only in the "w" mode, the script will create it for you.

**Code**
<details><summary>Solution</summary>
<p>

```Python
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

#OR

with open("my_file.txt") as file:
  contents = file.read()
  print(contents)
```

</p>
</details>


**Code**
<details><summary>Solution</summary>
<p>

```Python
with open("my_file.txt", mode="w") as file:
  file.write("New text.")

#OR

with open("my_file.txt", mode="a") as file:
```

</p>
</details>

#

### Read and Write the High Score to a File in Snake Game
- Add a file named data.txt to the snake_game project folder.
- Edit the scoreboard.py and main.py files to open the data.txt file and retrieve the current high score.
- If the score is surpassed, replace the current high score with the new one by writing to the file.

**Code**
<details><summary>scoreboard.py</summary>
<p>

```Python
class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    with open("data.txt") as data:
      self.high_score = int(data.read())
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(0, 270)
    sef.update_score()


  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open("data.txt", mode="w") as data:
        data.write(f"{self.highs_score}")
    self.score = 0
    self.update_score()
```

</p>
</details>

#

### Complete the Mail Merge Challenge
- Automate the process of writing the same invitation letter for a different guest.
- Replace the placeholder name with each guest's actual name.
- Save each personalized letter to a different file for each person.

**Code**
<details><summary>main.py</summary>
<p>

```Python
PLACEHOLDER = "[name]"

with open("input/names/invited_names.txt") as guest_names:
    guest_list = guest_names.readlines()

  
with open("input/letters/starting_letter.txt") as empty_letter:
    letter = empty_letter.read()
    for guest in guest_list:
        stripped_guest = guest.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_guest)
        with open(f"output/ready_to_send/letter_for_{stripped_guest}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
```

</p>
</details>

#

