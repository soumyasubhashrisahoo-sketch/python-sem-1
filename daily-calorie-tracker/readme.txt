Project Overview

The Daily Calorie Tracker is a beginner-level Python program that allows users to record their daily meals, track calorie intake, and compare it with a daily calorie limit. The purpose of this project is to help users understand how to handle user input, perform calculations, and display formatted output in Python. It also provides a simple example of data storage using lists, conditional statements for comparison, and file handling to save user data. This project demonstrates core programming concepts in a practical, health-related application.

Features

1.Displays a clear and formatted welcome message for the user.

2.Accepts user input for meal names and calorie values.

3.Stores data in two separate lists — one for meal names and one for calorie amounts.

4.Performs calculations for total and average calorie intake.

5.Compares total calorie intake with a user-defined daily limit.

6.Displays a well-formatted report showing each meal, total, average, and calorie limit.

7.Provides a warning message if the calorie limit is exceeded, or a success message if under the limit.

8.Optionally saves the session summary to a text file with a timestamp.



How It Works


1.The user is first greeted with a welcome message and a short description of the program.

2.The user specifies how many meals they want to log.

3.For each meal, the program asks for the meal name and the number of calories consumed.

4.The program stores this information in two lists and performs calculations using built-in Python functions such as sum() and arithmetic operators.

5.The user is then prompted to enter their daily calorie limit.

6.The program compares the total calorie intake with the limit and displays a message indicating whether the user is within or over their limit.

A formatted summary report is printed using f-strings and alignment for clarity.

Finally, the program asks the user if they want to save the report to a file. If the user agrees, the data is written to a text file along with the current date and time.

Example Output
