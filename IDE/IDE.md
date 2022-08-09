# IDE

## [Prettier + ESLint](https://www.robinwieruch.de/prettier-eslint/)

Prettier handles form, ESLint handles substance.
<br>In other words, Prettier handles code formatting, ESLint handles code quality

Install Prettier + ESLint in VSCode, then install these packages to make them interoperate

```
$ npm install --save-dev eslint-config-prettier eslint-plugin-prettier
$ npx install-peerdeps --dev eslint-config-airbnb
```

```
# .eslintrc
{
  "extends": ["airbnb", "prettier"],
  "plugins": ["prettier"],
  "rules": {
    "prettier/prettier": ["error"]
  }
}
```
