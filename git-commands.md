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

## Deleting Branches

- **Delete Local Branch**:

  ```bash
  git branch -d <branch-name>
  ```

- **Delete Remote Branch**:

  ```bash
  git push origin --delete <branch-name>
  ```

## Reverting

- **Revert Last Commit**:

  ```bash
  git revert HEAD
  ```

- **Revert Specific Commit**:

  ```bash
  git revert <commit-hash>
  ```

- **Revert Merge Commit**:

  ```bash
  git revert -m 1 <merge-commit-hash>
  ```

## Resetting

- **Reset Last Commit**:

  ```bash
  git reset HEAD~1
  ```

- **Reset Specific Commit**:

  ```bash
  git reset <commit-hash>
  ```

- **Reset to Specific Commit**:

  ```bash
  git reset --hard <commit-hash>
  ```

## Rebase

- **Rebase Branch**:

  ```bash
  git rebase <branch-name>
  ```

## Handling conflicts

- **Visual tols**:

  You can use VSCode, Github Desktop, or Github Web to resolve conflicts.

## Summary

With git we create new branches to work on new features, and we merge them back to the main branch when we are done. We can also revert commits, reset to a previous commit, and rebase branches. We can also stash changes to work on them later. We can also use git to handle conflicts. Good luck!
