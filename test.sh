# First remove any traces of the previous submodule config
git config -f .gitmodules --remove-section submodule.submodules/react.dev
git rm --cached submodules/react.dev 2>/dev/null || true
rm -rf .git/modules/submodules/react.dev 2>/dev/null || true
# Make sure directory exists
mkdir -p submodules
# Now add it fresh
git submodule add -b main https://github.com/reactjs/react.dev.git submodules/react.dev