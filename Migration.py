import argparse
import os
from datetime import datetime
from colorama import Back, Style

"""
@Author: Nawras Bukhari
@Description: This script is used to get the environment variables
@Github: https://github.com/NawrasBukhari
@Date: 22/Oct/2022
@LastEditors: Nawras Bukhari
@LastEditTime: 22/Oct/2022
"""

"""
    @usage: python3 Migration.py -n create_test_table
"""
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", action="store", help="Desired name for migration file in this form create_test_table", required=True)
args = parser.parse_args()

# get the current date
date = datetime.now().strftime("%Y%m%d%H%M%S")
# get the migration script name
name = args.name.replace(" ", "_")
# get the migration script path
path = "Migrations\\"
# get the migration script file name
file_name = f"{date}_{name}.py"
# get the migration script file path
file_path = os.path.join(path, file_name)
# create the migration script file
stub = open(file_path, "w+")
stub.write('from Database import Query\n\n\nQuery("")\n\nif __name__ == "__main__":\n\tpass')
stub.close()
# print the migration script file path
print(Back.GREEN + f"Migration script created at {file_path}", Style.RESET_ALL)
