git submodule add --depth 1 https://github.com/reactjs/react.dev.git subrepos/react.dev
git submodule add --depth 1 https://github.com/expo/expo.git subrepos/expo
git submodule add --depth 1 https://github.com/vercel/next.js.git subrepos/next.js
git submodule add --depth 1 https://github.com/cloudflare/cloudflare-docs.git subrepos/cloudflare-docs
git submodule add --depth 1 https://github.com/mrdoob/three.js.git subrepos/three.js # Cool 3D library
git submodule add --depth 1 https://github.com/openai/openai-cookbook.git subrepos/openai-cookbook # OpenAI Cookbook

# Ignore submodules
git config -f .gitmodules submodule.subrepos/react.dev.ignore all
git config -f .gitmodules submodule.subrepos/expo.ignore all
git config -f .gitmodules submodule.subrepos/next.js.ignore all
git config -f .gitmodules submodule.subrepos/cloudflare-docs.ignore all
git config -f .gitmodules submodule.subrepos/three.js.ignore all
git config -f .gitmodules submodule.subrepos/openai-cookbook.ignore all

# For installing submodules on a new clone, run: 
# git submodule update --init --recursive --depth 1