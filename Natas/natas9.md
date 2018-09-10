# natas9

The source code reveals that it's running a shell script, which means that I can use UNIX commands. Using 
```sh
| ls -a . #
```

revealed that there's a filed called `.htpasswd`, which I then modified it to `cat` out the content of the file, which had this.

> $1$p1kwO0uc$UgW30vjmwt4x31BP1pWsV

... but it is not the password.