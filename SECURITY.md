# Security Policy

## Reporting Security Vulnerabilities

We take security vulnerabilities seriously. If you discover a security issue, please report it responsibly.

### Reporting Process

1. **Do NOT** create a public GitHub issue for security vulnerabilities
2. Email security concerns privately to the maintainers
3. Include detailed information about the vulnerability:
   - Description of the issue
   - Steps to reproduce
   - Potential impact
   - Any suggested fixes (optional)

### Scope

This policy applies to:
- The main application code (`app.py`)
- Frontend templates (`templates/`)
- GitHub Actions workflows (`.github/workflows/`)
- All dependencies listed in `requirements.txt`

## SAMD Compliance

This project follows Secure AI Model Development (SAMD) principles:

### 1. Code Quality & Security
- Regular CodeQL security scanning
- Bandit security linting
- Input validation and sanitization
- Secure coding practices

### 2. Dependency Management
- Automated vulnerability scanning (Safety)
- License compliance verification
- Regular dependency updates

### 3. Secret Management
- No hardcoded secrets
- GitLeaks secret detection
- Environment variable usage for sensitive data

### 4. AI Model Safety
- Input validation for all user inputs
- Output sanitization
- Rate limiting
- Content filtering

### 5. Access Control
- Minimal permissions principle
- Secure API design
- Authentication best practices

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | ✅ Active Development |

## Security Updates

Security updates will be released as patch versions and communicated through:
- GitHub Security Advisories
- Release notes

## Attribution

Thank you for helping keep this project secure!
