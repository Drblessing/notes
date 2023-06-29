# Bin

I keep my user bin in `~/Github/notes/bin`.
This is where I put all my scripts and binaries that I want to be able to run from anywhere.
This directory is added to my `$PATH` in my `.zshrc` file.
Whenever I update my bin here, it gets updated on all my machines.

## Contents

| File         | Description                                                                      |
| ------------ | -------------------------------------------------------------------------------- |
| dirp         | Prints and copies the current directory contents and one sub-level deep.         |
| reth         | Ethereum execution client written in Rust.                                       |
| speedtest    | Opens speed.cloudflare.com in a browser                                          |
| hack         | Opens ~/Github/workbench in VSCode                                               |
| notes        | Opens ~/Github/notes in VSCode                                                   |
| lazygit      | Runs lazy git                                                                    |
| daily-brief  | Opens daily websites in browser: news, blogs, research or daily info             |
| update-notes | Updates notes repo to keep machines in sync. A script updating itself, how cool. |
| compare-hash | Compares the hash of two files                                                   |

## Examples

### Dirp

Useful for talkign about a directory structure with someone, including AI models.

A Python script to print the contents of a directory and one level down, then copy it to the keyboard. Also prints it to the console.

Input: A directory path. Can be absolute or relative, i.e. ".". If no path is given, the current directory is used.

Example usage:

```bash
dbless@Daniels-MacBook-Pro Github % dirp
Github/
    notes/
        .gitattributes
        .gitignore
        CONTRIBUTING.md
        LICENSE
        README.md
        .git/
        Blockchain/
        Collaborations/
        Deep Learning/
        Docker/
        Google Analytics/
        Hardware/
        MacOS Setup/
        Next/
        Notes/
        OOP/
        ProjectManagement/
        Prompts/
        Python/
        References/
        Scripts/
        Tech Interviews/
        Templates/
        Tools/
        Tutorials/
        npm/
        sysadmin/
        vscode/
    static/
        README.md
        .git/
        Images/
        References/
    workbench/
        .gitignore
        CONTRIBUTING.md
        LICENSE
        README.md
        .git/
        .venv/
        python/
```

### TODO: Add examples
