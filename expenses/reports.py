from collections import OrderedDict
from django.db.models import Sum, Value
from django.db.models.functions import Coalesce
from django.db.models.functions import ExtractYear, ExtractMonth


def summary_per_category(queryset):
    return OrderedDict(sorted(
        queryset
        .annotate(category_name=Coalesce('category__name', Value('-')))
        .order_by()
        .values('category_name')
        .annotate(s=Sum('amount'))
        .values_list('category_name', 's')
    ))

def summary_year_month(queryset):
    return queryset \
        .annotate(year=ExtractYear('date'), month=ExtractMonth('date')) \
        .values('year', 'month') \
        .annotate(monthly_total=Sum('amount')) \
        .order_by('-year', '-month')

