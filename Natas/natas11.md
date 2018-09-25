# Natas 11

Was pretty stumped on this one. The encryption wasn't exactly hard once you figure it out, but definitely took me a long time. 

```php
function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
```

The idea behind the XOR encryption was bascially out of two values, return true only when one of the values is true. Since we have the source code, we could get the input an output values, it was only the key that was a secret. 

I originally was planning to brute force reverse engineer it, which is pretty barbaric way of dealing with it. But my friend who was working alongside me realised that you could just substitute the other half of the XOR (being the json object) and get the key that way. 

```php
key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));
```

Once you have the key, you can construct your own encrypted cookie, using this idea:

```php
setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
```

You can noew post your encrypted cookie and voila! There's your key.

> EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3