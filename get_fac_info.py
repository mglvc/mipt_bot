import csv
import re

def get_info(fac, csv_path='data/fac_info.csv'):
    response = {
            "name": [],
            "description": [],
            "address": [],
            "phones": [],
            "email": [],
            "site": []
        }

    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        for row in reader:
            if not fac in row[0]:
                continue
            response = {
                    "name": re.sub(r'\s+', ' ', row[0]),
                    "description": re.sub(r'\s+', ' ', row[1]),
                    "address": row[2].split('\n'),
                    "phones": [row[3], row[4]],
                    "email": row[5],
                    "site": row[6]
                }
            break

    return response

#
#  def main():
#      res = get_info('ФЭФМ', 'data/fac_info.csv')
#      print(res)
#
#
#  if __name__ == '__main__':
    #  main()
