# Common Errors, Gotchas, and Troubleshooting

Django is a powerful tool, but it can be a bit finicky.  This doubles when trying to deploy to Heroku.  Below are some common mistakes, errors, and resolutions.

## Common Mistakes
* Don't forget to include the `.` when creating your project!  If you miss this, everything will work until you try to deploy, then you will have a large number of problems with commands not working as documented.
* The deployment instructions require you to consult outside documentation is several spots to properly configure some of the third party packages we will be using.
* You will be using Sqlite3 locally and Postgres when deployed to Heroku.  This very rarely causes minor issues, such as Postgres having a smaller max INT than Sqlite3.  However, it is much easier than trying to get Postgres working locally.

## `pipenv` error `'module' object is not callable`

If you're running `pipenv` and you get an error that ends like this:

```
"/usr/local/Cellar/pipenv/2018.7.1/libexec/lib/python3.7/site-packages/pipenv/vendor/requirementslib/models/requirements.py", line 704, in from_line
line, extras = _strip_extras(line)
TypeError: 'module' object is not callable
```

it might be time to upgrade `pipenv`. Make sure that `pipenv --version` is
outputting at least `2018.10.13`.

## `pipenv` error `Found existing installation: [package name]`

Add the following option to ignore existing installs: `--ignore-installed`

```
pip install pipenv --upgrade --ignore-installed
```

## `./manage.py` error `from exc`

If you get this:

```
    ) from exc
         ^
SyntaxError: invalid syntax
```

it usually means Python 2.x is running instead of Python 3. This, in turn,
usually means you've forgotten to `pipenv shell` into your virtual environment.

Run `python --version` and make sure it says `3.`-something.

## `./manage.py dbshell` not launching

_Chief. Windows_

Make sure you have your SQLite3 package installed and in your path.

A recommended way to install SQLite3 on Windows is [with
chocolatey](https://chocolatey.org/packages?q=sqlite).

## `curl` not working from PowerShell

By default, PowerShell uses `curl` as an alias for its own `Invoke-WebRequest`. If you've installed `curl` and want to use it instead, you have to unalias it with

```powershell
Remove-Item alias:curl
```

[Here are some instructions for removing the alias
permanently](https://superuser.com/questions/883914/how-do-i-permanently-remove-a-default-powershell-alias)

## VS Code not recognizing Django imports properly

Enable Django linting by adding the following to your VS Code workplace
settings:

```
"python.linting.pylingArgs":["--load-plugins","pylint_django"]
```

## Using PowerShell in VS Code terminal

If you prefer it, [here are some instructions on setting it
up](https://code.visualstudio.com/docs/editor/integrated-terminal).
