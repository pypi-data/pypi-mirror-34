=======
Web App
=======

Polls is a simple Django app to conduct Web-based polls. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "web_app" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'web_app',
    ]

2. Include the web_app URL conf in your project urls.py like this::

    url(r"^web_app/", include("web_app.urls", namespace="web_app")),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a web_app (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/web_app/web/app/index/ to participate in the web_app.
