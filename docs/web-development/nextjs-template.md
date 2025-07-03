# NextJS Template

Install:

npx create-next-app@latest [project-name]

Options:

- Typescript
- No ESLint
- Tailwind CSS
- No code inside src/ directory
- App Router
- Turbopack
- No customize the import alias

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

## Packages

### Shadcn

A UI component library for Next.js and Tailwind CSS.

```
npx shadcn@latest init
```

Installs class-variance-authority, clsx, lucide-react, tw-animate-css, and other dependencies.

### Tailwind CSS
