#!/bin/bash
# Sync script for domain experts to easily commit and push their changes

# Ensure we are at the root of the repo
cd "$(dirname "$0")/.."

echo "Checking branch status..."
BRANCH=$(git branch --show-current)

# If on a default branch, create a new branch for the changes
if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ]; then
    NEW_BRANCH="update-$(date +%Y%m%d%H%M%S)"
    echo "On default branch '$BRANCH'. Creating new branch '$NEW_BRANCH'..."
    git checkout -b "$NEW_BRANCH"
    BRANCH="$NEW_BRANCH"
else
    echo "Pulling latest changes on current branch..."
    git pull origin "$BRANCH" || true
fi

echo "Staging files..."
git add .

# Try to build a descriptive commit message based on modified files
MODIFIED_PROMPTS=$(git diff --name-only --cached | grep "prompts/\|workflows/" | head -n 1)

if [ -z "$MODIFIED_PROMPTS" ]; then
    COMMIT_MSG="Sync changes"
else
    FILE_NAME=$(basename "$MODIFIED_PROMPTS")
    COMMIT_MSG="Update prompt metadata and content for $FILE_NAME"
fi

echo "Committing with message: '$COMMIT_MSG'..."
git commit -m "$COMMIT_MSG" || echo "No changes to commit"

echo "Pushing changes..."
git push -u origin "$BRANCH"

echo ""
echo "======================================"
echo "Sync Complete! 🎉"
echo "Your changes have been saved."
ORIGIN_URL=$(git config --get remote.origin.url || echo "https://github.com/org/repo")
if [[ "$ORIGIN_URL" == *"github.com"* ]]; then
    HTTP_URL=$(echo $ORIGIN_URL | sed -e 's/git@github.com:/https:\/\/github.com\//' -e 's/\.git$//')
    echo "Create a Pull Request here: $HTTP_URL/pull/new/$BRANCH"
fi
echo "======================================"
