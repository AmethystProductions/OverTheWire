# natas8

```php
function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}
```

The functions are right there in the source code. I tried manually reversing it at first. That was not a good idea. Just get a php interpreter and the reverse it.

*`base64_encode()` is a function that encodes a piece of string to base 64, as the name suggests. `strrev()` reverses the string output by the last functions. Then `bin2hex` converts from binary values to hexidecimals.*

```php
print base64_decode(strrev(hex2bin("3d3d516343746d4d6d6c315669563362")));
```

> W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl