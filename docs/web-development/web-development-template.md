# Web Development Template

## Scaffold Project with Cloudflare

Create project on Cloudflare workers:

```bash
npm create cloudflare@latest -- my-cloudflare-app --framework=next

# create-next-app questions
# Would you like to use TypeScript? Yes
# Would you like to use ESLint? No
# Would you like to use Tailwind CSS? Yes
# Would you like your code inside a src/ directory? No
# Would you like to use the App Router? Yes
# Would you like to use Turbopack? Yes
# Would you like to customize the import alias? No

# create-cloudflare questions
# Do you want to use git for version control? Yes
# Do you want to deploy your application? Yes
```

Installs:

- react
- react-dom
- next
- @opennextjs/cloudflare

devDependencies:

- typescript
- wrangler
- @types/node
- @types/react
- @types/react-dom
- @tailwindcss/postcss
- tailwindcss

Delete .vscode directory, as it contains settings for VSCode that are not needed in the project.

## GitHub Setup

Using GithubDesktop, select `add` -> `add existing repository`, then select the project directory.

Then, publish the repository to Github, as a private repository.

## Directory Structure

```
[project-name]/
├── app/
├── components/
├── hooks/
├── lib/
├── public/
├── types/
├── next.config.ts
├── postcss.config.mjs
├── tsconfig.json
...
```

App: Contains the main application logic and routing, as well as api routes in /api/route.ts.

Components: Contains reusable UI components.

Hooks: Contains custom React hooks.

Lib: Contains utility functions and libraries.

Public: Contains static assets like images and fonts.

Types: Contains TypeScript type definitions.

next.config.ts: Next.js configuration file.

postcss.config.mjs: PostCSS configuration file for Tailwind CSS.

tsconfig.json: TypeScript configuration file.

## Additional Packages

### Installation

General UI, data, and 3D packages:

```bash
npm i swr motion lodash three @types/three @react-three/fiber @react-three/drei lucide-react
npm i -D daisyui
```

Optional: Blockchain/Web3 packages:

```bash
npm i viem wagmi @rainbow-me/rainbowkit @tanstack/react-query
```

Then, add daisyui to app/globals.css:

```app/globals.css
@import 'daisyui';
```

If using the Web3 stack, wrap your app with Wagmi and RainbowKit providers and set up TanStack Query's QueryClientProvider.

### Explanation

General:

- DaisyUI: A Tailwind CSS component library that provides pre-built UI components.
- SWR: A React Hooks library for data fetching.
- Motion: A library for animations in React.
- Lodash: A utility library for JavaScript that provides helpful functions for working with arrays, objects, and more.
- Three.js: A JavaScript library for creating 3D graphics in the browser.
- Lucide: A collection of open-source icons for React.

Blockchain/Web3 (optional):

- Viem: A library for interacting with Ethereum and other EVM-compatible blockchains.
- Wagmi: A React Hooks library for Ethereum that provides a set of hooks for interacting with Ethereum and other EVM-compatible blockchains.
- RainbowKit: A React component library for building Ethereum wallets and dapps.
- TanStack Query: A powerful data-fetching library for React that provides hooks for fetching, caching, and synchronizing data in your application.

## Appendix

- [shadcn ui](https://ui.shadcn.com/): A collection of free and open-source UI components built with Tailwind CSS and React.
- [Shadcn Blocks](https://www.shadcnblocks.com/): A collection of pre-built UI components for Shadcn. Site templates, and component libraries.
- [DaisyUI Store](https://daisyui.com/store/): A collection of professional pre-built UI components for DaisyUI. Site templates, and component libraries.
- [Tailwind Plus](https://tailwindcss.com/plus): A collection of professional pre-built UI components for Tailwind CSS. Site templates, and component libraries. Personal: $299 one-time
- [Tailwind Toolbox](https://www.tailwindtoolbox.com/): A collection of free and open-source UI components for Tailwind CSS. Site templates, and component libraries.
