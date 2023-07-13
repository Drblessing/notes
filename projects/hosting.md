# Hosting

## Python

You can hose Python projects on VPS, AWS Lambda, Google Cloud Functions, and Replit.
Fastapi is a good option for API's, and Flask is a good option for websites.
Docker containers are a good way to package your project, as is AWS Lambda.
You can run the Docker container on a VPS, or deploy it to AWS Lambda.
Very simple code can run on Replit.

## API

Python Fastapi can be hosted serverless on AWS Lambda or Google Cloud functions using the mangum handler.

Simple Tutorial: https://github.com/pixegami/fastapi-tutorial

Bugfixes: Use fastapi 0.99.0, and use a fresh directory.

## Static Content

Cloudflare pages is by far the best place to host static content and sites. Even without a framework, you can just throw your files, whether they be pdf, insanely large jpeg, pdfs, books, binaries, etc. with no limits, and it's free, unlimited, and ultra fast.

For example, I hosted a repo that only had this structure:

```
Images/
    img1.jpg
    4kimg2.png
    ...
```

And they were available at <cloudflare-pages-url>/Images/img1.jpg, etc. So any file you put in the repo is available at the url in the file structure.

I'm not sure using it as a CDN is allowed, but it's a great way to host static content for hobby projects. There are commercial plans for more advanced features.
