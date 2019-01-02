## Helpful tips for deploying a Django App to Heroku 

When deploying an app to heroku you might run into a range of issues. Django itself doesn't know about Heroku or any deployment service in fact. Luckily heroku come with great tools and guides to get started.

Here are some things that I ran into while deploying a Django into Heroku.

### ENV variables Missing
If your deploying to heroku via git, your env file will most likely be added to your gitignore as it might contain sensitive information. If this is the case, we have a few options. Hard code these into the django app(safety issue) or add them as enviromental variables to heroku. We can do the latter via heroku's command line tools or 

### settings.py
Its important that everything here is setup as there is where Django takes your configuration and turns into an app. Some things you might need to check are the Database url, allowed hosts and secret keys.