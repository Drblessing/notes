# Cloudflare

## Cloudflare Pages

The v2 beta comes with Node.js 18.16.0, and Python3.10.5. However, it says it can support any version, so we'll have to test Python 3.11 at some point. Maybe we could run AI models on it?

## Cloudflare Workers

Only supports Javascript and WebAssembly.

From their documentation:

"Workers does not allow our customers to upload native-code binaries to run on the Cloudflare network — only JavaScript and WebAssembly. Many other languages, like Python, Rust, or even Cobol, can be compiled or transpiled to one of these two formats. Both are passed through V8 to convert these formats into true native code."
