#!/bin/bash
# Install my favorite personal repos into ~/Github

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
clone_if_not_exists Drblessing/blockchain-development ~/Github/blockchain-development
clone_if_not_exists Drblessing/react-learn ~/Github/react-learn
clone_if_not_exists Drblessing/learn-expo ~/Github/learn-expo
clone_if_not_exists Drblessing/private-workbench ~/Github/private-workbench
clone_if_not_exists Drblessing/my-monorepo ~/Github/my-monorepo