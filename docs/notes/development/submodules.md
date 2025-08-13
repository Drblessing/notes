# Submodules

**Adding submodules (subrepositories) to a Git repository**

```zsh
mkdir subrepos

git submodule add https://github.com/expo/expo.git subrepos/expo
git submodule add https://github.com/vercel/next.js.git subrepos/next.js
git submodule add https://github.com/cloudflare/cloudflare-docs.git subrepos/cloudflare-docs
git submodule add https://github.com/reactjs/react.dev.git subrepos/react.dev
```

```zsh
git commit -m "Add reference submodules for offline documentation"
```

**Cloning Your Repository with Submodules**

```zsh
git clone --recurse-submodules https://github.com/your-username/notes.git
```

Or:

```zsh
git clone https://github.com/your-username/notes.git
cd notes
git submodule init
git submodule update
```

**Updating Submodules**

```zsh
git submodule update --remote
git commit -m "Update submodules"
```

**Check the status of submodules**

```zsh
git submodule status
```

**Remove a submodule**

```zsh
git submodule deinit -f subrepos/expo
git rm -f subrepos/expo
rm -rf .git/modules/subrepos/expo
git commit -m "Remove expo submodule"
```
