from django.views.generic import ListView, UpdateView
from django.db.models import Sum, Count
from django.db.models.functions import ExtractYear, ExtractMonth
from .forms import ExpenseSearchForm, CategoryForm
from .models import Expense, Category
from .reports import summary_per_category, summary_year_month
from django.urls import reverse_lazy


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5
    form_class = ExpenseSearchForm

    def get_queryset(self):
        queryset = super().get_queryset()
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        sort_by = self.request.GET.get('sort_by', 'date')
        sort_order = self.request.GET.get('sort_order', 'desc')

        if date_from:
            queryset = queryset.filter(date__gte=date_from)
        if date_to:
            queryset = queryset.filter(date__lte=date_to)

        # retrieves a list of selected category IDs
        categories = self.request.GET.getlist('categories')
        if categories:
            queryset = queryset.filter(category__in=categories)

        # sort parameters in the request
        if sort_by in ['category', 'date']:
            if sort_order == 'desc':
                sort_by = f'-{sort_by}'
            queryset = queryset.order_by(sort_by)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            context['form'] = form
            if name:
                queryset = queryset.filter(name__icontains=name)
                context['object_list'] = queryset

        # total amount spent
        total_amount = queryset.aggregate(total=Sum('amount'))['total']
        context['total_amount'] = total_amount

        context['summary_per_category'] = summary_per_category(queryset)

        # table with the total summary per year-month
        context['expenses_per_year_month'] = summary_year_month(queryset)

        return context

class CategoryListView(ListView):
    model = Category
    paginate_by = 5

    # adding a 'number of expenses' in table
    def get_queryset(self):
        return Category.objects.annotate(expense_count=Count('expense')).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# update button in 'Categories'
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'generic_update.html'
    success_url = reverse_lazy('expenses:category-list')