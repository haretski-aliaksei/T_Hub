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
├── tests/
│   ├── api/
│   └── ui/
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
