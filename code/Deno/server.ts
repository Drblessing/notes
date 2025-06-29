// @deno-types="deno.ns"
Deno.serve((_req: Request) => {
  return new Response('Hello, world!');
});
