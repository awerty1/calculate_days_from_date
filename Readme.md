# Calculate days from date

## Descriptions 
Sometimes you need to calculate the number of days to pay for a particular service. 
This can be done with this script to find out the exact date.
You can also set negative numbers from the current date.
Manual input and from a config file are supported.

## HOW TO USE
1. Set the dates in the list `start_dates` from which you want to calculate the date for payment 
in the file `date_calculation_example.py`
2. Set numbers of days in the list `num_days_list` in the file `date_calculation_example.py`
3. Click to **RUN** button


# Program example
## Input from file
```
Do you want to input manually (M) or from a file (F)? F
###################### phone 2 ######################
You have chosen a date: 2023-07-09
Next payment date 2023-10-26 , 27 days have passed!
More than 5 days left before the date
Don't forget to pay, otherwise you'll become poorer
#####################################################

###################### court ######################
You have chosen a date: 2023-07-20
Next payment date 2023-08-14 , 16 days have passed!
After the date 2023-08-14 has passed 1 days!!!
Don't forget to pay, otherwise you'll become poorer
###################################################

###################### payment of taxes ######################
You have chosen a date: 2023-07-09
Next payment date 2023-10-26 , 84 days have passed!
Until the date 2023-10-26 left 4 days!!!
Don't forget to pay, otherwise you'll become poorer
###################################################
```
## Input manually
**Note:** Multiple comma-separated`(,)` values are allowed. All lists must have equal length!
```
Do you want to input manually (M) or from a file (F)? M
Enter a list of start dates (YYYY-MM-DD), separated by a comma(,): 2023-10-01, 2023-10-02
Enter a list of numbers of days, separated by a comma(,): 3, 19, -5
Enter a list of titles, separated by a comma(,): test1, test2

###################### test1 ######################
You selected 3 days from the date 2023-10-01
Next payment date 2023-10-04 , 27 days have passed!
After the date 2023-10-04 has passed 24 days!!!
Don't forget to pay, otherwise you'll become poorer
###################################################


###################### test2 ######################
You selected 19 days from the date 2023-10-02
Next payment date 2023-10-21 , 26 days have passed!
After the date 2023-10-21 has passed 7 days!!!
Don't forget to pay, otherwise you'll become poorer
###################################################
```
# TESTS
The test file is located in the `test` folder. It is called `test_code.py`


# TODO BLOCK
1. Email msgs
2. Add profile to binary file(.spec pyinstaller) +
3. Calculate days until date
4. Add msg file for msg in the main +
5. Add a description to each event date
6. Change "date_calculation_example.py" to "date_calculation_example.json"
7. Added to file frm manual input (need thinking)
8. Added logging
9. Optimize and refactoring main.py file (double msg + output_file.write) +