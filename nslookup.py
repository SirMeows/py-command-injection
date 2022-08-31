import subprocess
import re

domain_name = input("Enter the domain name: ")

# string, from start to finish, must consist ONLY of the allowed characters
# if any other character is found, None is returned

pattern = '/^[a-zA-Z0-9\.]*$/'

result = re.search(pattern, domain_name)

if result == None:

    print('illegal input you ruffian')

else:

    command = "nslookup {}".format(domain_name)

    response = subprocess.check_output(command, shell=True, encoding="UTF-8")

    print(response)

