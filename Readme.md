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
====================================================================
 IMPORTANT: Manual input data WILL NOT be saved to the source file!
 Data will only be written to a separate report file.
====================================================================

Do you want to input manually (M) or from a file (F)? (or 'Q' to quit): F

####################### internet #######################
Description: Payment for home internet service
You selected 88 days from the date 2025-07-30
Next payment date 2025-10-26 , 38 days have passed!
More than 5 days left before the date
Don't forget to pay, otherwise you'll become poorer
########################################################


####################### phone #######################
Description: Mobile phone subscription fee
You selected 3 days from the date 2025-09-03
Next payment date 2025-09-06 , 3 days have passed!
Until the date 2025-09-06 left 0 days!!!
Don't forget to pay, otherwise you'll become poorer
#####################################################


####################### payment of taxes #######################
Description: Payment of taxes for 2025
You selected 85 days from the date 2025-06-09
Next payment date 2025-09-02 , 89 days have passed!
After the date 2025-09-02 has passed 4 days!!!
Don't forget to pay, otherwise you'll become poorer
################################################################

Press "Enter" for exit...
```
## Input manually
**Note:** Multiple comma-separated`(,)` values are allowed. All lists must have equal length!
```
====================================================================
 IMPORTANT: Manual input data WILL NOT be saved to the source file!
 Data will only be written to a separate report file.
====================================================================

Do you want to input manually (M) or from a file (F)? (or 'Q' to quit): M

------------------------------------------------
 Notice: Manual input mode selected.
 Results will only be saved to the report file.
 For permanent data storage, use file mode (F).
------------------------------------------------

Enter 'Q' at any time to quit.
Enter a list of start dates (YYYY-MM-DD), separated by a comma(,) (or 'Q' to quit): 2025-10-01, 2025-10-02
Enter a list of numbers of days, separated by a comma(,) (or 'Q' to quit): 3, 19
Enter a list of titles, separated by a comma(,) (or 'Q' to quit): test1, test2
Enter a list of descriptions, separated by a comma(,) (or 'Q' to quit): gfdgdf 1, gfdgdf 2

####################### test1 #######################
Description: gfdgdf 1
You selected 3 days from the date 2025-10-01
Next payment date 2025-10-04 , -25 days have passed!
More than 5 days left before the date
Don't forget to pay, otherwise you'll become poorer
#####################################################


####################### test2 #######################
Description: gfdgdf 2
You selected 19 days from the date 2025-10-02
Next payment date 2025-10-21 , -26 days have passed!
More than 5 days left before the date
Don't forget to pay, otherwise you'll become poorer
#####################################################

Press "Enter" for exit...
```
# TESTS
The test file is located in the `test` folder. It is called `test_code.py`


# TODO BLOCK
1. Email msgs
2. Add profile to binary file(.spec pyinstaller) +
3. Calculate days until date
4. Add msg file for msg in the main +
5. Add a description to each event date +
6. Change "date_calculation_example.py" to "date_calculation_example.json"
7. Added to file frm manual input (need thinking)
8. Added logging
9. Optimize and refactoring main.py file (double msg + output_file.write) +
10. Add quit on hotkey Q +