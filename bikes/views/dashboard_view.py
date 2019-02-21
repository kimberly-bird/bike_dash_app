from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView

from pygal.style import DefaultStyle

from bikes.models import Bike
from bikes.charts import BikesInventoryPieChart
from bikes.charts import BikesTotalSalesPieChart
from bikes.charts import LaborThisYearLineChart


class BikeChartView(TemplateView):
    template_name = './dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super(BikeChartView, self).get_context_data(**kwargs)

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

        # Call the `.generate()` method on our chart object
        # and pass it to template context.
        context['cht_bikes'] = cht_bikes.generate()
        context['total_bikes'] = total_bikes.generate()
        context['total_labor'] = total_labor.generate()
        return context