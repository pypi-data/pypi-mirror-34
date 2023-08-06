# Toto9 - The Missing GCP Python Client

The Google Python Client Library is missing stuff! This package fills in the gaps.

## Installation

*Development Environment*

Run `pip install -e .` from the root level of this repository. This symlinks the package so that source files are available as soon as they are updated.

### Development

- `export GOOGLE_APPLICATION_CREDENTIALS=PATH_TO_YOUR_CREDENTIALS_FILE`
- `export GOOGLE_PROJECT_ID=YOUR_PROJECT_ID` (for tests)
- `virtualenv -p python3 venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `pip install -e .`

*All Other Environments*

`pip install toto9`

## Usage

### Authentication

Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your credentials. Alternatively, pass in the path to your credentials and list of scopes to the service classes with `credentials_path` and `scopes` kwargs.

## Contributing

- Create an issue in gitlab
- Write the code
- Write tests, make sure they are meaningful and pass
- Submit MR against issue
- Merge

## References

- https://developers.google.com/api-client-library/python/
- https://google-cloud-python.readthedocs.io/en/latest/index.html

## Test

You should test your modules! Tests are in the `tests` directory. Name your file `test_*.py` so the unittest module will pick it up.

## Documentation

Update documentation in `docs/source` and then run `make html` from the `docs` directory.

### Setup and Run

`
export GOOGLE_PROJECT_ID=YOUR_PROJECT_ID
export GOOGLE_APPLICATION_CREDENTIALS=PATH_TO_YOUR_CREDENTIALS_FILE
`

Run all tests with `python -m unittest`.
