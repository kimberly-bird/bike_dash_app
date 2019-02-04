# Welcome to Bike Dash

This web application is for the Bike Dash web site. It is powered by Python and Django.

My dad buys bikes from pawn shops in Salt Lake City, Utah and then he rebuilds/upgrades the bikes to sell online. I asked him how he tracks his inventory and his sales and his response was, "I start with money in an envelope, and I hope that I end up with more money in the envelope at the end of the year than what I started with". That's when I decided to build him this app.

The following features are part of Bike Dash:

1. User registration 
1. User login 
1. User logout 
1. Bikes: add, edit, list
1. Brands: add, edit, list 
1. Bike models: add, edit, list
1. Parts: add, edit, list
1. Labor: add, list

## To Clone

1. Create a directory
1. `cd` into that directory
1. Clone the repository
1. Start a virtual environment
1. run `pip install django`
1. run `pip install safedelete`
1. run `pip install crispy_forms`
1. Create migrations `python manage.py makemigrations bikes`
1. Apply migrations to db `python manage.py migrate`


