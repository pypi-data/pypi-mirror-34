# Review Ipsum

Review Ipsum python package - Lorem Ipsum generated with a review theme. Create review of _x_ number of sentences.


# Installation

Use pip:

```
pip install review_ipsum
```


# Usage

Args:
    number_of_sentences (int): The number of sentences desired.

Returns:
    A paragraph of formatted sentences.

e.g:

```
>>> from review_ipsum import create_review
>>> create_review(number_of_sentences=6)
<<< "The screen size is just what I need. Took longer than I expected. So fast. I did'nt even know movies could look this good! Awesome product! Will buy this again. Great deal. "
```

# Code Style

This package uses [pre-commit](https://pre-commit.com/) to enforce coding style. These pre-made commit hooks can be installed with:

```bash
$ pre-commit install -f --install-hooks
```

Current style checking tools are:

- isort: python import sorting
- flake8: python linting
- black: explicit python code formatting

Note: Some hooks require python 3.6 to be available on your path.



# Contributing

1. Fork it!
2. Create your feature branch (`git checkout -b my-newfeature`)
3. Commit your changes (`git commit -m 'Some helpful feature'`)
4. Push (`git push origin my-new-feature`)
5. Create a new Pull Request
