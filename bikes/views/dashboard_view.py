from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Sum, F

from pygal.style import DefaultStyle

from bikes.models import Bike
from bikes.charts import BikesInventoryPieChart
from bikes.charts import BikesTotalSalesPieChart
from bikes.charts import LaborThisYearLineChart


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

        # count the number of sold bikes by logged in user
        sold_bikes = Bike.objects.filter(status_id=1, user_id=current_user).count()

        sql = """select sum(sales) as "totalsales"
                    from (
                    select b.name, b.status_id, sum(b.sale_price - b.purchase_price) as "sales"
                    from bikes_bike b
                    where b.status_id = 1
                    and b.user_id = {current_user}
                    group by b.name
                    );
        """

        total_sales = Bike.objects.filter(status_id=1, user_id=current_user).aggregate(sum=Sum(F('sale_price')+F('purchase_price')))

        print("total sales", total_sales['sum'])

        context['total_sales'] = total_sales['sum']
        context['sold_bikes'] = sold_bikes
        # Call the `.generate()` method on chart object
        # and pass it to template context.
        context['cht_bikes'] = cht_bikes.generate()
        context['total_bikes'] = total_bikes.generate()
        context['total_labor'] = total_labor.generate()
        return context