# Deployment Config

https://developers.cloudflare.com/pages/framework-guides/deploy-a-nextjs-site/

1. .nvmrc = 18.16.1

2. export const runtime = 'edge'; at the top of all routes (api routes and pages)

3. npm install --save-dev @cloudflare/next-on-pages

4. Build step

Configuration option Value
Production branch main
Build command npx @cloudflare/next-on-pages@1
Build directory .vercel/output/static

4. Comptability flags

Settings > Functions > Compatibility Flags.
nodejs_compat flag for both production and preview.

Compatibility Date and configure a compatibility date that is at least 2022-11-30 for both production and preview.

5. Smart Placement off

Can turn it on once everything is working smoothly, but best not overload potential errors.

6. Pages v2 beta on

Settings > Pages > Pages v2 beta
