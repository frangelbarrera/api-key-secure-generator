# API Key Secure Generator

A robust GitHub Action designed to create cryptographically secure API keys for your CI/CD pipelines. This action leverages Python's built-in `secrets` module to ensure high entropy and randomness, making it ideal for generating tokens, passwords, or any sensitive identifiers in automated workflows.

## Key Benefits
- **Cryptographic Security**: Utilizes `secrets.token_urlsafe()` for URL-safe, high-entropy keys.
- **Configurable Length**: Customize key length to meet your security requirements.
- **Log Protection**: Automatically masks generated keys in GitHub Actions logs to prevent accidental exposure.
- **Docker-Based**: Runs in a lightweight Alpine Linux container for fast execution.
- **Output Integration**: Seamlessly integrates with subsequent workflow steps via GitHub outputs.

## Prerequisites
- Python 3.11 or higher (included in the container).
- No external dependencies required beyond standard library.

## Quick Start

Add this action to your GitHub workflow to generate a secure API key:

```yaml
- name: Create Secure API Key
  id: generate_key
  uses: frangelbarrera/api-key-secure-generator@v1.1
  with:
    KEY_LENGTH: 64  # Optional: specify key length in bytes (default: 32)

- name: Use the Generated Key
  run: echo "New API Key: ${{ steps.generate_key.outputs.key }}"
```

### Parameters
- `KEY_LENGTH` (optional): The byte length of the generated key. Must be a positive integer. Default is 32, producing approximately 43 characters in base64.

### Outputs
- `key`: The generated secure API key, ready for use in your workflow.

## How It Works
1. The action accepts a configurable key length via the `KEY_LENGTH` input.
2. It validates the input to ensure it's a positive integer.
3. Using Python's `secrets` module, it generates a URL-safe random string.
4. The key is masked in logs and set as a workflow output for secure consumption.

## Security Considerations
- Keys are generated using cryptographically strong random number generators.
- Generated keys are automatically masked in GitHub Actions logs.
- Never log or expose keys in plaintext within your workflows.
- Rotate keys regularly and store them securely (e.g., in GitHub Secrets).

## Examples
### Basic Usage
```yaml
- uses: frangelbarrera/api-key-secure-generator@v1.1
```

### Custom Length
```yaml
- uses: frangelbarrera/api-key-secure-generator@v1.1
  with:
    KEY_LENGTH: 128
```

### Integration with Secrets
```yaml
- name: Generate and Store Key
  id: key_gen
  uses: frangelbarrera/api-key-secure-generator@v1.1

- name: Update Secret
  uses: actions/github-script@v6
  with:
    script: |
      github.rest.actions.createOrUpdateRepoSecret({
        owner: context.repo.owner,
        repo: context.repo.repo,
        secret_name: 'MY_API_KEY',
        encrypted_value: btoa('${{ steps.key_gen.outputs.key }}')
      })
```

## Development
To test locally:
```bash
python -m unittest test_run.py
docker build -t secure-key-gen .
```

## Contributing
We welcome contributions! Feel free to submit issues, feature requests, or pull requests to improve this action.

## License
Licensed under the MIT License. See LICENSE file for details.

## Links
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python Secrets Module](https://docs.python.org/3/library/secrets.html)