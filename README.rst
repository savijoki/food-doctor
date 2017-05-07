===========
Food doctor
===========

This project is done as an course project for Ohjelmallinen Sisällönhallinta (MAT-81000) held in TUT spring 2017. The project is done using Django as web framework and materialize for frontend styles.

The application uses `Spoonacular's food API <https://spoonacular.com/food-api>`_.

Idea
====

The idea behind this project is to provide a simple service that offers information about recipes and nutrients in the ingredients. The scope in the project isn't set so it might still change during implementation. The aim is also to visualize also the data retrieved from the API by using for example d3js or c3js.

Features
========

* Users can search for recipes
* Recipes can be observed in more detail, including cooking instructions, ingredients, nutritions...
* Data-visualization with c3js -library
* Users can comment on recipes
* Users can save their favourite recipes

Configuration
=============

The application .secrets -file contains secret keys that needs to be updated when starting to use this application.
These include 
    
    * Django secret key
    * Postgresql database name
    * Postgresql user
    * Postgresql database password
    * Github key
    * Github secret
    * API url root
    * API image url root
    * Foods API key

Installation
============

You can install the required packages for the application using virtualenv from `requirements.txt` -file.

.. code-block:: bash

   $ source venv/bin/activate
   $ pip install -r requirements.txt

After the packages have been installed, you have to create postgresql user and a database that the user owns. Update `.secrets`-file accordingly.

Then you can proceed to creating the migrations for the project. This can be achieved by:

.. code-block:: bash

   $ ./manage.py makemigrations food
   $ ./manage.py migrate

After these server can be started with:

.. code-block:: bash

   $ ./manage.py runserver

Server can be accessed in `localhost:8000 <http://localhost:8000>`_.

