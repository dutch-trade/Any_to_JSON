from bs4 import BeautifulSoup
import json
import os

def parse_xml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    return parse_xml_content(content)

def parse_xml_content(content):
    soup = BeautifulSoup(content, 'html.parser')

    # Extract information from the first table
    first_table = soup.find('table')
    first_table_data = {}
    if first_table:
        for row in first_table.find_all('tr'):
            columns = row.find_all(['th', 'td'])
            if columns:
                key = columns[0].text.strip()
                value = columns[1].text.strip()
                first_table_data[key] = value

    # Extract information from the second table
    second_table_data = {"Quantities": [], "Units": [], "Products": [], "Specification": [], "Value Dutch guilders": [], "Value Indian guilders": []}
    second_table = soup.find_all('table')
    if second_table:
        second_table = second_table[1]
        for row in second_table.find_all('tr', class_='odd'):
            columns = row.find_all('td')
            quantities_colspan = int(columns[0].get('colspan', 1))
        
            # Handle colspan for 'Quantities'
            if quantities_colspan == 2:
                second_table_data["Quantities"].append(columns[0].text.strip())
                second_table_data["Units"].append(columns[1].text.strip())
            else:
                second_table_data["Quantities"].append(columns[0].text.strip())
                second_table_data["Units"].append("")  # Add an empty string for 'Units'

            # Continue parsing other columns
            second_table_data["Products"].append(columns[quantities_colspan + 1].text.strip())
            second_table_data["Specification"].append(columns[quantities_colspan + 2].text.strip())
            second_table_data["Value Dutch guilders"].append(columns[quantities_colspan + 3].text.strip())
            second_table_data["Value Indian guilders"].append(columns[quantities_colspan + 4].text.strip())
    # Create the final dictionary entry
    entry = {
        'Number': first_table_data.get('Number', ''),
        'Book year': first_table_data.get('Book year', ''),
        'Source': first_table_data.get('Source', ''),
        'Folio number': first_table_data.get('Folio number', ''),
        'Ship name': first_table_data.get('Ship name', ''),
        'Departure date': first_table_data.get('Departure date', ''),
        'Departure place and region': first_table_data.get('Departure place and region', ''),
        'Arrival date': first_table_data.get('Arrival date', ''),
        'Arrival place and region': first_table_data.get('Arrival place and region', ''),
        'Total value Dutch guilders': first_table_data.get('Total value Dutch guilders', ''),
        'Total value Indian guilders': first_table_data.get('Total value Indian guilders', ''),
        'Remarks Voyage': first_table_data.get('Remarks Voyage', ''),
        'Voyage in DAS': first_table_data.get('Voyage in DAS', ''),
        'Quantities': second_table_data["Quantities"],
        'Units': second_table_data["Units"],
        'Products': second_table_data["Products"],
        'Specification': second_table_data["Specification"],
        'Value Dutch guilders': second_table_data["Value Dutch guilders"],
        'Value Indian guilders': second_table_data["Value Indian guilders"]
    }

    return entry

def process_all_xml_files(directory_path):
    bgb_voyages = []  # List to store results for each voyage

    # Get a list of all XML files in the directory
    xml_files = [f for f in os.listdir(directory_path) if f.endswith('.xml')]

    # Process each XML file
    for xml_file in xml_files:
        file_path = os.path.join(directory_path, xml_file)
        parsed_data = parse_xml_file(file_path)
        bgb_voyages.append(parsed_data)

    # Write the results to a file named "bgb_json.json"
    with open('bgb_json5.json', 'w', encoding='utf-8') as output_file:
        json.dump({"bgb_voyages": bgb_voyages}, output_file, indent=2)

# Example usage with a directory path
directory_path = '/Users/axel22/Dropbox/trade_data/bgb'
process_all_xml_files(directory_path)
