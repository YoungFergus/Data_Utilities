SERVICE_USER_SCRIPT = """
    BEGIN

    USER ROLE SECURITYADMIN;

    CREATE USER {username}
        PASSWORD = '{password}'
        LOGIN_NAME = {username}
        DISPLAY_NAME = 'Service User';

    END;
"""

PERSONAL_USER_SCRIPT = """
    BEGIN

    USE ROLE SECURITYADMIN;

    CREATE USER {basename}
        PASSWORD = ''
        LOGIN_NAME = '{email}'
        DISPLAY_NAME = '{basename}'
        EMAIL = '{email}';

    END;
"""