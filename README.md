app-structure-example
=============

A basic Flask microblogging app to demonstrate an organized and isolated project structure.

## Structure

```
.
├── Makefile
├── README.md
├── app
│   ├── __init__.py
│   ├── forms
│   │   ├── __init__.py
│   │   └── post_form.py
│   ├── journal.db
│   ├── models
│   │   ├── __init__.py
│   │   └── post.py
│   ├── services
│   │   ├── __init__.py
│   │   └── posts.py
│   ├── static
│   │   ├── css
│   │   ├── fonts
│   │   └── js
│   ├── templates
│   │   ├── index.html
│   │   └── layout.html
│   └── views
│       ├── __init__.py
│       └── index.py
├── create_db.py
├── requirements.txt
└── run.py
```

## Packages

Each package in the `app` package is isolated by dependency. The `services` package is the only one that should be importing from the `models` package. In more complex apps this reduces the chances of circular imports.

## `forms`

 - Forms go here. 
 - Each form should be in it's own module (file) and should be imported in the package `__init__.py`

## `models`

 - Models go here. 
 - Each model should be in it's own module (file) and should be imported in the package `__init__.py`
 - Don't import models directly in other packages. Use a service module.
 
 ## `services`

 - Modules for interacting with your apps various dependencies. 
 - Each service should be in it's own module (file) and should be imported in the package `__init__.py`
 - Modules here should bring together all the other packages. This help reduce the chances of import errors.

## `views`

 - Views go here. 
 - Each view should be in it's own module (file) and should be imported in the package `__init__.py`
 - Prefer [class based views](https://flask.palletsprojects.com/en/1.1.x/views/) over function based views
