# Contributing to TempMailChecker Python SDK

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/python-disposable-email-checker.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
5. Install dependencies: `pip install -e ".[dev]"`
6. Create a new branch: `git checkout -b feature/your-feature-name`

## Development

### Code Style

- Follow PEP 8 style guide
- Use type hints for all function parameters and return values
- Add docstrings for all public methods
- Keep functions focused and single-purpose

### Testing

- Write tests for new features
- Ensure all tests pass: `pytest`
- Maintain or improve code coverage: `pytest --cov=tempmailchecker`

### Building

- Build before committing: `python -m build`
- Ensure package builds without errors

## Submitting Changes

1. Commit your changes with clear, descriptive messages
2. Push to your fork: `git push origin feature/your-feature-name`
3. Create a Pull Request on GitHub
4. Provide a clear description of your changes

## Reporting Issues

When reporting issues, please include:
- Python version
- Package version
- Steps to reproduce
- Expected vs actual behavior
- Any error messages

## Questions?

Feel free to open an issue for questions or reach out to support@tempmailchecker.com

Thank you for contributing! 🎉

