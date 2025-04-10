git submodule add -b main https://github.com/reactjs/react.dev submodules/react.dev

"Add ignore=all to .gitmodules file, then run git submodule sync"

git config submodule.submodules/react.dev.ignore all

# Get the submodule on fresh repo

git submodule update --init --remote submodules/react.dev
