# paytext

[![Build Status](https://scrutinizer-ci.com/g/yhoiseth/paytext/badges/build.png?b=master)](https://scrutinizer-ci.com/g/yhoiseth/paytext/build-status/master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/yhoiseth/paytext/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/yhoiseth/paytext/?branch=master)
[![Code Coverage](https://scrutinizer-ci.com/g/yhoiseth/paytext/badges/coverage.png?b=master)](https://scrutinizer-ci.com/g/yhoiseth/paytext/?branch=master)
[![PyPI version](https://badge.fury.io/py/paytext.svg)](https://badge.fury.io/py/paytext)

Python package to generalize texts from payments.

## Motivation

When categorizing payments, I want to avoid categorizing the same type of expense multiple times. Often, the only information we have about a payment is the date, amount and a slightly cryptic string. For example, I recently bought some plane tickets using [Ticket](https://www.ticket.no/). On my account statement, that produced a string similar to this one: `*4274 25.06 NOK 4101.00 WWW.TICKET.NO Kurs: 1.0000`.

Now, when I put this payment in the _Travel_ category, I'd like all future payments to the same vendor to be automatically put in the same category. But the next time I buy a plane ticket from them, the date and amount will be different. Also, the leading card number may be different, too. So, in order to automate the categorization, we need to _generalize_ the text. In other words, `*4274 25.06 NOK 4101.00 WWW.TICKET.NO Kurs: 1.0000` needs to become `WWW.TICKET.NO`. That's what this tiny package does.

## Installation

Use [Pipenv](https://docs.pipenv.org/): `pipenv install paytext`

## Usage

```python
from paytext import PaymentText

payment_text: PaymentText = PaymentText(
    '*4274 25.06 NOK 4101.00 WWW.TICKET.NO Kurs: 1.0000',
)

print(payment_text) # Output: '*4274 25.06 NOK 4101.00 WWW.TICKET.NO Kurs: 1.0000' 

payment_text.generalize()

print(payment_text) # Output: 'WWW.TICKET.NO'

```

## Known limitations

I've mostly had strings from transactions with Norwegian merchants and banks to work with, so this package probably won't work as well with other languages/locales. If you find strings that it doesn't handle well, please [open an issue on GitHub](https://github.com/yhoiseth/payment-card-text/issues/new).

## Running tests

Run the command `nosetests`.

## Upload new release to the Python Package Index

1. Update version number in [setup.py](setup.py).
2. Make new distribution: `python setup.py sdist bdist_wheel`
3. Upload to PyPI: `twine upload dist/*`
