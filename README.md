## How To Use

Place your translation JSON files inside any `locales` directory, anywhere within your project or working folder.

Each JSON file ***should*** be named after the language code, for example:  
`en.json`, `es.json`, `fr.json`.
<br>
(even calling it terrorism.json works, as long as it's a valid file!)

Ensure you have a `.env` file with a `locale` variable that sets your default language code, like so:  
```env
locale=en
```
If you don't want to manually add keys to each file you can use [ctih's translator compiler!](https://github.com/ctih1/kaannos)
