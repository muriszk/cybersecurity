## Commit Convention

This repository follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to maintain a clean, readable, and professional project history.

### Structure
All commits must follow this strict format:
`type(optional-scope): description in the imperative`

### Allowed Types
* **`feat`**: Adds a new script, tool, or feature.
* **`fix`**: Fixes a bug, crash, or execution error.
* **`sec`**: Security improvements, mitigations, or vulnerability patches.
* **`docs`**: Updates to documentation (e.g., `README.md`, inline comments).
* **`refactor`**: Code changes that neither fix a bug nor add a feature (e.g., optimizing logic).
* **`chore`**: Maintenance tasks, dependency updates, or environment configuration.
* **`test`**: Adding or updating automated tests.

### Golden Rules
1. **Use the imperative mood:** Write `add script` instead of `added` or `adding`. Treat the commit as an order given to the codebase.
2. **Lowercase:** The description must start with a lowercase letter.
3. **No periods:** Do not end the commit message with a period (`.`).
4. **Length limit:** Keep the first line (the title) under 50 characters.

### Good Examples
* `feat(network): add initial python port scanner`
* `fix(socket): resolve timeout exception on closed ports`
* `refactor(threads): optimize parallel execution for faster scanning`
* `docs(readme): add commit convention guidelines`