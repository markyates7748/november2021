## rank file in descending order by time
## select latest file
## ensure latest file has a diffence of more than 500 lines compared to the next latest file

# import needed packages
import numpy as np
import pandas as pd
import regex as re
import os, logging, phonenumbers
import matplotlib.pyplot as plt
from datetime import datetime as dt
from validate_email import validate_email

# function to check if state is valid
def check_state(check_me):
    valid_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    is_valid = False
    for state in valid_states:
        if check_me == state:
            is_valid = True
            break
    return is_valid

# set up logging
logging.basicConfig(level=logging.INFO, filename="agents_log.log", filemode="a", format="%(asctime)s - [%(levelname)s ] - %(message)s", datefmt="%Y/%m/%d %H:%M:%S")

logging.info("Starting NYL agent file processing")

# create empty list for files
found_files = []

# extract all relevant csv files
logging.info("Attempting to access C:/Users/myate/git/november2021/python_basics/panda_weekend_project_files directory")
try:
    with os.scandir("C:/Users/myate/git/november2021/python_basics/panda_weekend_project_files") as files:
        logging.info("Directory opened. Searching for relevent files")
        for file in files:
            if "NYL" and ".csv" in file.name:
                found_files.append(file.name)
        logging.info(f"Found the following files: {found_files}")

    # sort in descending order by date
    # process: remove all non-numeric symbols, parse remaining numbers as datetime object, sort by reverse date value
    found_files.sort(key = lambda date: dt.strptime(re.sub(r"[^0-9]","",date),"%Y%m%d"), reverse=True)
    logging.info(f"sorted files by date: {found_files}")

    # check latest file has at least 500 more lines than previous file
    logging.info("Checking latest file is sufficiently different")
    latest_file = pd.read_csv(found_files[0])
    check_previous_file = len(pd.read_csv(found_files[1]))

    if abs(check_previous_file - len(latest_file)) < 500:
        logging.info("Latest file is significantly different. Checking NYL.lst if file was previously processed")
        # bool to check process status
        already_processed = False
        try:
            f = open("NYL.lst", "r")
            # check for filename in list of already processed files
            for line in f:
                if line == found_files[0]:
                    print("file already processed")
                    logging.error("Latest file has already been processed")
                    already_processed = True
                    break
            f.close()
            # if not processed, process
            if not already_processed:
                logging.info("Latest file has not yet been processed. Beginning processing")
                ## Processing File
                latest_file.info()
                # replace incorrect headers with correct headers
                logging.info("Ensuring correct Contract header names")
                latest_file = latest_file.rename({"Agent Writing Contract Start Date (Carrier appointment start date)" : "Agent Writing Contract Start Date"}, axis=1)
                latest_file = latest_file.rename({"Agent Writing Contract Status (actually active and cancelled\"s should come in two different files)" : "Agent Writing Contract Status"}, axis=1)
                
                # check valid phone numbers
                logging.info("Checking for invalid phone numbers")
                for phone_number in latest_file["Agency Phone Number"]:
                    try:
                        if not phonenumbers.is_valid_number(phonenumbers.parse(re.sub(r"[.]"," ",phone_number), "US")):
                            logging.info(f"Validation for '{phone_number}' failed: invalid number")
                    except Exception as e:
                        if phone_number.strip() != "":
                            logging.error(f"Error with the number '{phone_number}'", exc_info=True)
                for phone_number in latest_file["Agent Phone Number"]:
                    try:
                        if not phonenumbers.is_valid_number(phonenumbers.parse(re.sub(r"[.]"," ",phone_number), "US")):
                            logging.info(f"Validation for '{phone_number}' failed: invalid number")
                    except Exception as e:
                        if phone_number.strip() != "":
                            logging.error(f"Error with the number '{phone_number}'", exc_info=True)
                            
                # check valid US states
                logging.info("Checking for invalid States")
                for state in latest_file["Agency State"]:
                    if not check_state(state):
                        logging.info(f"Validation for '{state}' failed: invalid state")
                for state in latest_file["Agent State"]:
                    if not check_state(state):
                        logging.info(f"Validation for '{state}' failed: invalid state")

                # check valid email address
                logging.info("Checking for invalid email addresses")
                for email in latest_file["Agent Email Address"]:
                    validate_email(email_address=email, check_format=True, check_blacklist=False, check_dns=False, check_smtp=False)

                # create dataframe with headers as index and data as rows
                logging.info("Creating new dataframe with headers as indices")
                new_df_0 = pd.MultiIndex.from_frame(latest_file)
                print(new_df_0)

                # create new dataframe which groups agents by Agency State
                logging.info("Grouping Agent Id by Agency State")
                new_df_1 = pd.DataFrame(latest_file.groupby(["Agency State"])["Agent Id"])
                print(new_df_1)

                # create new dataframe with Agent Name, Agent Writing Contract Start Date, Date when an agent became A20
                logging.info("Creating new DataFrame with Agent Last Name, Contract Start Date, Date of Becoming A2O")
                new_df_2 = latest_file[["Agent Last Name", "Agent Writing Contract Start Date", "Date when an agent became A2O"]]
                print(new_df_2)

                # create data visualization with first two dataframes
                logging.info("Creating histogram with number of agents in each state")
                try:
                    hist_df = pd.DataFrame(latest_file["Agency State"].value_counts())
                    hist_df.hist(column="Agency State")
                    plt.show()
                except Exception as e:
                    logging.error('Error creating histogram', exc_info=True)

                # append filename to list of processed files
                logging.info("Recording file as processes in NYL.lst")
                try:
                    with open("NYL.lst", "a") as f:
                        f.write(found_files[0])
                    f.close()
                except Exception as e:
                    logging.error("Error recording to NYL.lst", exc_info=True)
        except Exception as e:
            print("error opening NYL.lst")
            logging.error("Error opening NYL.lst", exc_info=True)
    else:
        print("insignificant difference between files")
        logging.error("Latest file is not significantly different")
except Exception as e:
    print("error opening directory")
    logging.error("Error opening directory", exc_info=True)

logging.info("Ending NYL agent processing")

