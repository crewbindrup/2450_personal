1/16/24: **The Youface boilerplate code**
I went and poked around the code we were given, and was horrified.
The implementation of auth and storing passwords in plaintext and in a cookie is evil.
I spent roughly 45 minutes implementing bcrypt and sessions to fix that.
