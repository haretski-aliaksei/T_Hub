# QA Automation Home Assignment

This repository contains automated API and UI tests for the Senior QA Engineer home assignment.

## Tech Stack

- Python
- pytest
- requests
- Playwright
- Ruff

## Scope

The solution includes two automation areas:

- API tests for selected endpoints from [DummyJSON](https://dummyjson.com);
- UI end-to-end tests for core user flows of a selected web application.

The API tests focus on:

- successful response validation;
- response structure and data type validation;
- business rule and constraint checks;
- negative scenarios and error handling;
- boundary and edge case coverage.

The UI tests focus on:

- core user journeys;
- form and page state validation;
- interaction with key application elements;
- validation of important user-facing results;
- stable waiting strategies for dynamic content and network activity.

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── tests.yml
├── api/
│   ├── __init__.py
│   ├── client.py
│   └── endpoints/
│       ├── __init__.py
│       └── products.py
├── conftest.py
├── constants/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── products/
│   │   │   ├── __init__.py
│   │   │   ├── constraints.py
│   │   │   ├── fields.py
│   │   │   ├── messages.py
│   │   │   └── test_data.py
│   │   ├── settings.py
│   │   └── urls.py
│   └── ui/
│       ├── __init__.py
│       ├── cart.py
│       ├── checkout.py
│       ├── messages.py
│       ├── products.py
│       ├── urls.py
│       └── users.py
├── fixtures/
│   ├── __init__.py
│   ├── api.py
│   └── ui.py
├── models/
│   ├── __init__.py
│   └── api/
│       ├── __init__.py
│       └── products/
│           ├── __init__.py
│           └── product.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── login_page.py
│   └── products_page.py
├── tests/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── products/
│   │       ├── __init__.py
│   │       ├── test_get_single_product.py
│   │       └── test_search_products.py
│   └── ui/
│       ├── __init__.py
│       ├── test_cart.py
│       ├── test_checkout.py
│       └── test_login.py
├── utils/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── products/
│   │       ├── __init__.py
│   │       └── test_data.py
│   └── ui/
│       ├── __init__.py
│       └── money.py
├── pyproject.toml
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

## Running Tests

```bash
pytest
```

Run API tests only:

```bash
pytest tests/api
```

or:

```bash
pytest -m api
```

Run UI tests only:

```bash
pytest tests/ui
```

or:

```bash
pytest -m ui
```

Run UI tests in headed browser mode:

```bash
pytest tests/ui --headed --browser chromium
```

Run smoke tests only:

```bash
pytest -m smoke
```

Run end-to-end UI tests only:

```bash
pytest -m "ui and e2e"
```

Run negative tests only:

```bash
pytest -m negative
```

## Code Quality

Ruff is used for linting, import ordering, and formatting checks.

Run lint checks:

```bash
ruff check .
```

Check formatting:

```bash
ruff format --check .
```

Apply formatting:

```bash
ruff format .
```

## Test Strategy

The test suite is organized around clear separation of concerns:

- test cases describe expected behavior;
- helper code handles reusable test data preparation;
- API client classes handle API requests and endpoint-specific paths;
- Page Object classes handle reusable UI interactions and locators;
- assertions validate status codes, response payloads, page states, and user-facing results.

The suite includes positive, negative, and edge case scenarios to provide balanced coverage across API and UI layers.

## Pytest Markers

Markers are used to run meaningful subsets of the test suite:

- `api` - API tests;
- `ui` - UI end-to-end tests;
- `smoke` - high-value checks for critical application availability;
- `regression` - tests that protect existing behavior;
- `e2e` - complete user journeys;
- `negative` - error handling or restricted behavior validation.

## API Coverage Notes

The current API suite focuses on the `Products -> Get a single product` endpoint family from DummyJSON.

Covered API scenarios:

- successful retrieval of an existing product, including data type and constraint
  validation for `price`, `stock`, `rating`, and `discountPercentage`;
- not-found error handling for a dynamically calculated non-existent product ID;
- invalid input handling for a non-numeric product ID;
- delayed response handling using the supported `delay` query parameter;
- empty response handling via `Products -> Search` with a query that matches nothing.

Mocked responses are not used because the selected scenarios can be covered reliably against the public DummyJSON API.

## Scalability Approach

The current API structure is intentionally minimal and contains only the implemented `products` endpoint layer and tests.

API tests are organized using layered responsibility:

```text
tests -> endpoint-specific API classes -> common APIClient -> requests
```

As the API coverage grows, new endpoint groups can be added under `api/endpoints/` and `tests/api/` without changing the existing layout:

```text
api/
└── endpoints/
    ├── products.py
    ├── carts.py
    └── users.py

tests/
└── api/
    ├── products/
    ├── carts/
    └── users/
```

This keeps the repository lightweight while still allowing the test suite to scale by resource or business domain.

The common `APIClient` owns reusable HTTP behavior such as base URL handling and request timeout. Endpoint-specific classes, such as `ProductsAPI`, own resource paths and actions. Tests can stay focused on expected behavior instead of request construction details.

## UI Coverage Notes

The current UI suite focuses on core flows for [Sauce Demo](https://www.saucedemo.com).

Covered UI scenarios:

- successful login for a standard user;
- locked-out user error validation;
- adding a product to the cart;
- removing a product from the cart;
- cart badge, item name, and item quantity validation;
- checkout flow from cart to order completion;
- checkout total calculation (item total + tax = total) on the order overview step;
- required-field validation when submitting checkout information with missing data.

The UI tests use Playwright's built-in web-first assertions through `expect`. This allows checks such as URL, visibility, and text validation to wait automatically for the expected browser state.

## UI Scalability Approach

UI tests are organized using the Page Object pattern:

```text
tests -> page objects -> Playwright page
```

Page objects own locators and user actions for a specific screen, for example `LoginPage`, `ProductsPage`, `CartPage`, and `CheckoutPage`. Test cases combine these actions into business flows and keep assertions focused on user-visible results.

As UI coverage grows, new pages and flows can be added without changing the existing structure:

```text
pages/
├── login_page.py
├── products_page.py
├── cart_page.py
├── checkout_page.py
└── ...

tests/
└── ui/
    ├── test_login.py
    ├── test_cart.py
    ├── test_checkout.py
    └── ...
```

Reusable UI values such as URLs, users, product names, expected messages, and checkout data are stored under `constants/ui/`. This avoids spreading string literals across tests and keeps future changes localized.

Fixtures are split by test layer under `fixtures/api.py` and `fixtures/ui.py`, while the root `conftest.py` only registers fixture modules. This keeps the setup readable and still allows API fixtures to be reused in UI or end-to-end tests when needed.

## CI

GitHub Actions workflow is configured in `.github/workflows/tests.yml`.

It runs on push to `main`, pull requests, and manual dispatch.

The workflow executes:

```bash
ruff check .
ruff format --check .
pytest --browser chromium
```

This makes linting, formatting, and automated tests part of the repository quality gate.
