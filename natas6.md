# natas6

Well, this one feels a bit too easy. There's literally a link that shows you the source code, in which there's a file location which you can access.

```php
include "includes/secret.inc";
```

Using the code from this file, you can submit into the query box,

```php
if(array_key_exists("submit", $_POST)) {
```

which passes this test easily, and gives you the flag.

> 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9