# Days Between Two Dates
A simple python script that counts the number of times each day appears between two given dates.
 
There's a lot of websites that can count the number of days between two given dates but I couldn't find one that counts the number of times every day of the week appears between the two dates. One most likely exists somewhere but since I couldn't find it easily when I looked for it, I made my own.

## Usage

**As a module:** You can import it as a module and use the `count_days(date1, date2)` function, it returns a dictionary with keys being days and their values being the number of times that day appears between the two dates. Eg: `"Saturday": 12`

**By itself (As intended):** You can run the program directly and it'll prompt you to input two dates in the format `YYYY MM DD` and then it will print out the total number of days and how many times each day appears between the dates in a neat format.

## Requirements

- [Python](https://www.python.org/) 3.7 or above.

### Todos

- Make a GUI for it with a date picker.

License
----

The Unlicense