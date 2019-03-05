from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Sum, F, Q

from pygal.style import DefaultStyle
from pygal.style import Style

from bikes.models import Bike
from bikes.models import Labor
from bikes.models import Part
from bikes.charts import BikesInventoryPieChart
from bikes.charts import BikesTotalSalesPieChart
from bikes.charts import LaborThisYearLineChart
from bikes.charts import BikesTotalSalesThisYearAndLastBarChart


class BikeChartView(TemplateView):
    template_name = './dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super(BikeChartView, self).get_context_data(**kwargs)
        current_user = self.request.user

        custom_style = Style(
            foreground='#00000',
            font_family='googlefont:PT Sans', 
            label_font_size=20,
            major_label_font_size=25,
            title_font_size=40,
            legend_font_size=20,
            tooltip_font_size=30,
           )

        cht_bikes = BikesInventoryPieChart(
            style=custom_style
        )

        total_bikes = BikesTotalSalesPieChart(
            style=custom_style
        )

        total_labor = LaborThisYearLineChart(
            style=custom_style
        )

        sales_this_year_vs = BikesTotalSalesThisYearAndLastBarChart(
            style=custom_style
        )

        # count the number of sold bikes by logged in user
        sold_bikes = Bike.objects.filter(status_id=1, user_id=current_user, sale_date__icontains='2019').count()

        total_sales = Bike.objects.filter(status_id=1, user_id=current_user, sale_date__icontains='2019').aggregate(sum=Sum(F('sale_price')-F('purchase_price')))

        sold_bikes_labor_2019 = Bike.objects.filter(status_id=1, user_id=current_user, sale_date__icontains='2019')

        total_labor_2019 = 0
        # loop over bikes that were sold in 2019
        for bike in sold_bikes_labor_2019:
            # for each bike, get the total labor reports
            labor_calculation = bike.get_total_profit
            total_labor_2019 += labor_calculation
        # get total profit by subtracting labor costs from total sales
        profit_2019 = total_sales.get('sum') - total_labor_2019
        
        # calculate rate of pay*time for each labor instance - returns an int ($)
        labor_2019 = Labor.objects.filter(user_id=current_user, date__icontains='2019').aggregate(sum=Sum(F('time')*F('rate_of_pay')))

        # get the total amount of time spent on labor in 2019 - returns an int (hours)
        labor_hours_2019 = Labor.objects.filter(user_id=current_user, date__icontains='2019').aggregate(sum=Sum('time'))

        # total # of bikes in inventory that are not sold
        bike_inventory = Bike.objects.filter(Q(user_id=current_user), Q(status_id=2) | Q(status_id=3)).count()

        # total # of parts that are not installed on a bike
        part_inventory = Part.objects.filter(user_id=current_user, bike_id=None, deleted=None).count()
        print("# of parts", part_inventory)


        context['parts_in_inventory'] = part_inventory
        context['bikes_in_inventory'] = bike_inventory
        context['labor_hours_2019'] = labor_hours_2019['sum']
        context['labor_2019'] = labor_2019['sum']
        context['sales_this_year_vs'] = sales_this_year_vs.generate()
        context['total_sales'] = profit_2019
        context['sold_bikes'] = sold_bikes
        # Call the `.generate()` method on chart object
        # and pass it to template context.
        context['cht_bikes'] = cht_bikes.generate()
        context['total_bikes'] = total_bikes.generate()
        context['total_labor'] = total_labor.generate()
        return context