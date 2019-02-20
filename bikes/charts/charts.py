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
        self.chart.title = 'Number of Sold Bikes'
        self.chart.x_labels = '#'

    def get_data(self):
        '''get the total number of bikes markes as sold

        '''

        total_sold = Bike.objects.filter(status_id=1).count()

        data = {
            "Total Bikes Sold": total_sold
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
