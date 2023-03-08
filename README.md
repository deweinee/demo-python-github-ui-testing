# UI autotests example for [github.com](https://github.com/)

### Technology stack:
Python, PyTest, Selenium

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
