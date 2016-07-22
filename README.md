#notifyMe

This is a quick little module to allow you to send yourself emails simply by writing: 
```
from notifyMe import notifyMe

<some code, presumably>

notifyMe("Your message goes here")
```

You'll be prompted for your email and password upon import, so I recommend importing in the first few lines of your program. This'll allow you to start your program, enter your email and password, and then wander off to lunch, all the while receiving emails about how your code is doing.

**However**, the module will store your email password in plaintext via the getpass module, so for the *love of god* don't ever actually use this for anything actually serious.
