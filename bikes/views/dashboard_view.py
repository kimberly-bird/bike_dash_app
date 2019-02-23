from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Sum, F

from pygal.style import DefaultStyle

from bikes.models import Bike
from bikes.models import Labor
from bikes.charts import BikesInventoryPieChart
from bikes.charts import BikesTotalSalesPieChart
from bikes.charts import LaborThisYearLineChart
from bikes.charts import BikesTotalSalesThisYearAndLastBarChart


class BikeChartView(TemplateView):
    template_name = './dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super(BikeChartView, self).get_context_data(**kwargs)
        current_user = self.request.user

        # Instantiate our chart. We'll keep the size/style/etc.
        # config here in the view instead of `charts.py`.
        cht_bikes = BikesInventoryPieChart(
            height=400,
            width=500,
            explicit_size=True,
            style=DefaultStyle
        )

        total_bikes = BikesTotalSalesPieChart(
            height=400,
            width=500,
            explicit_size=True,
            style=DefaultStyle
        )

        total_labor = LaborThisYearLineChart(
            height=400,
            width=500,
            explicit_size=True,
            style=DefaultStyle
        )

        sales_this_year_vs = BikesTotalSalesThisYearAndLastBarChart(
            height=400,
            width=500,
            explicit_size=True,
            style=DefaultStyle
        )

        # count the number of sold bikes by logged in user
        sold_bikes = Bike.objects.filter(status_id=1, user_id=current_user, sale_date__icontains='2019').count()

        total_sales = Bike.objects.filter(status_id=1, user_id=current_user, sale_date__icontains='2019').aggregate(sum=Sum(F('sale_price')+F('purchase_price')))

        labor_2019 = Labor.objects.filter(user_id=current_user, date__icontains='2019').aggregate(sum=Sum(F('time')*F('rate_of_pay')))
        labor_hours_2019 = Labor.objects.filter(user_id=current_user, date__icontains='2019').aggregate(sum=Sum('time'))

        print("labor", labor_hours_2019)

        context['labor_hours_2019'] = labor_hours_2019['sum']
        context['labor_2019'] = labor_2019['sum']
        context['sales_this_year_vs'] = sales_this_year_vs.generate()
        context['total_sales'] = total_sales['sum']
        context['sold_bikes'] = sold_bikes
        # Call the `.generate()` method on chart object
        # and pass it to template context.
        context['cht_bikes'] = cht_bikes.generate()
        context['total_bikes'] = total_bikes.generate()
        context['total_labor'] = total_labor.generate()
        return context