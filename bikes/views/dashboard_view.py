from django.db.models import Sum, F, Q
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView

from pygal.style import DefaultStyle
from pygal.style import Style

from bikes.models import Bike
from bikes.models import Labor
from bikes.models import Part
from bikes.charts import BikesInventoryPieChart
from bikes.charts import BikesTotalSalesPieChart
from bikes.charts import BikesTotalSalesThisYearAndLastBarChart
from bikes.charts import LaborThisYearLineChart


class BikeChartView(TemplateView):
    '''This view handles all of the data sent to the dashboard template. Some of the charts are rendered using pygal and others just through data sent to the template without a chart. Pygal chart data is sent from charts.py

    The following charts/data are returned: 
    1. Bike inventory
    2. Part inventory
    3. Bikes by status (pie chart)
    4. Sold bikes 2018 vs 2019 (bar chart)
    5. 2019 total bikes sold
    6. 2019 total bike profit (sale price - (purchase_price + labor + parts))
    7. Labor this year (line graph)
    8. 2019 total labor (total labor in $ and hours)
    '''

    template_name = './dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super(BikeChartView, self).get_context_data(**kwargs)
        current_user = self.request.user

        # custom style for pygal charts
        custom_style = Style(
            foreground='#00000',
            font_family='googlefont:PT Sans', 
            label_font_size=20,
            major_label_font_size=25,
            title_font_size=40,
            legend_font_size=20,
            tooltip_font_size=30,
        )

        # ----------------------------------------------------------------------

        # 1. Bike inventory
        # total # of bikes in inventory that are not sold
        bike_inventory = Bike.objects.filter(Q(user_id=current_user), Q(status_id=2) | Q(status_id=3)).count()

        # ----------------------------------------------------------------------

        # 2. Part inventory
        # total # of parts that are not installed on a bike
        part_inventory = Part.objects.filter(user_id=current_user, bike_id=None, deleted=None).count()

        # ----------------------------------------------------------------------

        # 3. Bikes by status (pie chart)
        cht_bikes = BikesInventoryPieChart(
            style=custom_style
        )

        # ----------------------------------------------------------------------

        # 4. Sold bikes 2018 vs 2019 (bar chart)
        sales_this_year_vs = BikesTotalSalesThisYearAndLastBarChart(
            style=custom_style
        )

        # ----------------------------------------------------------------------

        # 5. 2019 total bikes sold
        # count the number of sold bikes by logged in user
        sold_bikes = Bike.objects.filter(status_id=1, user_id=current_user, sale_date__icontains='2019').count()

        # ----------------------------------------------------------------------

        # 6. 2019 total bike profit (sale price - (purchase_price + labor + parts))

        # This calculation is to get the total profit for all bikes sold in 2019. It does the following: 
        # 1. Get all sold bikes
        # 2. Get calculation for sale_price - purchase_price
        # 3. Iterate over all sold bikes and get the total parts cost and add that total to the total_parts_investment variable
        # 4. Iterate over all of the sold bikes and get the labor total for each bike and add that total to the total_labor_2019 variable
        # 5. Subtract total sales from total labor and parts cost
        
        # get all sold bikes
        sold_bikes_labor_2019 = Bike.objects.filter(status_id=1, user_id=current_user, sale_date__icontains='2019')

        # calculate sale price - purchase price
        total_sales = Bike.objects.filter(status_id=1, user_id=current_user, sale_date__icontains='2019').aggregate(sum=Sum(F('sale_price')-F('purchase_price')))

        total_labor_2019 = 0
        total_parts_investment = 0
        # loop over bikes that were sold in 2019
        for bike in sold_bikes_labor_2019:
            # for each bike, get the total cost of parts (get_part_total_on_bike is a method on the bike model)
            parts = bike.get_part_total_on_bike
            # add that amount to the variable total_parts_investment
            total_parts_investment += parts
            # for each bike, get the total labor reports (get_total_profit is a method on the bike model)
            labor_calculation = bike.get_total_profit
            # add that amount to the total_labor_2019 total
            total_labor_2019 += labor_calculation
        # get total profit by subtracting labor costs and part costs from total sales
        if total_labor_2019 != 0 or total_parts_investment != 0:
            profit_2019 = total_sales.get('sum') - total_labor_2019 - total_parts_investment
            # 6. 2019 total bike profit (sale price - (purchase_price + labor + parts))
            context['total_sales'] = profit_2019

        # ----------------------------------------------------------------------

        # 7. Labor this year (line graph)
        total_labor = LaborThisYearLineChart(
            style=custom_style
        )

        # ----------------------------------------------------------------------

        # 8. 2019 total labor (total labor in $ and hours)
        # calculate rate of pay*time for each labor instance - returns an int ($)
        labor_2019 = Labor.objects.filter(user_id=current_user, date__icontains='2019').aggregate(sum=Sum(F('time')*F('rate_of_pay')))

        # get the total amount of time spent on labor in 2019 - returns an int (hours)
        labor_hours_2019 = Labor.objects.filter(user_id=current_user, date__icontains='2019').aggregate(sum=Sum('time'))

        # CONTEXT --------------------------------------------------------------

        # 1. Bike inventory
        context['bikes_in_inventory'] = bike_inventory
        # 2. Part inventory
        context['parts_in_inventory'] = part_inventory
        # 3. Bikes by status (pie chart)
        context['cht_bikes'] = cht_bikes.generate()
        # 4. Sold bikes 2018 vs 2019 (bar chart)
        context['sales_this_year_vs'] = sales_this_year_vs.generate()
        # 5. 2019 total bikes sold
        context['sold_bikes'] = sold_bikes
        # 6. context set up in if statment above
        # 7. Labor this year (line graph)
        context['total_labor'] = total_labor.generate()
        # 8. 2019 total labor (total labor in $ and hours)
        context['labor_hours_2019'] = labor_hours_2019['sum']
        context['labor_2019'] = labor_2019['sum']

        return context