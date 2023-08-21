## Test task for DockuSketch | FastAPI Example

This repository contains an example FastAPI application that demonstrates basic usage of FastAPI features, including request logging, response logging, error handling, and routing.

[![Maintainability](https://api.codeclimate.com/v1/badges/b07d162221bb5e22a5bf/maintainability)](https://codeclimate.com/github/sergdemc/dockusketch_task/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b07d162221bb5e22a5bf/test_coverage)](https://codeclimate.com/github/sergdemc/dockusketch_task/test_coverage)

## Installation

### Prerequisites

#### Python

Before installing the package make sure you have Python version 3.6 or higher installed:

```bash
>> python --version
Python 3.6+
```

#### Poetry

The project uses the Poetry dependency manager. To install Poetry use its [official instruction](https://python-poetry.org/docs/#installation).

### Application

To use the application, you need to clone the repository to your computer. This is done using the `git clone` command. Clone the project:

```bash
>> git clone https://github.com/sergdemc/python-project-52.git && cd python-project-52
```

Then you have to install all necessary dependencies:

```bash
>> make install
```

## Usage

Start the gunicorn Django server by running:
```bash
make start
```
By default, the server will be available at http://0.0.0.0:8000. 


## Features
### Logging
The application utilizes custom logging using the custom_logging module. Logs are recorded for incoming requests, responses, and errors. Logs are configured to provide insightful information about the application's behavior. The logs are written to the console and to a file.

### Endpoints
The following endpoints are available:

- Root Endpoint: /
  - Method: GET
  - Description: Returns a friendly greeting message.
- Get Your Job: /jobs/{job_id}
  - Method: GET
  - Description: Retrieves a job description based on the provided job ID.
  Method: GET

### Middleware
The application uses middleware functions to log incoming requests and outgoing responses. This provides visibility into the interactions between the client and the server.

### Error Handling
Errors occurring during request processing are captured and logged, providing insights into any issues that may arise during application execution.

### Linter
The application uses the Flake8 linter to ensure code quality and consistency. To run the linter, run the following command from the root directory:

```bash
>> make lint
```

### Testing
To run the test suite, run the following command from the root directory:

```bash
>> make test
```

### Code Coverage
To run the test suite and generate a code coverage report, run the following command from the root directory:

```bash
>> make coverage
```

### Contributing
Contributions to this test app are welcome! Feel free to submit pull requests to add new features, improve documentation, or fix any issues.