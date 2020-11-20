# python-test

## API authentication
1. Go to https://gorest.co.in/
2. Login with Google/Facebook/Github
3. Copy the generated access token
4. Create an 'api_keys.py' file in project root
5. In it: `ACCESS_TOKEN = 'paste_your_access_token_here'`

## Installing the package
1. Run `python3 setup.py develop` for now
2. Run `pipenv install` or `pip install` depending on virtual env used

## Running the tests
After installing the package, run:
- `runtests` for default run
- `runtests -e` for default run with email report. You have to change the email recipient in the settings file in order to receive the email. Otherwise, I will receive it.
