# takes T and Z out of timezone
# adds microseconds to timezone, if not already included
# changes timezone from UTC to EST

import pandas as pd
import pytz
from datetime import datetime
import time

# Initial processing to remove 'T' and 'Z' from timestamps
def remove_tz_characters(input_csv, output_csv, timestamp_column):

    # specify data type for all columns as string using dtype function
    df = pd.read_csv(input_csv, dtype=str) # make sure to update to correct source file

    ######### CHARACTER DELETE #########
    # change the T and Z to blanks
    df[timestamp_column] = df[timestamp_column].str.replace("T", " ")
    df[timestamp_column] = df[timestamp_column].str.replace("Z", " ")

    # saves changed CSV file
    df.to_csv(output_csv, index=False) # saves without index number, make sure to update to correct end name
    print(f'T and Z characters removed in {output_csv}')

# Correct timestamps to ensure they include microseconds
def correct_timestamps(input_csv, output_csv, timestamp_column):
    # Read the CSV file
    df = pd.read_csv(input_csv)
    
    # Function to correct a single timestamp
    def correct_timestamp(timestamp):
        # Strip any leading/trailing whitespace
        timestamp = timestamp.strip()
        # Check if the timestamp includes microseconds
        if '.' not in timestamp:
            # Append microseconds if missing
            timestamp += '.000'
        else:
            # Ensure microseconds are in the correct format
            parts = timestamp.split('.')
            if len(parts[1]) < 6:
                parts[1] = parts[1].ljust(6, '0')
            timestamp = '.'.join(parts)
        return timestamp
    
    # Apply the correction function to the timestamp column
    df[timestamp_column] = df[timestamp_column].apply(correct_timestamp)
    
    # Write the corrected data back to a new CSV file
    df.to_csv(output_csv, index=False)
    print(f'Microseconds appended in {output_csv}')

# Convert corrected UTC timestamps to EST
def convert_utc_to_est(input_csv, output_csv, timestamp_column):
    # Read the CSV file
    df = pd.read_csv(input_csv)
    
    # Define timezones
    utc = pytz.utc
    est = pytz.timezone('US/Eastern')
    
    # Function to convert a single timestamp
    def convert_timestamp(utc_timestamp):
        # Parse the timestamp string into a datetime object
        utc_dt = datetime.strptime(utc_timestamp.strip(), '%Y-%m-%d %H:%M:%S.%f')
        
        # Localize the datetime object to UTC
        utc_dt = utc.localize(utc_dt)
        
        # Convert the datetime object to EST
        est_dt = utc_dt.astimezone(est)
        
        # Return the datetime object as a string
        return est_dt.strftime('%Y-%m-%d %H:%M:%S.%f')
    
    # Apply the conversion function to the timestamp column
    df[timestamp_column] = df[timestamp_column].apply(convert_timestamp)
    
    # Write the converted data back to a new CSV file
    df.to_csv(output_csv, index=False)
    print(f'Time zone changed from UTC to EST in {output_csv}')

# Conversion of original ADC measured values to actual current values, in Amperes (A)
def actual_current(input_csv, output_csv, current_column):
    # read through csv data 
    df = pd.read_csv(input_csv)

    # Function to apply the current formula to each value
    def current_formula(x):
        return (25 / 8) * (x - 4)
    
    # Apply the formula to the specified column
    df[current_column] = df[current_column].astype(float).apply(current_formula)

    # Save the modified DataFrame to a new CSV file
    df.to_csv(output_csv, index=False)
    print(f'Current values converted in {output_csv}')


# set up to determine processing time
t = time.process_time()

# Adjust to proper parameters
input_csv = '/Users/cj/Library/CloudStorage/Box-Box/Purdue-Tuskegee/Birck_plasma_etcher_monitoring/plasma_data/Raw_Data/Conversions/PhaseACopy.csv'
intermediate_csv_1 = 'intermed_1.csv'
intermediate_csv_2 = 'intermed_2.csv'
intermediate_csv_3 = 'intermed_3.csv'
output_csv = 'PhaseA_Formatted.csv'
timestamp_column = 'time' 
current_column = 'value'

print(" ")

# Remove 'T' and 'Z' characters
remove_tz_characters(input_csv, intermediate_csv_1, timestamp_column)

# Correct timestamps first
correct_timestamps(intermediate_csv_1, intermediate_csv_2, timestamp_column)

# Convert timestamps from UTC to EST
convert_utc_to_est(intermediate_csv_2, intermediate_csv_3, timestamp_column)

# Convert measured ADC current values to actual current values
actual_current(intermediate_csv_3, output_csv, current_column)

# Print how long calculations took
elapsed_time = time.process_time() - t
print("The entire operation took", elapsed_time, "seconds.")