=========
DB Logger
=========

DB Logger is a simple Django app to save logs to database.

Quick start
-----------

1. Add "db_logger" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'db_logger',
    ]

2. Run `python manage.py migrate` to create the polls models.

3. Add handler and logger to LOGGING setting like this::

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                'datefmt': "%d/%b/%Y %H:%M:%S"
            },
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'db_log': {
                'level': 'DEBUG',
                'class': 'db_logger.handlers.DbLogHandler'
            },
        },
        'loggers': {
            '': {
                'handlers': ['db_log'],
                'level': 'DEBUG',
            }
        }
    }

4. Visit /admin/db_logger/dblogentry/ to check the logs.
