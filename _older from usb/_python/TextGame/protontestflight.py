import urllib.request

print('Branch name?')
BranchName = input()
URL = 'https://raw.githubusercontent.com/JMcB17/Zarya/' + BranchName + '/zarya.py'

print('Connecting...')
try:
    with urllib.request.urlopen(URL) as response:
        code = response.read()
        print('Latest version downloaded.')
        print('')
        exec(code)
except urllib.error.URLError as err:
    print('No connection.')
except ValueError as err:
    print('No zarya-edit.')
