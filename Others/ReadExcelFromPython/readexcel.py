


import pandas as pds

uri_excel_path = sys.argv[1]
sys.stdout.reconfigure(enconding='utf-8')
excel_data_df = pandas.read_excel(uri_excel_path, sheet_name='data')
json_str = excel_data_df.to_json(orient='record')
print(json_str)