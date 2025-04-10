#!/bin/bash
# GitHub CLI Login Script
# This script handles authentication with GitHub and refreshes permissions

# Check if GitHub CLI is installed
if ! command -v gh &> /dev/null; then
    echo "GitHub CLI (gh) is not installed. Installing now..."
    if command -v brew &> /dev/null; then
        brew install gh
    else
        echo "Error: Homebrew is not installed. Please install GitHub CLI manually."
        exit 1
    fi
fi

echo "Starting GitHub authentication process..."

# Check if already logged in
if gh auth status &> /dev/null; then
    echo "Already authenticated with GitHub."
    
    # Ask user if they want to re-authenticate
    read -p "Do you want to re-authenticate? (y/n): " REPLY
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Authentication refresh skipped."
        exit 0
    fi
    
    # Logout first if re-authenticating
    echo "Logging out of current GitHub session..."
    gh auth logout
fi

# Login via web browser (most user-friendly method)
echo "Opening browser for GitHub authentication..."
gh auth login --web

# Check if login was successful
if ! gh auth status &> /dev/null; then
    echo "GitHub authentication failed. Please try again."
    exit 1
fi

echo "Successfully authenticated with GitHub."

# Refresh token with additional permissions
echo "Refreshing with additional permissions (repo, read:org)..."
gh auth refresh -h github.com -s repo,read:org

# Verify the authentication status
echo "Verifying GitHub authentication..."
gh auth status

echo "GitHub authentication and permission setup complete."