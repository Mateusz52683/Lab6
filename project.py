# project.py
import sys
import json
import yaml
import xmltodict

def parse_arguments():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    return input_file, output_file

def read_file(input_file):
    with open(input_file, 'r') as file:
        if input_file.endswith('.json'):
            data = json.load(file)
        elif input_file.endswith('.xml'):
            data = xmltodict.parse(file.read())
        elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
            data = yaml.safe_load(file)
        else:
            print("Unsupported file format")
            sys.exit(1)
    return data

def write_file(output_file, data):
    with open(output_file, 'w') as file:
        if output_file.endswith('.json'):
            json.dump(data, file, indent=4)
        elif output_file.endswith('.xml'):
            xml_string = xmltodict.unparse(data, pretty=True)
            file.write(xml_string)
        elif output_file.endswith('.yml') or output_file.endswith('.yaml'):
            yaml.dump(data, file, default_flow_style=False)
        else:
            print("Unsupported file format")
            sys.exit(1)

def main():
    input_file, output_file = parse_arguments()
    data = read_file(input_file)
    write_file(output_file, data)

if __name__ == "__main__":
    main()
