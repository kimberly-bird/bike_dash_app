from django.db.models import Count
from django.db.models import Sum

import pygal

from bikes.models import Bike
from bikes.models import Labor


class BikesInventoryPieChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Pie(**kwargs)
        self.chart.title = 'Bikes by Status'

    def get_data(self):
        '''
        Query the db for chart data, pack them into a dict and return it.

        '''

        # I don't like this solution, but it works. Groups bikes by status and sends dictionary to generate the chart
        sold_bikes = len(Bike.objects.filter(status_id=1))
        listed_bikes = len(Bike.objects.filter(status_id=2))
        in_process_bikes = len(Bike.objects.filter(status_id=3))

        data = {
            "Sold": sold_bikes,
            "Listed": listed_bikes,
            "In Process": in_process_bikes
        }

        return data

    def generate(self):
        # Get chart data
        chart_data = self.get_data()

        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        # Return the rendered SVG
        return self.chart.render(is_unicode=True)

class BikesTotalSalesPieChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Bar(**kwargs)
        self.chart.title = 'Sold Bikes by Date'
        self.chart.x_labels = ''

    def get_data(self):
        '''get the total number of bikes marked as sold, grouped by date sold

        '''

        # get bikes that have a status of "sold" (id=1) and count the bikes sold, grouped by sale date
        total_sold = Bike.objects.values('sale_date').annotate(count=Count('status_id')).filter(status_id=1)

        data = {}

        # loop over all bikes that are sold and add them to data dictionary with sale date as key and the count of bikes grouped by that date as the value
        for bike in total_sold:
            data[bike["sale_date"]] = bike["count"]
        
        return data

    def generate(self):
        
        # Get chart data
        chart_data = self.get_data()

        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        # Return the rendered SVG
        return self.chart.render(is_unicode=True)


class LaborThisYearLineChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Line(include_x_axis=True, **kwargs)
        self.chart.title = 'Labor This Year'

    def generate(self):
        '''get the total number of bikes marked as sold, grouped by date sold

        '''
        # get all recorded labor
        total_labor = Labor.objects.values('date').annotate(count=Sum('time'))

        labor_time = []
        labor_dates = []
        # loop over total labor queryset and add the total time spent per day and date of labor to respsective sets
        for count in total_labor:
            labor_time.append(count['count'])
            labor_dates.append(count['date'])
        
        # set the x axis to the dates of the labor
        self.chart.x_labels = labor_dates

        # add the data to the chart
        self.chart.add('Hours', labor_time)

        # Return the rendered SVG
        return self.chart.render(is_unicode=True)
