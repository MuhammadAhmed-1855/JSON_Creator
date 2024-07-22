import csv
from collections import defaultdict

def read_csv(file_path):
    bank_names = []
    encoding = detect_encoding(file_path)  # Make sure detect_encoding is defined
    with open(file_path, mode='r', encoding=encoding) as file:
        reader = csv.reader(file)
        for row in reader:
            # Assuming the bank name is in the first column
            if row:  # Check if the row is not empty
                bank_names.append(row[0])
    return bank_names

def detect_encoding(file_path):
    import chardet
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

def group_by_initial(bank_names):
    grouped_data = defaultdict(list)
    for name in bank_names:
        initial = name[0].upper()
        grouped_data[initial].append(name)
    return grouped_data

def create_text_file(grouped_data, output_file):
    with open(output_file, mode='w', encoding='utf-8') as file:
        file.write("export const BanksData = [\n")
        for initial in sorted(grouped_data.keys()):
            file.write(f"  {{\n    title: '{initial}',\n    data: [\n")
            for name in grouped_data[initial]:
                file.write(f"      {{name: '{name}', value: '{name}'}},\n")
            file.write("    ],\n  },\n")
        file.write("];\n")

def main():
    input_file = 'bank.csv'  # Change this to your CSV file path
    output_file = 'BanksData.js'
    
    bank_names = read_csv(input_file)
    grouped_data = group_by_initial(bank_names)
    create_text_file(grouped_data, output_file)

if __name__ == "__main__":
    main()
