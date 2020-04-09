
from csv import reader
import sys
import datetime as dt

def parse_cmd_args(args):
    country_list = args[1:]
    return country_list

def read_data(filename):
    opened_file = open(filename)
    read_file = reader(opened_file)
    data = list(read_file)
    data_dict = {'header': data[0], 'data': data[1:]}
    return data_dict

def extract_data(country, data_dict):
    country_data = []
    for row in data_dict['data']:
        if row[1] == country:
            country_data.append(row)

    current_date  = dt.datetime.strptime(country_data[-1][0], '%Y-%m-%d')
    final_date = current_date.strftime("%B %d, %Y")

    print("Date: "+final_date)
    print("Total Cases: ",country_data[-1][4])
    print("Total Deaths: ",country_data[-1][5])
    print("Death Rate: ",round((int(country_data[-1][5]) / int(country_data[-1][4])) * 100, 2),"%")
    print("New Cases: ",country_data[-1][2])

if __name__ == '__main__':
    country_list = parse_cmd_args(sys.argv)
    data_dict = read_data('full_data.csv')

    for i in country_list:
        print('Stats for {}:'.format(i))
        extract_data(i, data_dict)
        print('\n')
