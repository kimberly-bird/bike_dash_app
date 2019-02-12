# Welcome to Bike Dash!

This web application is for the Bike Dash website. It is powered by Python and Django.

## Background
As a hobby, my dad buys bikes from pawn shops in Salt Lake City, Utah and then he rebuilds/upgrades the bikes to sell online. I asked him how he tracks his inventory and his sales and his response was, "I start with money in an envelope, and I hope that I end up with more money in the envelope at the end of the year than what I started with". That's when I decided to build him this app.

## General app functionality 
The following features are part of Bike Dash:

1. User registration (forked from Steve and Joe - thanks! ;) )
1. User login (forked from Steve and Joe)
1. User logout (forked from Steve and Joe)
1. Bikes: add, edit, list, detail
1. Bike Brands: add, edit, list 
1. Bike models: add, edit, list
1. Parts: add, edit, list, detail
1. Labor: add, edit, list, detail

## General flow
The goal of this app is to track inventory, labor, and sales on bikes, so a typical flow would be to: 

1. Add a new bike to your inventory
1. Add new parts from your part inventory to the bike
1. Record the time spent and rate of pay for that work
1. Repeat adding parts/recording labor as you work on the bike (you can also add labor independent of a part if you're working on maintenance or an existing part)
1. Once you're ready, list the bike for sale
1. Once you've sold the bike, record the sale price and date
1. Check your dashboard to see your reporting on sales, inventory, labor, etc.

## FYI
Note about brands/models - in a perfect world, this would not be user generated data - someday I might scrape some data to populate the database with common bike brands/models. For now, users can enter in bike brand manufacturers/models to the database. These brands/models are public and are accessible by anyone using the app. I am hoping to add more functionality to this, such as checking that the brand/model isn't already in the db.

Bikes, Parts, and Labor are unique to the current user and can only be viewed by the logged in user.

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
1. run `python manage.py runserver`
1. Open up your browser and navigate to the running server
1. Register, add bikes/parts/labor, and you're on your way!


