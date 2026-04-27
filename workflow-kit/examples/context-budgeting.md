# Example: Context Budgeting

Weak instruction:

> Build the app, make it clean, follow best practices, add tests, document everything.

Better instruction:

> Implement the checkout validation rule in the application layer. Keep API controllers thin, return structured validation errors, and add tests for valid input, missing customer, invalid quantity, and unavailable stock.

Why it works:

- It names the layer.
- It defines expected error behavior.
- It gives concrete test cases.
- It avoids broad, vague documentation requests.
