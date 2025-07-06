## How To Use

Place your translation JSON files inside any `locales` directory, anywhere within your project or working folder.

Each JSON file ***should*** be named after the language code, for example:  
`en.json`, `es.json`, `fr.json`.
(even calling it terrorism.json works)\

Ensure you have a `.env` file with a `locale` variable that sets your default language code, like so:  
```env
locale=en
