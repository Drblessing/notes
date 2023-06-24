# Scripts

To use these scripts, you have to:

1. Add a shebang line to the top of the script with the path to the program interpreter. For example, `#!/usr/bin/env python3` for Python 3.

2. Make the script executable with `chmod +x <script>`.

3. Add the script to your path. For example, `sudo cp <script> /usr/local/bin`. I have a directory ~/.local/bin in my path, so I put them there.

4. Rename the script to remove the extension. For example, `mv <script>.py <script>`.

5. Run it anywhere with `<script>`.

## Dirp

A Python script to print the contents of a directory and one level down, then copy it to the keyboard. Also prints it to the console. Useful for pasting a directory listing into a text editor or LLM.

Input: A directory path. Can be absolute or relative, i.e. ".". If no path is given, the current directory is used.

Example usage: `$ dirp ~/Documents`

```
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
