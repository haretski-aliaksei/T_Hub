import re

CURRENCY_PATTERN = re.compile(r"\$(\d+\.\d{2})")


def parse_currency(text):
    match = CURRENCY_PATTERN.search(text)

    if not match:
        raise ValueError(f"No currency amount found in: {text!r}")

    return float(match.group(1))
