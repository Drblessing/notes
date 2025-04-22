# Submodules

Git submodules allow you to include one Git repository inside another subdirectory, while keeping their histories completely separate.

## Adding a Submodule

```zsh
git submodule add --depth 1 <repository-url> <path>
```

Depth 1 is used to limit the history to the latest commit, which can speed up the cloning process.

Use the .git url for added clarity.

Example:

```zsh
git submodule add --depth 1 https://github.com/reactjs/react.dev.git subrepos/react.dev
```

## Ignore changes to a submodule

```zsh
git config -f .gitmodules submodule.<path-to-submodule>ignore all
```

Example:

```zsh
git config -f .gitmodules submodule.subrepos/react.dev.ignore all
```

## Updating Submodules

I do not care about local changes to submodules, so I will always update them to the latest commit. Also, I use the force option to ensure that the submodule is updated even if there are local changes.

```zsh
git submodule update --remote --force
```

## Cloning a Repository with Submodules

```zsh
git clone --recurse-submodules <repository-url>
```

## Submodules

**My submodules**

| url                                               | Description              |
| ------------------------------------------------- | ------------------------ |
| https://github.com/reactjs/react.dev.git          | React documentation      |
| https://github.com/cloudflare/cloudflare-docs.git | Cloudflare documentation |
| https://github.com/vercel/next.js.git             | Next.js framework        |
| https://github.com/expo/expo.git                  | Expo framework           |
| https://github.com/openai/openai-cookbook.git     | OpenAI Cookbook          |
| https://github.com/mrdoob/three.js.git            | Three.js library         |

**Comprehensive List of Submodules**

| url                                                           | Description                     |
| ------------------------------------------------------------- | ------------------------------- |
| https://github.com/python/cpython.git                         | Python programming language     |
| https://github.com/golang/go.git                              | Go programming language         |
| https://github.com/rust-lang/rust.git                         | Rust programming language       |
| https://github.com/vercel/next.js.git                         | Next.js framework               |
| https://github.com/expo/expo.git                              | Expo framework                  |
| https://github.com/reactjs/react.dev.git                      | React documentation             |
| https://github.com/cloudflare/cloudflare-docs.git             | Cloudflare documentation        |
| https://github.com/openjdk/jdk.git                            | OpenJDK                         |
| https://github.com/tailwindlabs/tailwindcss.git               | Tailwind CSS framework          |
| https://github.com/nodejs/node.git                            | Node.js runtime                 |
| https://github.com/pytorch/pytorch.git                        | PyTorch machine learning        |
| https://github.com/pandas-dev/pandas.git                      | Pandas data analysis library    |
| https://github.com/microsoft/vscode.git                       | Visual Studio Code editor       |
| https://github.com/codecrafters-io/build-your-own-x.git       | Build your own X projects       |
| https://github.com/EbookFoundation/free-programming-books.git | Free programming books          |
| https://github.com/sindresorhus/awesome.git                   | Awesome lists                   |
| https://github.com/ethereum/solidity.git                      | Solidity programming language   |
| https://github.com/ethereum/go-ethereum.git                   | Go Ethereum client              |
| https://github.com/bitcoin/bitcoin.git                        | Bitcoin client                  |
| https://github.com/TheAlgorithms/Python.git                   | Algorithms in Python            |
| https://github.com/Significant-Gravitas/AutoGPT.git           | AutoGPT project                 |
| https://github.com/ollama/ollama.git                          | Ollama project                  |
| https://github.com/meta-llama/llama-models.git                | Llama models                    |
| https://github.com/meta-llama/llama-stack.git                 | Llama stack                     |
| https://github.com/meta-llama/llama-stack-apps.git            | Llama stack apps                |
| https://github.com/meta-llama/llama-cookbook.git              | Llama cookbook                  |
| https://github.com/huggingface/transformers.git               | Hugging Face Transformers       |
| https://github.com/lm-sys/FastChat.git                        | FastChat                        |
| https://github.com/infiniflow/ragflow.git                     | RAGFlow                         |
| https://github.com/modelcontextprotocol/servers.git           | Model Context Protocol Servers  |
| https://github.com/karpathy/nanoGPT.git                       | nanoGPT                         |
| https://github.com/microsoft/TypeScript.git                   | TypeScript programming language |
| https://github.com/shadcn-ui/ui.git                           | shadcn UI                       |
