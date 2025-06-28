#!/bin/bash
# Install my favorite personal repos into ~/github

# Function to clone a repository if it doesn't already exist
clone_if_not_exists() {
    local repo=$1
    local dir=$2
    
    if [ ! -d "$dir" ]; then
        echo "Cloning $repo to $dir..."
        gh repo clone $repo $dir
    else
        echo "$dir already exists, skipping clone."
    fi
}

# Clone the repositories
clone_if_not_exists Drblessing/blockchain-development ~/github/blockchain-development
clone_if_not_exists Drblessing/react-learn ~/github/react-learn
clone_if_not_exists Drblessing/learn-expo ~/github/learn-expo
clone_if_not_exists Drblessing/private-workbench ~/github/private-workbench
clone_if_not_exists Drblessing/my-monorepo ~/github/my-monorepo