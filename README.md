# Day of the Week Calculator

A small Python mini-project that calculates the **day of the week** for a given date.

## Why I Made This

The idea came from watching **The Mentalist**.

I saw Patrick Jane calculate the day of the week mentally, which made me curious about how that was possible.

So I searched for the mathematical formula behind it and decided to see if I could understand it and implement it myself in Python.

Basically:

> The Mentalist: calculates it in his head.
> Me: makes a Python program to do it. 😂

## How It Works

The program asks the user for:

* Day
* Month
* Year

Then it applies a mathematical formula to calculate the corresponding day of the week.

The project uses a list containing the seven days:

```python
days = ["Saturday", "Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday"]
```

The calculated result is then matched with the corresponding day.

## Example

**Input:**

```text
enter the day: 19
choose the month(1-12): 8
enter the year(min: 1000, max: 9999): 2026
```

**Output:**

```text
19 August 2026 is day: Wednesday
```

## Concepts Used

* Python lists
* `for` loops
* `if` statements
* User input
* Input validation
* `try/except`
* Mathematical formulas
* Basic indexing

## Goal

This was mainly a **learning project**.

The goal was not to build a complicated application, but to take something that made me curious, understand the logic behind it, and try to implement it myself without relying on Python's built-in date libraries.

## Future Improvements

Possible improvements:

* Validate whether the entered date actually exists.
* Allow the user to calculate multiple dates without restarting the program.
* Improve the error-handling system.
* Make the interface cleaner.
* Add more date-related features.

## Built With

**Python**
