#!/bin/bash

# A script to check the development environment setup.

# Helper function to print a check result
# $1: The name of the tool to check (e.g., "python3")
# $2: The command to run to get the version info (e.g., "python3 --version")
# $3: (Optional) A command to get detailed info, like a list of versions.
check_tool() {
    local tool_name="$1"
    local version_cmd="$2"
    local details_cmd="$3"
    # A custom grep pattern to extract the version info, if the output is complex
    local grep_pattern="$4"

    if command -v "$tool_name" &> /dev/null; then
        # For commands that output version to stderr (e.g., java)
        local output
        if [[ "$tool_name" == "java" || "$tool_name" == "mvn" || "$tool_name" == "gradle" || "$tool_name" == "javac" || "$tool_name" == "clang" || "$tool_name" == "gcc" || "$tool_name" == "chromedriver" || "$tool_name" == "docker" && "$version_cmd" == *"compose"* ]]; then
            output=$($version_cmd 2>&1)
        else
            output=$($version_cmd)
        fi

        local version_info
        if [ -n "$grep_pattern" ]; then
            version_info=$(echo "$output" | grep -oE "$grep_pattern" | head -n 1)
        else
            version_info=$(echo "$output" | head -n 1)
        fi

        # Remove the tool name from the version info if present
        version_info=$(echo "$version_info" | sed -e "s/^$tool_name //i" -e "s/^version //i")

        echo "✅ $tool_name: $version_info"

        if [ -n "$details_cmd" ]; then
            # Execute the details command and indent its output
            eval "$details_cmd" 2>/dev/null | sed 's/^/  /'
        fi
    elif [ "$tool_name" == "pyenv" ] || [ "$tool_name" == "nvm" ]; then
         # Special case for pyenv and nvm, which might be shell functions
         if type "$tool_name" &> /dev/null; then
              echo "✅ $tool_name: available"
              if [ -n "$details_cmd" ]; then
                  eval "$details_cmd" 2>/dev/null | sed 's/^/  /'
              fi
         else
              echo "❌ $tool_name: not found"
         fi
    else
        echo "❌ $tool_name: not found"
    fi
}

# --- Python ---
echo "-------- Python --------"
check_tool "python3" "python3 --version"
check_tool "python" "python --version"
check_tool "pip" "pip --version"
check_tool "pipx" "pipx --version"
check_tool "poetry" "poetry --version"
check_tool "uv" "uv --version"
check_tool "black" "black --version"
check_tool "mypy" "mypy --version"
check_tool "pytest" "pytest --version"
check_tool "ruff" "ruff --version"
check_tool "pyenv" "pyenv --version" "pyenv versions"

# --- NodeJS ---
echo ""
echo "-------- NodeJS --------"
check_tool "node" "node --version" "nvm list"
check_tool "nvm" "nvm" "nvm list"
check_tool "npm" "npm --version"
check_tool "yarn" "yarn --version"
check_tool "pnpm" "pnpm --version"
check_tool "eslint" "eslint --version"
check_tool "prettier" "prettier --version"
check_tool "chromedriver" "chromedriver --version"

# --- Java ---
echo ""
echo "-------- Java --------"
check_tool "java" "java -version"
check_tool "maven" "mvn --version" "" "Apache Maven [0-9.]+"
check_tool "gradle" "gradle --version" "" "Gradle [0-9.]+"

# --- Go ---
echo ""
echo "-------- Go --------"
check_tool "go" "go version"

# --- Rust ---
echo ""
echo "-------- Rust --------"
check_tool "rustc" "rustc --version"
check_tool "cargo" "cargo --version"

# --- C/C++ Compilers ---
echo ""
echo "-------- C/C++ Compilers --------"
check_tool "clang" "clang --version"
check_tool "gcc" "gcc --version"
check_tool "cmake" "cmake --version"
check_tool "ninja" "ninja --version"
check_tool "conan" "conan --version"

# --- Docker ---
echo ""
echo "-------- Docker --------"
check_tool "docker" "docker --version"
check_tool "docker" "docker compose version"

# --- Other Utilities ---
echo ""
echo "-------- Other Utilities --------"
check_tool "awk" "awk --version"
check_tool "curl" "curl --version"
check_tool "git" "git --version"
check_tool "grep" "grep --version"
check_tool "gzip" "gzip --version"
check_tool "jq" "jq --version"
check_tool "make" "make --version"
check_tool "rg" "rg --version"
check_tool "sed" "sed --version"
check_tool "tar" "tar --version"
check_tool "tmux" "tmux -V"
check_tool "yq" "yq --version"
