##  
##  
##  This scrip reads the post-fit (background only for example) rate parameters for DY estimate 
##  and update the initial values of these rate parameters in a datacard of our choice
##  it can be run like follows:
##  python update_rateParam_inizialization.py table.html datacard.txt
##  
##  
from __future__ import print_function
from bs4 import BeautifulSoup
import re
import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 3:
    print("Please provide the HTML file name and the datacard file name as command line arguments.")
    exit(1)

html_file_name = sys.argv[1]
datacard_file_name = sys.argv[2]

# Read the HTML file
with open(html_file_name, 'r') as file:
    html_content = file.read()

data_dict_res_btag = {}
data_dict_boost_bTag = {}
data_dict_res_bVeto = {}
data_dict_boost_bVeto = {}


# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table in the HTML
table = soup.find('table')

# Find the header row
header_row = table.find('tr')
header_cells = header_row.find_all('th')

# Find the column index of "background fit"
background_fit_index = None

for i, cell in enumerate(header_cells):
    if cell.text.strip().lower() == 'background fit':
        background_fit_index = i
        break

if background_fit_index is None:
    print("Failed to find 'background fit' column in the table.")
    exit(1)

# Find the rows with the desired label pattern and extract "background fit" values
rows = table.find_all('tr')

for row in rows:
    cells = row.find_all('td')

    # Skip rows that do not have enough cells
    if len(cells) < background_fit_index + 1:
        continue

    # Match the rows with the desired label pattern
    label_cell = cells[0]
    label_text = label_cell.text.strip()

    # Resolved b-tag category
    if 'CMS_DY_Resolved_2d' in label_text and 'norm_res_Z_btag' in label_text:
        match = re.match(r'CMS_DY_Resolved_2d_(\d+)_norm_res_Z_btag', label_text)

        if match:
            row_number = int(match.group(1))
            background_fit_cell = cells[background_fit_index]
            background_fit_text = background_fit_cell.text.strip()

            match_fit = re.match(r'^([\+\-\.\d]+)', background_fit_text)

            if match_fit:
                background_fit = float(match_fit.group(1))
                data_dict_res_btag[row_number] = background_fit

    # Resolved b-Veto category
    if 'CMS_DY_Resolved_2d' in label_text and 'norm_res_Z_bVeto' in label_text:
        match = re.match(r'CMS_DY_Resolved_2d_(\d+)_norm_res_Z_bVeto', label_text)

        if match:
            row_number = int(match.group(1))
            background_fit_cell = cells[background_fit_index]
            background_fit_text = background_fit_cell.text.strip()

            match_fit = re.match(r'^([\+\-\.\d]+)', background_fit_text)

            if match_fit:
                background_fit = float(match_fit.group(1))
                data_dict_res_bVeto[row_number] = background_fit

    # Boosted b-tag category
    if 'CMS_DY_Boosted_Z' in label_text and 'norm_boost_bTag' in label_text:
        match = re.match(r'CMS_DY_Boosted_Z_(\d+)_norm_boost_bTag', label_text)

        if match:
            row_number = int(match.group(1))
            background_fit_cell = cells[background_fit_index]
            background_fit_text = background_fit_cell.text.strip()

            match_fit = re.match(r'^([\+\-\.\d]+)', background_fit_text)

            if match_fit:
                background_fit = float(match_fit.group(1))
                data_dict_boost_bTag[row_number] = background_fit

    # Boosted b-Veto category
    if 'CMS_DY_Boosted_Z' in label_text and 'norm_boost_bVeto' in label_text:
        match = re.match(r'CMS_DY_Boosted_Z_(\d+)_norm_boost_bVeto', label_text)

        if match:
            row_number = int(match.group(1))
            background_fit_cell = cells[background_fit_index]
            background_fit_text = background_fit_cell.text.strip()

            match_fit = re.match(r'^([\+\-\.\d]+)', background_fit_text)

            if match_fit:
                background_fit = float(match_fit.group(1))
                data_dict_boost_bVeto[row_number] = background_fit


# Read the datacard file
with open(datacard_file_name, 'r') as file:
    datacard_content = file.read()

# Update the values in the datacard file
for key, value in data_dict_res_btag.items():
    pattern = r'(CMS_DY_Resolved_2d_{}_norm_res_Z_btag\w+\s+rateParam\s+\w+\s+DY_Resolved_2d_\d+\s+)([\d\.]+)'.format(key)
    replacement = r'\g<1>{:.4f}'.format(value)
    datacard_content = re.sub(pattern, replacement, datacard_content)

for key, value in data_dict_res_bVeto.items():
    pattern = r'(CMS_DY_Resolved_2d_{}_norm_res_Z_bVeto\w+\s+rateParam\s+\w+\s+DY_Resolved_2d_\d+\s+)([\d\.]+)'.format(key)
    replacement = r'\g<1>{:.4f}'.format(value)
    datacard_content = re.sub(pattern, replacement, datacard_content)

for key, value in data_dict_boost_bTag.items():
    pattern = r'(CMS_DY_Boosted_Z_{}_norm_boost_bTag\w+\s+rateParam\s+\w+\s+DY_Boosted_Z_\d+\s+)([\d\.]+)'.format(key)
    replacement = r'\g<1>{:.4f}'.format(value)
    datacard_content = re.sub(pattern, replacement, datacard_content)

for key, value in data_dict_boost_bVeto.items():
    pattern = r'(CMS_DY_Boosted_Z_{}_norm_boost_bVeto\w+\s+rateParam\s+\w+\s+DY_Boosted_Z_\d+\s+)([\d\.]+)'.format(key)
    replacement = r'\g<1>{:.4f}'.format(value)
    datacard_content = re.sub(pattern, replacement, datacard_content)


# Write the updated datacard back to the file
with open(datacard_file_name, 'w') as file:
    file.write(datacard_content)

print("Datacard updated successfully.")
