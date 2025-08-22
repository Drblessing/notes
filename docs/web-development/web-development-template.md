# Web Development Template

## Scaffold Project with Cloudflare

1. Create project on Cloudflare workers:

```bash
npm create cloudflare@latest -- . --framework=next

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

2. Delete `.vscode/` and `.dev.vars`

They are not needed for the project.

## GitHub Desktop Setup (Optional)

Github Desktop is an easy and handy GUI for managing Git repositories and Github workflows. You can also use the `gh` command line tool. Github Desktop is particularly useful for repositories with multiple branches and merge conflicts.

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

**App**: Contains the main application logic and routing, as well as api routes in /api/route.ts.<br>
**Components**: Contains reusable UI components.<br>
**Hooks**: Contains custom React hooks.<br>
**Lib**: Contains utility functions and libraries.<br>
**Public**: Contains static assets like images and fonts.<br>
**Types**: Contains TypeScript type definitions.<br>
**next.config.ts**: Next.js configuration file. <br>
**postcss.config.mjs**: PostCSS configuration file for Tailwind CSS. <br>
**tsconfig.json**: TypeScript configuration file.

## Additional Packages

### Installation

General UI, data, and 3D packages:

```bash
npm i swr motion lodash three @react-three/fiber @react-three/drei lucide-react @headlessui/react @heroicons/react react-icons use-sound
npm i -d @types/three @tailwindcss/forms @tailwindcss/typography @tailwindcss/aspect-ratio
```

To enable the plugins in tailwind:

```javascript
// tailwind.config.js
module.exports = {
  // ...
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
  ],
};
```

### Optional: Blockchain/Web3 packages:

```bash
npm i viem wagmi @rainbow-me/rainbowkit @tanstack/react-query
```

If using the Web3 stack, wrap your app with Wagmi and RainbowKit providers and set up TanStack Query's QueryClientProvider.

### Explanation

General:

- SWR: A React Hooks library for data fetching.
- Motion: A library for animations in React.
- Lodash: A utility library for JavaScript that provides helpful functions for working with arrays, objects, and more.
- Three.js: A JavaScript library for creating 3D graphics in the browser.
- Lucide: A collection of open-source icons for React.
- React icons: An icon vending machine which bundles popular icon libraries.
- Headless UI: A set of completely unstyled, fully accessible UI components designed to integrate beautifully with Tailwind CSS. Required for Tailwind Plus.
- Heroicons react: Required for Tailwind Plus.
- Use-sound: Fun React hook for playing sounds.
- Tailwind: A utility-first CSS framework for creating custom designs.
- Tailwind/Forms: A plugin for Tailwind CSS that provides form styles.
- Tailwind/Typography: A plugin for Tailwind CSS that provides prose styles.
- Tailwind/Aspect Ratio: A plugin for Tailwind CSS that provides aspect ratio utilities.
- Tailwind Plus: A premium collection of templates and components for Tailwind CSS.

Blockchain/Web3 (optional):

- Viem: A library for interacting with Ethereum and other EVM-compatible blockchains.
- Wagmi: A React Hooks library for Ethereum that provides a set of hooks for interacting with Ethereum and other EVM-compatible blockchains.
- RainbowKit: A React component library for building Ethereum wallets and dapps.

### Appendix

Resources that don't have a place right now, but I want to explore in the future

- Lenis: A smooth scrolling library for React.
- MagicUI: A cutting-edge fun UI library for React.
