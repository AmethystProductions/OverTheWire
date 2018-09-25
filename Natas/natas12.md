# natas 12

So this one is mostly about thinking outside the box.

The key line of code is not the generate random string and all that jazz, they're all red herring. The key problem that's preventing one from executing a script is mainly the fact that it's being sent as a .jpg file to the server. 

```html
<input type="hidden" name="filename" value="<? print genRandomString(); ?>.jpg" />
```
This line generates a random name and attach a jpg extension to it. Which means that it doesn't matter what you named it, it'll always be sent as a JPG. 

... But since it's attaching the extension on your broswer, before being sent to the server instead of generating the file on the server side. It's possible to intercept the POST request, edit it so that it sends a .php file instead with the same content, and now you get yourself a php file you can execute on the other side.

From this point on it's basically a repeat of natas8, trying to figure out the right location and getting the pass using `shell_exec`.

```html
<pre><? print(shell_exec("cat ../../../../../etc/natas_webpass/natas13")) ?><pre>
```

*Using `<pre>` allows us to format the output. Otherwise when you're testing for things it's a mess.*

> jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY