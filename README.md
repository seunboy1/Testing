# Testing
This project provides resources and examples for various software testing concepts and practices. It aims to be a valuable learning tool for developers and testers.

## Testing Tools Overview

### PyTest

- Pytest is a popular Python testing framework known for its flexibility, expressiveness, and ease of use. It promotes writing clean, readable tests with features like fixtures, parametrization, and assertions.

### Coverage

- Coverage is a Python library that calculates the percentage of your code that is executed by your tests. This helps you identify areas where you might need to write more tests to achieve better code coverage.

### Installation
 ```bash
    pip install pytest coverage
 ```

## Instructions
- Create a `test` folder
- Create a test file for each of your python file implementation with the name either starting, ending or having `test` in it. Eg `test_` , `_test_`, `_test.py`.
- Write your unit test and integration test in all of the test files.
- You can run your test either by running this at the root directory
    ```bash
        pytest
    ```
    
        Or
    
    ```bash
        pytest test/test_class.py
    ```
    
  




pytest
touch .coveragerc 
[run]
source = src 

coverage run -m pytest                                    
coverage report -m   
coverage html  
