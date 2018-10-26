    I thought my experience deploying a Django app on Heroku went pretty well. I followed instructions and things worked. The first place I really stumbled was when I over thought the dj_database_url setup:
    
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)
        I was reading through the docs but I was thinking I still needed to change the Engine or put the dj_database line inside of Database but it was the exact syntax they showed on the docs.

    Once I got over that hurdle it seemed to be smooth sailing again until I ran into trouble with my Procfile being named procfile.
    Guys, this matters for Heroku! Don't create lowercase procfiles. That's my lesson for today as I spent a good chunk debugging since I didn't notice Github didn't notice case changes as changes on github.

    TLDR: Overall Django is cool. Didn't seem any more difficult than deploying for Javascript & the magic makes it a breeze if you know what you are doing.
