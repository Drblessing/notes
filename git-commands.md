# Git Commands Quick Reference

## Branches

- **List All Branches (Local and Remote)**:

  ```bash
  git branch -a
  ```

- **Switch to a branch**:

  - Using `checkout`:

  ```bash
  git checkout <branch-name>
  ```

  - Using `switch` (Git 2.23+):

  ```bash
  git switch <branch-name>
  ```

- **Create and switch to a new branch**:

  - Using `checkout`:

  ```bash
  git checkout -b <branch-name>
  ```

  - Using `switch` (Git 2.23+):

  ```bash
  git switch -c <branch-name>
  ```

## Staging and Committing

- **Stage Changes**:

  ```bash
  git add .
  ```

- **Commit Changes**:

  ```bash
  git commit -m "Commit message"
  ```

## Updating and Publishing

- **Fetch Changes**:

  ```bash
  git fetch
  ```

- **Pull Changes**:

  ```bash
  git pull
  ```

- **Push Changes**:

  ```bash
  git push
  ```

- **Push New Branch to Remote**:

  ```bash
  git push -u origin <branch-name>
  ```

- **Auto push new branches**:

  ```bash
  git config --global push.default current
  ```

## Stashing

- **Stash Changes**:

  ```bash
  git stash push -m "Stash message"
  ```

- **List Stashes**:

  ```bash
  git stash list
  ```

- **View Stash**:

  - Latest stash:

    ```bash
    git stash show
    ```

  - Specific stash:

    ```bash
    git stash show -p stash@{<stash-number>}
    ```

- **Apply Stash**:

  - Latest stash:

    ```bash
    git stash apply
    ```

  - Specific stash:

    ```bash
    git stash apply stash@{<stash-number>}
    ```

- **Pop Stash**:

  - Latest stash:

    ```bash
    git stash pop
    ```

  - Specific stash:

    ```bash
    git stash pop stash@{<stash-number>}
    ```

- **Deleting a Stash**:

  - Latest stash:

    ```bash
    git stash drop
    ```

  - Specific stash:

    ```bash
    git stash drop stash@{<stash-number>}
    ```

- **Clearing All Stashes**:

  ```bash
  git stash clear
  ```

## Repository Status

- **Check Status**:

  ```bash
  git status
  ```

- **View Last Commit**:

  ```bash
  git log -1
  ```

- **Show Configured Remote Repository**:

  - Summary:

    ```bash
    git remote -v
    ```

  - Detailed View:

    ```bash
    git remote show origin
    ```

## Merging

- **Merge Branch into main**:

  ```bash
  git checkout main
  git merge <branch-name>
  ```

- **Merge Branch (Fast-Forward)**:

  ```bash
  git merge --ff-only <branch-name>
  ```

- **Merge Branch (No Fast-Forward)**:

  ```bash
  git merge --no-ff <branch-name>
  ```

- **Merge Branch (Squash)**:

  ```bash
  git merge --squash <branch-name>
  ```
