# Cloudflare

## Cloudflare Pages

Static hosting, moving towards dynamic hosting with serverless apis and frameworks. Unfortuantely, you can't run python fastapi on pages yet. You can run serverless api routes with frameworks like NextJS. However, it only supports the edge runtime, so not all packages are supported. Use cloudflare workers for more flexibility.

https://developers.cloudflare.com/pages/platform/language-support-and-tools/

## Cloudflare Workers

Only supports Javascript and WebAssembly.

From their documentation:

"Workers does not allow our customers to upload native-code binaries to run on the Cloudflare network — only JavaScript and WebAssembly. Many other languages, like Python, Rust, or even Cobol, can be compiled or transpiled to one of these two formats. Both are passed through V8 to convert these formats into true native code."

## NextJS on Cloudflare

https://developers.cloudflare.com/pages/framework-guides/deploy-a-nextjs-site/
