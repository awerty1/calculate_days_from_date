# Calculate days from date

## Descriptions 
Sometimes you need to calculate the number of days to pay for a particular service. 
This can be done with this script to find out the exact date.
You can also set negative numbers from the current date.

## HOW TO USE
1. Set the dates in the list `start_dates` from which you want to calculate the date for payment 
in the file `date_calculation_example.py`
2. Set numbers of days in the list `num_days_list` in the file `date_calculation_example.py`
3. Click to RUN button

[not relevant] P.S.: Also, you can uncomment the lines and enter `start_date_str` and `num_days` from the console

## Program example
```
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

# TESTS
The test file is located in the `test` folder. It is called `test_code.py`
