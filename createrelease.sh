#!/bin/bash

# Function to extract version from pyproject.toml
get_pyproject_version() {
    grep '^version' pyproject.toml | sed 's/version *= *"\([^"]*\)"/\1/'
}

# Function to validate version number format
validate_version() {
    if ! [[ $1 =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        echo "Error: Version must be in format x.y.z (e.g., 1.0.0)"
        exit 1
    fi
}

# Main release process
create_release() {
    local version=$1
    
    # Check version in pyproject.toml
    local pyproject_version=$(grep '^version' pyproject.toml | sed 's/version *= *"\([^"]*\)"/\1/')
    if [ "$version" != "$pyproject_version" ]; then
        echo "Error: Version in pyproject.toml ($pyproject_version) does not match argument ($version)"
        exit 1
    fi

    echo "🚀 Starting release process for v$version"
    
    # Activate virtual environment
    echo "🐍 Activating virtual environment..."
    source venv/Scripts/activate
    
    # Build package
    echo "🔨 Building package..."
    python -m build
    
    # Check package
    echo "🔍 Checking package..."
    python -m twine check dist/*
    
    # Upload to PyPI
    echo "🚀 Uploading to PyPI..."
    python -m twine upload dist/*
    if [ $? -ne 0 ]; then
        echo "❌ PyPI upload failed. Aborting release."
        exit 1
    fi
    
    # Ensure we're on main branch and it's up to date
    echo "📥 Updating main branch..."
    git checkout main
    git pull origin main
    
    # Create tag
    echo "🏷️ Creating release tag 'v$version'..."
    git tag -a "v$version" -m "Release version $version"
    
    # Push changes
    echo "📤 Pushing tag 'v$version'..."
    git push origin "v$version"
    
    echo "✅ Release process completed for version v$version"
}

# Script usage
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <version>"
    echo "Example: $0 1.0.0"
    exit 1
fi

# Validate and create release
validate_version $1
create_release $1