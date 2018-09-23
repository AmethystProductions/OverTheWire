# Natas 11

Was pretty stump on this one. The encryption wasn't exactly hard once you figure it out, but definitely took me a long time. 

The idea behind the XOR encryption was bascially out of two values, return true only when one of the values is true. Since we have the source code, we could get the input an output values, it was only the key that was a secret. I originally was planning to brute force reverse engineer it, which is pretty barbaric way of dealing with it. But my friend who was working alongside me realised that you could just substitute the other half of the XOR (being the json object) and get the key that way. 

Once you have the key, just sent it through a get request.

> EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3