# natas9

The source code reveals that it's running a shell script, which means that I can use UNIX commands. Using 
```sh
| ls -a . #
```

revealed that there's a filed called `.htpasswd`, which I then modified it to `cat` out the content of the file, which had this.

> $1$p1kwO0uc$UgW30vjmwt4x31BP1pWsV

... but it is not the password.

So after struggling for way too long, someone gave me a hint. "Look at the front page of Natas." Which tells me that the password is stored in a specific location, which then makes this incredibly easy.

```sh
| cat ../../../../etc/natas_webpass/natas9 #
```

> W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl