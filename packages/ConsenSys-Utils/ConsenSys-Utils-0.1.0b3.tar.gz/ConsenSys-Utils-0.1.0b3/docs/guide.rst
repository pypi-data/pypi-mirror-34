=====
Guide
=====

About ConsenSys-Utils
=====================

ConsenSys-Utils is a library including a set of utility resources used on a daily basis
by ConsenSys France Engineering team.

Create a Flask Application
==========================

Quickstart
~~~~~~~~~~

ConsenSys-Utils provides multiple features to create a Flask application.
In particular ConsenSys-Utils helps you implement the Application factory pattern

#. Create a :file:`app.py`

    .. doctest::

        >>> from consensys_utils.flask import FlaskFactory
        >>> from consensys_utils.flask.cli import FlaskGroup

        # Create an application factory
        >>> create_app = FlaskFactory(__name__)

        # Declares a click application using ConsenSys-Utils click group
        >>> cli = FlaskGroup(create_app=create_app)

#. Define an entry point in :file:`setup.py`::

    from setuptools import setup

    setup(
        name='my-app',
        ...,
        entry_points={
            'console_scripts': [
                'my-app=app:cli'
            ],
        },
    )

#. Install the application and start the application

    .. code-block:: bash

        $ pip install -e .
        $ my-app run --config config.yml

    Note that

    - ``config.yml`` is your .yml configuration file
    - you don't need to set ``FLASK_APP`` environment variable
    - ``run`` command reads ``FLASK_ENV`` environment variable. If ``FLASK_ENV=production`` the application will be run using a ``gunicorn`` server otherwise it uses ``werkzeug`` default development server

Advanced usage
~~~~~~~~~~~~~~

Class :class:`consensys_utils.flask.FlaskFactory` allows you to

- `provide a specific yaml configuration loader`_
- `provide specifics WSGI middlewares`_
- `initialize specifics Flask extensions`_
- `set application hooks`_
- `register specifics Flask blueprints`_

.. _`provide a specific yaml configuration loader`:

Change configuration loader
```````````````````````````

By default :class:`consensys_utils.flask.FlaskFactory` uses a .yml configuration that
validates against :class:`consensys_utils.config.schema.flask.ConfigSchema`.
If you like you can define your own configuration loader.

.. doctest::
    >>> from consensys_utils.flask import FlaskFactory
    >>> from consensys_utils.flask.cli import FlaskGroup
    >>> from cfg_loader import ConfigSchema, YamlConfigLoader
    >>> from marshmallow import fields

    # Declare you configuration schema and config loader
    >>> class MySchema(ConfigSchema):
    ...     my_parameter = fields.Str()

    >>> yaml_config_loader = YamlConfigLoader(config_schema=MySchema)

    # Create an application factory
    >>> create_app = FlaskFactory(__name__, yaml_config_loader=yaml_config_loader)

    # Declares a click application using ConsenSys-Utils click group
    >>> cli = FlaskGroup(create_app=create_app)

.. _`provide specifics WSGI middlewares`:

Add WSGI Middlewares
````````````````````

You can define your own WSGI middlewares and have it automatically applied on your application

.. doctest::
    >>> from consensys_utils.flask import FlaskFactory
    >>> from consensys_utils.flask.cli import FlaskGroup
    >>> import base64

    >>> class AuthMiddleware:
    ...     def __init__(self, wsgi):
    ...         self.wsgi = wsgi
    ...
    ...     @staticmethod
    ...     def is_authenticated(header):
    ...         if not header:
    ...             return False
    ...         _, encoded = header.split(None, 1)
    ...         decoded = base64.b64decode(encoded).decode('UTF-8')
    ...         username, password = decoded.split(':', 1)
    ...         return username == password
    ...
    ...     def __call__(self, environ, start_response):
    ...         if self.is_authenticated(environ.get('HTTP_AUTHORIZATION')):
    ...             return self.wsgi(environ, start_response)
    ...         start_response('401 Authentication Required',
    ...             [('Content-Type', 'text/html'),
    ...              ('WWW-Authenticate', 'Basic realm="Login"')])
    ...         return [b'Login']

    >>> middlewares = {
    ...     'auth': AuthMiddleware,
    ... }

    # Create an application factory
    >>> create_app = FlaskFactory(__name__, middlewares=middlewares)

    # Declares a click application using ConsenSys-Utils click group
    >>> cli = FlaskGroup(create_app=create_app)

.. _`initialize specifics Flask extensions`:

Add Flasks Extension
````````````````````

You can declare your own flask extensions

.. doctest::
    >>> from consensys_utils.flask import FlaskFactory
    >>> from consensys_utils.flask.cli import FlaskGroup
    >>> from flasgger import Swagger

    >>> swag = Swagger(template={'version': '0.3.4-dev'})

    >>> my_extensions = {'swagger': swag}

    # Create an application factory
    >>> create_app = FlaskFactory(__name__, extensions=my_extensions)

    # Declares a click application using ConsenSys-Utils click group
    >>> cli = FlaskGroup(create_app=create_app)

:class:`consensys_utils.flask.FlaskFactory` also extensions given as a
function taking a :class:`flask.Flask` application as an argument

.. doctest::
    >>> from consensys_utils.flask import FlaskFactory
    >>> from consensys_utils.flask.cli import FlaskGroup

    >>> def init_login_extension(app):
    ...     if app.config.get('LOGIN'):
    ...         from flask_login import LoginManager
    ...
    ...         login_manager = LoginManager()
    ...         login_manager.init_app(app)

    >>> my_extensions = {'login': init_login_extension}

    # Create an application factory
    >>> create_app = FlaskFactory(__name__, extensions=my_extensions)

    # Declares a click application using ConsenSys-Utils click group
    >>> cli = FlaskGroup(create_app=create_app)

It allows you to implement advanced extension initialization based on application configuration.
In particular in the example above it allows to allows user having 'Flask-Login' installed on option,
only users having activated a ``LOGIN`` configuration need to have 'Flask-Login' installed.

.. _`set application hooks`:


Set Application Hooks
`````````````````````

.. doctest::
    >>> from consensys_utils.flask import FlaskFactory
    >>> from consensys_utils.flask.cli import FlaskGroup

    >>> def set_log_request_hook(app):
    ...     @app.before_request
    ...     def log_request():
    ...         current_app.logger.debug(request)

    >>> my_hook_setters = {'log-request': set_log_request_hook}

    # Create an application factory
    >>> create_app = FlaskFactory(__name__, hook_setters=my_hook_setters)

    # Declares a click application using ConsenSys-Utils click group
    >>> cli = FlaskGroup(create_app=create_app)

.. _`register specifics Flask blueprints`:

Register Blueprints
```````````````````
.. doctest::
    >>> from flask import Blueprint
    >>> from consensys_utils.flask import FlaskFactory
    >>> from consensys_utils.flask.cli import FlaskGroup


    >>> my_bp1 = Blueprint('my-bp1', __name__)
    >>> my_bp2 = Blueprint('my-bp2', __name__)

    >>> blueprints = {
    ...     'my-bp1': my_bp1,
    ...     'my-bp2': lambda app: app.register_blueprint(my_bp2),
    ... }

    # Create an application factory
    >>> create_app = FlaskFactory(__name__, blueprints=blueprints)

    # Declares a click application using ConsenSys-Utils click group
    >>> cli = FlaskGroup(create_app=create_app)

