# QA Automation Home Assignment

This repository contains automated API and UI tests for the Senior QA Engineer home assignment.

## Tech Stack

- Python
- pytest
- requests
- Playwright

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
│       ├── urls.py
│       └── users.py
├── fixtures/
│   ├── __init__.py
│   ├── api.py
│   └── ui.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── login_page.py
├── tests/
│   ├── __init__.py
│   └── api/
│       ├── __init__.py
│       └── products/
│           ├── __init__.py
│           └── test_get_single_product.py
├── utils/
│   ├── __init__.py
│   └── api/
│       ├── __init__.py
│       └── products/
│           ├── __init__.py
│           └── test_data.py
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

Run UI tests only:

```bash
pytest tests/ui
```

## Test Strategy

The test suite is organized around clear separation of concerns:

- test cases describe expected behavior;
- helper code handles API requests and reusable UI interactions;
- assertions validate status codes, response payloads, page states, and user-facing results.

The suite includes positive, negative, and edge case scenarios to provide balanced coverage across API and UI layers.

## API Coverage Notes

The current API suite focuses on the `Products -> Get a single product` endpoint family from DummyJSON.

Covered API scenarios:

- successful retrieval of an existing product;
- validation of selected response fields, data types, and constraints;
- not-found error handling for a dynamically calculated non-existent product ID;
- delayed response handling using the supported `delay` query parameter.

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
