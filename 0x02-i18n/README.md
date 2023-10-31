# alx-backend Project: Internationalization and Localization

## Directory: 0x02-i18n

### Task Descriptions

### Task 0: Basic Flask app
- **File:** [0-app.py](./0-app.py), [templates/0-index.html](./templates/0-index.htm)
- **Description:** Set up a basic Flask app with a single route (`/`) and an `index.html` template displaying "Welcome to Holberton" as the page title (`<title>`) and "Hello world" as the header (`<h1>`).

### Task 1: Basic Babel setup
- **File:** [1-app.py](./1-app.py), [templates/1-index.html](./templates/1-index.htm)
- **Description:** Install the Babel Flask extension and instantiate the Babel object in your app. Create a `Config` class with `LANGUAGES` attribute equal to `["en", "fr"]`. Use `Config` to set Babel’s default locale ("en") and timezone ("UTC").

### Task 2: Get locale from request
- **File:** [2-app.py](./2-app.py), [templates/2-index.html](./templates/2-index.html)
- **Description:** Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with supported languages.

### Task 3: Parametrize templates
- **File:** [3-app.py](./3-app.py), [babel.cfg](./babel.cfg), [templates/3-index.html](./templates/3-index.html), [translations/en/LC_MESSAGES/messages.po](./`translations/en/LC_MESSAGES/messages.po), [translations/fr/LC_MESSAGES/messages.po](./translations/fr/LC_MESSAGES/messages.po), [translations/en/LC_MESSAGES/messages.mo](./translations/en/LC_MESSAGES/messages.mo), [translations/fr/LC_MESSAGES/messages.mo](./`translations/fr/LC_MESSAGES/messages.mo)

- **Description:** Parametrize templates using the `_` or `gettext` function. Create a `babel.cfg` file for configuration. Initialize translations and edit message files for English and French.

### Task 4: Force locale with URL parameter
- **File:** [4-app.py](./4-app.py), [templates/4-index.html](./templates/4-index.html)
- **Description:** Implement a way to force a specific locale by passing the `locale=fr` parameter to the app's URLs. Detect the incoming request for the locale argument.

### Task 5: Mock logging in
- **File:** [5-app.py](./5-app.py), [templates/5-index.html](./templates/5-index.html)
- **Description:** Mock a user login system by creating a user table. Define a `get_user` function and a `before_request` function to set the user as a global on `flask.g.user`.

### Task 6: Use user locale
- **File:** [6-app.py](./6-app.py), [templates/6-index.html](./templates/6-index.html)
- **Description:** Change `get_locale` to use a user’s preferred locale if supported. Priority: URL parameters > user settings > request header > default locale.

### Task 7: Infer appropriate time zone
- **File:** [7-app.py](./7-app.py), [templates/7-index.html](./templates/7-index.html)
- **Description:** Define `get_timezone` and use the `babel.timezoneselector` decorator. Find the time zone from URL parameters, user settings, or default to UTC.

### Task 8: Display the current time
- **File:** [app.py](./app.py), [templates/index.html](./templates/index.html), [translations/en/LC_MESSAGES/messages.po](./translations/en/LC_MESSAGES/messages.po), [translations/fr/LC_MESSAGES/messages.po](./translations/fr/LC_MESSAGES/messages.po)
- **Description:** Display the current time in the inferred time zone using the default format. Use translations for the message.
