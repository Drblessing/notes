# Web Development Template

## Scaffold Project with Cloudflare

Create project:

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

### Shadcn

A UI component library for Next.js and Tailwind CSS.

```
npx shadcn@latest init
npx shadcn@latest add --all
```

Installs class-variance-authority, clsx, lucide-react, tw-animate-css, and other dependencies.

### swr

A React Hooks library for data fetching.

```
npm i swr
```

### Motion

For animations and transitions in React applications.

```
npm i motion
```

### Lodash

A utility library for JavaScript that provides functions for common programming tasks.

```
npm i lodash
```
