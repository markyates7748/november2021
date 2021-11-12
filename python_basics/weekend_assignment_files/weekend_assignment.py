from openpyxl import load_workbook
import datetime
import logging

logging.basicConfig(level=logging.INFO, filename="assignment_log.log", filemode='w', format='%(process)d - [%(levelname)s ] - %(message)s')

logging.info('Starting weekend assignment program')

## January Data
january_filename = "expedia_report_monthly_january_2018.xlsx"
logging.info(f'opening {january_filename}')
try:
    january_workbook = load_workbook(january_filename)
    logging.info(f'getting {january_filename} sheets')
    try:
        january_summary_sheet = january_workbook["Summary Rolling MoM"]
        january_voc_sheet = january_workbook["VOC Rolling MoM"]
    except Exception as e:
        logging.error(f'error getting {january_filename} sheets', exc_info=True)

    #January Summary Data
    january_summary_data = {}

    logging.info(f'extracting {january_summary_sheet} sheet data')
    try:
        for row in january_summary_sheet.iter_rows(min_row=2, max_row=13, min_col=1, max_col = 6, values_only=True):
            data_id = row[0].date().isoformat()
            datum = {
                "Calls Offered" : row[1],
                "Abandon after 30s" : row[2],
                "FCR" : row[3],
                "DSAT" : row[4],
                "CSAT" : row[5]
            }
            january_summary_data[data_id] = datum
        logging.info(f'{january_summary_sheet} data extraction completed')

        #print all subentries of given date
        given_date = "2018-01-01"
        logging.info(f'searching extracted data for {given_date}')
        for data_id, data_values in january_summary_data.items():
            if data_id == given_date:
                print(data_id)
                for key in data_values:
                    if key == "Calls Offered":
                        print(key + ':', data_values[key])
                    else:
                        print(key + ':', data_values[key]*100 ,'%')
        logging.info(f'data for {given_date} found')
    except Exception as e:
        logging.error(f'error extracting data from {january_summary_sheet}', exc_info=True)
    

    #January VOC data
    january_voc_data = {}

    logging.info(f'extracing {january_voc_sheet} sheet data')
    try:
        for column in january_voc_sheet.iter_cols(min_row=1, max_row=19, min_col=2, max_col=24, values_only=True):
            data_id = column[0].date().isoformat()
            datum = {
                "Base Size" : column[2],
                "Promoters Total" : column[3],
                "Promoters Percent" : column[4],
                "Passives Total" : column[5],
                "Passives Percent" : column[6],
                "Detractors Total" : column[7],
                "Detractors Percent" : column[8],
                "Overall NPS Percent" : column[12],
                "Sat with Agent Percent" : column[15],
                "DSat with Agent Percent" : column[18]
            }
            january_voc_data[data_id] = datum
        logging.info(f'{january_voc_sheet} data extraction completed')

        #print all subentries of given date
        given_date = "2018-01-01"
        logging.info(f'searching extracted data for {given_date}')
        for data_id, data_values in january_voc_data.items():
            if data_id == given_date:
                print(data_id)
                for key in data_values:
                    if "Percent" in key:
                        print(key + ':', data_values[key]*100 ,'%')
                    else:
                        print(key + ':', data_values[key])
        logging.info(f'data for {given_date} found')
        print('')
    except Exception as e:
        logging.error(f'error extracting data from {january_voc_sheet}', exc_info=True)
except Exception as e:
    logging.error(f'error opening {january_filename}', exc_info=True)


## March Data
march_filename = "expedia_report_monthly_march_2018.xlsx"
logging.info(f'opening {march_filename}')
try:
    march_workbook = load_workbook(march_filename)
    logging.info(f'getting {march_filename} sheets')
    try:
        march_summary_sheet = march_workbook["Summary Rolling MoM"]
        march_voc_sheet = march_workbook["VOC Rolling MoM"]
    except Exception as e:
        logging.error(f'error getting {march_filename} sheets', exc_info=True)

    #march Summary Data
    march_summary_data = {}

    logging.info(f'extracting {march_summary_sheet} sheet data')
    try:
        for row in march_summary_sheet.iter_rows(min_row=2, max_row=13, min_col=1, max_col = 6, values_only=True):
            data_id = row[0].date().isoformat()
            datum = {
                "Calls Offered" : row[1],
                "Abandon after 30s" : row[2],
                "FCR" : row[3],
                "DSAT" : row[4],
                "CSAT" : row[5]
            }
            march_summary_data[data_id] = datum
        logging.info(f'{march_summary_sheet} data extraction completed')

        #print all subentries of given date
        given_date = "2018-03-18"
        logging.info(f'searching extracted data for {given_date}')
        for data_id, data_values in march_summary_data.items():
            if data_id == given_date:
                print(data_id)
                for key in data_values:
                    if key == "Calls Offered":
                        print(key + ':', data_values[key])
                    else:
                        print(key + ':', data_values[key]*100 ,'%')
        logging.info(f'data for {given_date} found')
    except Exception as e:
        logging.error(f'error extracting data from {march_summary_sheet}', exc_info=True)
    

    #march VOC data
    march_voc_data = {}

    logging.info(f'extracing {march_voc_sheet} sheet data')
    try:
        for column in march_voc_sheet.iter_cols(min_row=1, max_row=19, min_col=2, max_col=24, values_only=True):
            #March 2018 voc sheet is slightly different from January 2018 voc sheet
            if type(column[0]) == datetime:
                data_id = column[0].date().isoformat()
            else:
                data_id = column[0]
            datum = {
                "Base Size" : column[2],
                "Promoters Total" : column[3],
                "Promoters Percent" : column[4],
                "Passives Total" : column[5],
                "Passives Percent" : column[6],
                "Detractors Total" : column[7],
                "Detractors Percent" : column[8],
                "Overall NPS Percent" : column[12],
                "Sat with Agent Percent" : column[15],
                "DSat with Agent Percent" : column[18]
            }
            march_voc_data[data_id] = datum
        logging.info(f'{march_voc_sheet} data extraction completed')
        #print all subentries of given date
        given_date = "2018-03-18"
        logging.info(f'searching extracted data for {given_date}')
        for data_id, data_values in march_voc_data.items():
            if data_id == given_date or data_id == "March":
                print(data_id)
                for key in data_values:
                    if "Percent" in key:
                        print(key + ':', data_values[key]*100 ,'%')
                    else:
                        print(key + ':', data_values[key])
        logging.info(f'data for {given_date} found')
        print('')
    except Exception as e:
        logging.error(f'error extracting data from {march_voc_sheet}', exc_info=True)
except Exception as e:
    logging.error(f'error opening {march_filename}', exc_info=True)
