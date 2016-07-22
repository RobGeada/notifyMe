#notifyMe

This is a quick little module to allow you to send yourself emails simply by writing: 
```
import notifyMe as nm

<some code, presumably>

notifyMe.notifyMe("Your message goes here")
```

You'll be prompted for your email and password upon import. Take a look at the code, I'm not doing anything malicious with that data in any way, but the module will store your email password in plaintext on your machine via the getpass module, so for the *love of god* don't ever actually use this for anything actually serious.
