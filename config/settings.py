"""
config data
"""

"""
github credentials:
actual password and other secrets should be removed before pushing to open repository

tests that require these credentials would fail being run without it,
therefore, skipif mark for those tests with the condition PASSWORD == ""
"""
LOGIN = "devautotests"
PASSWORD = ""

"""
test users urls
"""
USER_PROFILE = "https://github.com/devautotests"
ALIEN_PROFILE = "https://github.com/devautotests2"

"""
test repositories urls
"""
USER_PUBLIC_REPOSITORY = "https://github.com/devautotests/devautotests_public"
USER_PRIVATE_REPOSITORY = "https://github.com/devautotests/devautotests_private"
ALIEN_PUBLIC_REPOSITORY = "https://github.com/devautotests2/devautotests2-public"
ALIEN_PRIVATE_REPOSITORY = "https://github.com/devautotests2/devautotests2-private"
ALIEN_PRIVATE_REPOSITORY_SHARED = "https://github.com/devautotests2/devautotests2-private-shared"
