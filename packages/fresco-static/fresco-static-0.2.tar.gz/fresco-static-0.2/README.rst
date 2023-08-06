fresco-static - static file serving for fresco
==============================================


Basic usage
-----------

First you need a fresco app. Here's one I made earlier::

    app = FrescoApp()

Let's assume this lives in an application that's structured like this::

    mypackage
    ├── __init__.rst
    ├── app.py
    ├── static
    │   └── photo.jpg
    └── setup.py


Once you have the app, you can create an instance of ``StaticFiles``:

.. code-block:: python

    static = StaticFiles(app)

StaticFiles automatically adds routes for the path ``/static``.
Static files will be available under ``/static/<packagename>/<path>``
eg ``/static/mypackage/photo.jpg``. You can change these defaults:

.. code-block:: python

    static = StaticFiles(app,
                         prefix='/media',
                         route_name='media',
                         cache_max_age=3600)

You can have multiple packages serving files through a single StaticFiles
object without fear of conflict.

Now you can start configuring static source directories:

.. code-block:: python

    # Mount directory '/www/mysite/htdocs'. The first argument is an arbitrary
    # name used to identify this source. You can use whatever string you like.
    static.add_directory('site-htdocs', '/site/htdocs', cache_max_age=60)

    # Serve files located in a 'subdir' directory within the python package
    # 'mypackage'
    static.add_package('mypackage', 'subdir', cache_max_age=86400)

The ``cache_max_age`` argument specifies for how long (in seconds)
browsers and proxies can cache responses.
For development you might want to set this to zero,
but in production use you should
set this to a reasonable value and
configure a caching HTTP proxy server.
When adding source directories you can omit this argument, and the default
(configured when you created the ``StaticFiles`` object)
will be used instead.

``static.pathfor`` generates URLs for static content.
You will probably want to include this
in your templating system's default namespace. How you do that depends on how
you've integrated the templating system, but it would typically be something
like this:

.. code-block:: python

    templating.contextprocessor({'static': static.pathfor})

Call this in templates to link to static files, eg:

.. code-block:: html

    <!-- Reference a file from the "site-htdocs" source
    -->
    <img src="{{ static('site-htdocs/photo.jpg') }}" alt="My photo" />

    <!-- Reference a file from the "mypackage" source
    -->
    <img src="{{ static('mypackage/photo.jpg') }}" alt="My photo" />

    <!-- Path doesn't begin with a source name — all sources will be
         searched for a matching file
    -->
    <img src="{{ static('cat-pictures/miaow.gif') }}" alt="My photo" />
