git submodule add https://github.com/reactjs/react.dev.git subrepos/react.dev
git submodule add https://github.com/expo/expo.git subrepos/expo
git submodule add https://github.com/vercel/next.js.git subrepos/next.js
git submodule add https://github.com/cloudflare/cloudflare-docs.git subrepos/cloudflare-docs
git config -f .gitmodules submodule.subrepos/react.dev.ignore all
git config -f .gitmodules submodule.subrepos/expo.ignore all
git config -f .gitmodules submodule.subrepos/next.js.ignore all
git config -f .gitmodules submodule.subrepos/cloudflare-docs.ignore all
# gh repo clone notes -- -recurse-submodules    