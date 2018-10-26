Blockers I ran into:
- For installing dependencies, I tried to install via the virtual environment, and used `pip install` for all of    my commands. I eventually found out that this did not properly install the dependencies, and I had to `pipenv     install` instead.
- Configuring the environment variables in `settings.py` was pretty difficult (specifically `ALLOWED_HOSTS` and     `DATABASES`), as I didn't find a lot of good resources for this online. I don't think I would've been able to     complete this step without help from the PMs.
- By far the biggest pain point for me was configuring whitenoise. One problem is that the documentation is         misleading when it says that after you install, you just need to add Whitenoise to your middleware list - not     true. There are other things you need to add to settings.py, in addition to running the `collectstatic` command.
- Some resources say to add staticfiles to your `.gitignore` but I was unable to run the app correctly until I      committed and pushed staticfiles.

What went well:
- The steps for adding Procfile and requirements.txt were very easy.
- After I found out that I needed to use the `pipenv` command instead of the `pip` command, I didn't have any       trouble installing dependencies.
- I also had an easy time creating the app, and running migrations. I like Heroku's CLI so far.
- The deployment process was overall a little tricky, but definitely a useful experience! 

