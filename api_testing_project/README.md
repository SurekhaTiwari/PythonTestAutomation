# Simple API Testing Project (Python + requests + pytest)

## Setup
```bash
pip install -r requirements.txt
pytest
```
(Internet access is needed because the tests call public APIs.)

## Project structure
```
api_testing_project/
├── requirements.txt
├── pytest.ini
├── tests/test_api.py                 # Python API automation
└── postman/
    ├── api_testing.postman_collection.json
    └── local.postman_environment.json
```

## Module 11 coverage

| Module 11 topic                        | Where it is covered                                   |
|----------------------------------------|-------------------------------------------------------|
| API fundamentals, HTTP/HTTPS           | All tests (HTTPS endpoints, requests Session)         |
| GET, POST, PUT, PATCH, DELETE          | tests 1, 3, 4, 5, 6                                   |
| Requests and responses                 | Every test (status, headers, body)                    |
| Headers                                | `test_custom_request_header`, Content-Type checks     |
| Parameters                             | `test_get_with_query_parameters`                      |
| JSON and XML                           | JSON in CRUD tests, `test_xml_response`               |
| Authentication and authorization       | Basic Auth and Bearer token tests                     |
| Status codes                           | `test_various_status_codes` (parameterized)           |
| Positive and negative API testing      | 404, wrong password (401), missing token (401)        |
| Postman: collections, environments     | `postman/` folder (import both JSON files)            |
| Pre-request and test scripts           | Inside the Postman collection                         |
| API automation using Python            | `tests/test_api.py`                                   |

## REST vs SOAP (concept note)
- **REST**: uses HTTP verbs, usually JSON, lightweight (what this project tests).
- **SOAP**: XML-only envelopes over HTTP, strict WSDL contract, heavier.

## Using Postman
1. Import both files from `postman/`.
2. Select the "Demo Environment" in the top-right.
3. Run the collection with the Collection Runner.
