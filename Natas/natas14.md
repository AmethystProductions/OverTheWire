# natas 14

```sql
$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\""; 
```

Realising that this was a SQL injection exploit, I of course went to the `OR 1=1 -- `  idea *{a very well known SQL injection, most it exploits the fact the some strings are not well protected and using some knowledge of SQL you can essentially make bypass checking and just evaluate true.}*, but that kind of just hang the webpage.

I honestly don't quite understand why it hangs the webpage (probably because it never finish executing since you're doing comments), but I started to look for other solutions. The important one being the "debug" mode that seems to have been included *(this really isn't necessary, it just allows me to see what I'm doing better)*.

```php
if(array_key_exists("debug", $_GET)) {
    echo "Executing query: $query<br>";
} 
```

Since the debug mode requires `$_GET`, it's really just a matter of POSTing it to `?debug=true` instead.

After fiddling with it a while, and noticing that it's not really sanitising its inputs, I came up with this that got me the code. *(A little more research shows me that this is the second most common injection method https://www.w3schools.com/sql/sql_injection.asp)*

```php
username=natas15&password=" OR ""="
```

Since that would evaluate to the query as:

```sql
SELECT * from users where username="natas15" and password="" OR ""=""
```

*Technically the `username` doesn't really matter here, considering that `AND` executes before `OR`, meaning that it would be `false OR true` (evaluates to `true`) regardless of what I put into `username` or `password`.*


> AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J