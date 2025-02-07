#!/usr/bin/env python
# coding: utf-8

# <img src="materials/images/introduction-to-python-cover.png"/>

# 
# # 👋 Welcome, before you start
# <br>
# 
# ### 📚 Module overview
# 
# Python provides excellent functionality and extensibility to make working with data efficient and even fun! Python is very human-readable and can be picked up relatively quickly. We will go through three lessons with you:
# 
# - <font color=#E98300>**Lesson 1: Python Data Types**</font>    `📍You are here.`
#     
# - [**Lesson 2: Python Data Structures**](Lesson_2_Python_Data_Structures.ipynb)
#     
# - [**Lesson 3: Functions**](Lesson_3_Functions.ipynb)
# 
# </br>
# 
# ### ✅ Exercises
# We encourage you to try the exercise questions in this module, and use the [**solutions to the exercises**](Exercise_solutions.ipynb) to help you study.
# 
# </br>
# 
# <div class="alert alert-block alert-info">
# <h3>⌨️ Keyboard shortcut</h3>
# 
# These common shortcut could save your time going through this notebook:
# - Run the current cell: **`Enter + Shift`**.
# - Add a cell above the current cell: Press **`A`**.
# - Add a cell below the current cell: Press **`B`**.
# - Change a code cell to markdown cell: Select the cell, and then press **`M`**.
# - Delete a cell: Press **`D`** twice.
# 
# Need more help with keyboard shortcut? Press **`H`** to look it up.
# </div>

# ---

# # Lesson 1: Python Data Types

# In this lesson, you’ll learn about the different types of data you can work with in Python:
# 
# - [Numbers](#Numbers-(Integers,-Floats))
# - [Comments](#Comments)
# - [Strings](#Strings)
# - [Variables](#Variables)
# - [Booleans](#Booleans)
# 

# `🕒 This module should take about 30 minutes to complete.`
# 
# `✍️ This notebook is written using Python.`

# ---

# ## Numbers (Integers, Floats)

# - **Integers** are whole numbers.
# - **Floats** are decimal numbers.
# 
# 
# 
# Expression |<p style='text-align:left'>Description</p> | Result
# :------------: |------------ | :-------------
# 3 + 2 |<p style='text-align:left'>Addition</p> | <p style='text-align:center'>5</p>
# 3 - 2 |<p style='text-align:left'>Subtraction</p> | <p style='text-align:center'>1</p>
# 3 * 2|<p style='text-align:left'>Multiplication</p> | <p style='text-align:center'>6</p>
# 3 / 2|<p style='text-align:left'>Division</p> | <p style='text-align:center'>1.5</p>
# 3 // 2|<p style='text-align:left'>Floor Division</p> | <p style='text-align:center'>1</p>
# 3 % 2|<p style='text-align:left'>Modulus/Remainder</p> | <p style='text-align:center'>1</p>
# 3 ** 2|<p style='text-align:left'>Exponent</p>| <p style='text-align:center'>9</p>

# <div class="alert alert-block alert-success">
# <b>Keep in mind:</b> The spacing in these examples has no effect on how Python evaluates the expressions; it may simply help the code to be easier to read. 
# </div>

# ### ✅ `Run` each of the cells below:

# In[1]:


3 + 2


# In[2]:


3 - 2


# In[3]:


3 * 2


# In[4]:


3/2


# In[5]:


# Floor division: returns only the whole part following division

3//2


# In[6]:


# Modulus: returns the remainder after division

3%2


# In[7]:


# Exponent

3**2


# When you divide any two numbers, even if they are integers that result in a whole number, you’ll always get a float:

# In[8]:


4/2


# When you mix an integer and a float in an operation, Python will always return a float:

# In[9]:


4 + 2.0


# ### ✅ Add a new cell below this one, and `Run` the following mathematical operation: 
# ```5 times 6 divided by 3``` 
# ```The output should be: 10.0```

# ---

# ## Comments

# You may have noticed the use of comments above. A comment is text in a code cell that is to be ignored. A comment, in Python, is preceded by a hash symbol.
# 
# ### ✅ `Run` the code cell below, as is. Then, remove the hash symbol preceding the last line and rerun the cell.

# In[10]:


# This line will be ignored. 
# The following line is code that is commented out so that it will be ignored, until uncommented:

#3 + 2


# Comments are useful for annotating your code in plain English. It's a good habit to frequently add notes to your code that describe your thinking, your approach to solving a problem, or even as a TODO list. 

# <div class="alert alert-block alert-info">
# <b>Tip:</b> As you're learning Python, use comments to take notes to remember key concepts 
#     and to enhance your understanding.
# </div>

# ---

# ## Strings

# A string is a sequence of characters. Anything inside quotes is considered a string in Python. You can use single or double quotes around strings.

# In[11]:


# Single or double quotes are fine.

'This is fun!'


# In[12]:


# If an apostrophe is used, then double quotes are required.

"Isn't this fun?"


# Strings can be combined (concatenated) by placing a "+" between them:

# In[13]:


"The wonderful world of " + "Python!"


# ---

# ## Print
# So far, the result of the code that we've written was automatically returned as output for us to see. This is because Jupyter Notebook is an interactive environment and, by default, sends its results to the output to be viewed. However, as you write more code, there will be times when this won't be the case. That's when you can use the **print()** function to command it to "print" its contents to the screen.

# In[14]:


print(4 + 2.0)


# In[15]:


print("Coding in Python...")


# We'll discuss more about the use of the print function below.

# ---

# ## Variables
# A variable is a named value. In other words, if we assign the value "Hello Python!" to the variable **_greeting_**, we can type in **_greeting_** to have the value "Hello Python!" returned:

# In[16]:


greeting = "Hello Python!"
print(greeting)


# You can change the value of a variable at any time, and Python will always keep track of its current value.

# In[17]:


greeting = "Welcome to Jupyter Notebook!"
print(greeting)


# ### Naming variables
# 
# When naming variables in Python you must keep a few rules and guidelines in mind:
# 
# **Variables:**
#    - can only be one word
#    - can use only letters, numbers, and the underscore (_) character
#    - can’t begin with a number
#    - are case-sensitive (data, Data and DATA would be different variable names)
#    
#    For example:
#    
#    ``` python
#    first_month_of_year = "January"
#    id_007 = "j_bond"
#     
#     ```

# In[18]:


# Using variables

number_of_participants = 50
cost_per_participant = 100
study_expense = number_of_participants * cost_per_participant

print(study_expense)


# ### Print formatting

# There will be times when you'll want to provide more context to your output than just the  value of a variable. In these instances, you can use what's known as **_print formatting_** to place the value within a larger string. Typically, the string will provide more context to the outputted variable.
# 
# To use print formatting, insert the base string inside the print function. Place curly braces where you would like a variable's value to be placed. Add the dot format to the end of the string, with your variables in respective order within the format method, separated by a comma. Python will replace the curly braces with the respective variable's value and display the results.

# In[19]:


apparatus = "wearable device"
cost = 299

print("The cost of the {} for each participant will be ${}.".format(apparatus, cost))


# ### f-string 

# Similar to print formattng, we can also use what's known as an **_f-string_** in Python (for formatted string) to include a variable's value inside of a string.
# 
# To have a variable’s value inserted within a string, place the letter **_f_** immediately before the opening quotation mark of the string. Within the quotation marks, place curly braces where you would like for the variable  to appear within the string, and place the variable within the curly braces. Python will then replace the variable with its value when the string is displayed:

# In[20]:


f"The cost of the study will be: ${study_expense}"


# ### Multiple variable assignment (Unpacking)

# As a convenience in Python, you can assign values to multiple variables at the same time, using just one line of code. This is known in Python as "unpacking".
# 
# For example:

# In[21]:


apples, bananas, oranges = 2, 3, 4
print(bananas)


# To use unpacking, be sure to separate the variable names with commas, and do the same with the values. Python will then assign each value to its respectively positioned variable. This will work as long as the number of values matches the number of variables.

# ### Constants
# A constant is a variable whose value should never change. In Python, use all capital letters to indicate that a variable should be treated as a constant and thus never be changed:
# 
# ```python
# MINUTES_IN_DAY = 1440
# ```

# ---

# ## Booleans

# The Boolean data type can be either True or False. It is typically used  with conditional expressions which we will explore shortly.
# 
# `True` and `False` are reserved words in Python of type Boolean.

# In[22]:


True


# In[23]:


False


# The numerical value of True is 1 and of False is 0.

# In[24]:


int(True)


# In[25]:


int(False)


# <div class="alert alert-block alert-info">
# <b>Tip:</b> You can convert a value to become an integer 
# by wrapping the value inside the int() function. This is known as casting. This can be convenient when you'd like,
# for example, to convert the float 1.0 to the integer 1. Just cast it: int(1.0) will return the integer 1. It's also conveniently used to round a number down. For example, the value 12.304 can be cast to the integer 12 using int(12.304).
# </div>

# ### Boolean Operators (and, or, not)
# When working with compound conditions, if "and" is used, then both tests must be True for the statement to return True.

# In[26]:


True and True


# In[27]:


True and False


# If "or" is used in the compound statement, then only one condition needs to be True for the statement to return True.

# In[28]:


True or False


# If "not" is used, then the condition returns the opposite value.

# In[29]:


not False


# ### Comparison Operators
# 
# Expression |<p style='text-align:left'>Description </p> | Result
# :------------: |------------ | :-------------
# 1 < 2 |<p style='text-align:left'>Less Than </p> | True
# 1 > 2 |<p style='text-align:left'>Greater Than </p> | False
# 1 <= 2|<p style='text-align:left'> Less Than Or Equal To </p>| True
# 1 >= 2|<p style='text-align:left'>Greater Than Or Equal To</p> | False
# 1 == 2|<p style='text-align:left'>Equivalent To</p> | False
# 1 != 2|<p style='text-align:left'>Not Equal To</p> | True

# ### ✅ `Run` each of the cells below:

# Numerical comparison:

# In[30]:


1 < 2


# In[31]:


1 > 2


# In[32]:


1 <= 2


# In[33]:


1 >= 2


# In[34]:


1 == 2


# In[35]:


1 != 2


# String comparison:

# In[36]:


"string" == "string"


# In[37]:


"string" == 'spring'


# 
# <div class="alert alert-block alert-warning">
# <b>Alert:</b> Note the use of the double equal sign above. Keep in mind that a double equal sign asks a question whereas a single equal sign is really a statement. Understanding this can avoid a common mistake.
#     
# The use of a double equal sign is for performing a comparison, to determine if what's on the right is equivalent to what's on the left. 
#     
# The use of a single equal sign is for performing assignment which means that you need a variable on the left side to perform the assignment of the value on the right side. The use of a single equal sign in the above example would indicate assignment and result in an error message.  
# </div>
# 

# <div class="alert alert-block alert-info">
# <b>Tip:</b> String comparison can be useful, for example, when comparing if the text a person entered is equaivalent to the saved password.
# </div>

# ---

# 
# 
# ---
# 
# 
# 
# ---
# 
# 

# # 🌟 Ready for the next one?
# <br>
# 
# - [**Lesson 2: Python Data Structures**](Lesson_2_Python_Data_Structures.ipynb)
#     
# - [**Lesson 3: Functions**](Lesson_3_Functions.ipynb)

# ---

# # Contributions & Acknowledgement

# Thanks Antony Ross for his diligent and thoughtful work in crafting the content for this notebook.

# -----

# Copyright (c) 2022 Stanford Data Ocean (SDO)
# 
# All rights reserved.
