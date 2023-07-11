# Bin

I keep my user bin in `~/Github/notes/bin`.
This is where I put all my scripts and binaries that I want to be able to run from anywhere.
This directory is added to my `$PATH` in my `.zshrc` file, which is symlinked to my `~/Github/notes` repo.
Whenever I update my bin here, it gets updated on all my machines. The programs are mostly written in Bash or Python, and are mostly for personal use. The ones that use bash/zsh are configured for bash to ensure they work on all machines.

## Contents

### Self-made scripts

| File           | Description                                                                      |
| -------------- | -------------------------------------------------------------------------------- |
| speedtest      | Opens speed.cloudflare.com in a browser.                                         |
| dirp           | Prints and copies the current directory contents and one sub-level deep.         |
| hack           | Opens ~/Github/workbench in VSCode.                                              |
| notes          | Opens ~/Github/notes in VSCode.                                                  |
| lazygit        | Runs lazy git.                                                                   |
| daily-brief    | Opens daily websites in browser: news, blogs, research or daily info.            |
| update-notes   | Updates notes repo to keep machines in sync. A script updating itself, how cool. |
| compare-hashes | Compares the hash of two files.                                                  |
| st             | Super Tar, adds renaming functionality to tar.                                   |
| pomodoro       | A pomodoro timer.                                                                |

### Other software

| File             | Description                                |
| ---------------- | ------------------------------------------ |
| reth             | Ethereum execution client written in Rust. |
| Google cloud sdk | GCloud                                     |

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
