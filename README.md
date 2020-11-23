This is an example app based on: https://github.com/fangli/django-saml2-auth

Using an ADFS server.   I've supplied claims.png to show how the ADFS server should be setup.

As django-saml2-auth has not accepted this pull request: https://github.com/fangli/django-saml2-auth/pull/118/commits
I had to result to some hackery on the project so that I get good URL redirection after auth.  That is why there is libs folder with the libary in it.

The "/" of this django app will just display your username and the query string.  Then you get logged out.   If you where to use the default libary you would get redirected to the root and would loose the query string.

You probably want to change the remote_metadata.xml to your own file so it does not try to auth against my SAML server.

