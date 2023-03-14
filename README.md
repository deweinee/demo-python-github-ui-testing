# UI autotests example for [github.com](https://github.com/)

### Technology stack
Python, PyTest, Selenium

### Run
In Chrome (default configuration): `pytest`

In Firefox: `pytest --browser_name=firefox`


### Tests
#### Login tests:
1. Authorization with correct login and password should be successful
2. Authorization with incorrect password should fail
3. Authorization with empty password should fail
#### Repository access tests:
1. Public repository should be accessible for unauthorized user
2. Private repository should not be accessible for unauthorized user
3. User's own private repository should be accessible for the authorised user
4. Shared repository should be accessible for the authorized user
5. Someone else's private repository should not be accessible for the authorized user
#### User profile page tests:
1. Unauthorized user should be redirected to login page after clicking 'follow' button

-----

#### Very basic CI/CD is set up for this repository:
  - A workflow with pylint checks is created in GitHub Actions
  - Direct merging into main is prohibited, all commits must be made to a non-protected branch and submitted via a pull request
  - All conversations on code must be resolved before a pull request can be merged
  - Pylint checks must pass before merging a pull request
  
