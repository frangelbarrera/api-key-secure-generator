#!/bin/sh -l

# Retrieve the key length from the GitHub Action input, using 32 as fallback
export KEY_LENGTH="${INPUT_KEY_LENGTH:-32}"

# Ensure KEY_LENGTH is a valid positive integer
if ! echo "$KEY_LENGTH" | grep -q '^[0-9]\+$' || [ "$KEY_LENGTH" -le 0 ]; then
    echo "Input error: KEY_LENGTH must be a positive integer above zero" >&2
    exit 1
fi

# Run the Python application to produce the secure key
key=$(python /usr/src/app/run.py)

# Conceal the key in logs to avoid accidental disclosure
echo "::add-mask::$key"

# Export the key as an output parameter for workflow integration
echo "key=$key" >> $GITHUB_OUTPUT