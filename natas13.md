# natas 13

This is essencially the same question. Except it now checks for EXIF of the file to see if it's an image. 

```php
else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
    echo "File is not an image"; 
```

There probably is a way to edit the EXIF of a file to make it look like an image, but why bother doing that when you can literally just create an iamge and then attach the `php` code at the end of it? 

Which is exactly what I did. I created fa 1x1 jpg file using GIMP, and when I sent it. I intercepted it and added the same code from last problem, merely tweaking the numbers from 13 to 14. *(don't forget to POST the file as php)*


> Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1