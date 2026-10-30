from django.shortcuts import render
from django.http import HttpResponse
from .models import Countries, Locations, Employees, Jobs, Dependents
from django.db.models import Count
# Create your views here.
def index_page(request):
    return render(request, "index.html")

def get_max_salary_employees(request, top):
    queryset = Employees.objects.all().order_by('-salary')[:top]
    return render(request, "max_salary.html", {"max_salary": queryset})


def get_dependents(request, employee_id):
    queryset = Dependents.objects.all().filter(employee=employee_id)
    employee = Employees.objects.get(employee_id=employee_id)
    context = {"deps": queryset, "employee": employee}
    return render(request, "dependents.html", context)


# def orm_list(request):
#     queryset = Employees.objects.values("job").annotate(работники=Count("*"))
#     # countries = Countries.objects.values("region_id").annotate(n=Count("region_id"))
#     # print(countries.query)
#     for i in queryset:
#         print(i)
#     return HttpResponse(queryset)
#
