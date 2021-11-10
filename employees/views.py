
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, FormView, DetailView, CreateView, UpdateView
from .models import EmployeeModel
from .form import EmployeesFormForIdForm, EmployeesFormForNameForm, EmployeeForm


# class EmployeesView(ListView, FormView):
#     model = EmployeeModel
#     template_name = 'employees/main.html'
#     form_class = EmployeesFormForIdForm
#     success_url = 'employees/cool'
#
#     def form_valid(self, form):
#         return HttpResponseRedirect(self.get_success_url())
def employees_view(request):
    if request.method == 'POST':
        if 'search_by_id' in request.POST:
            form_for_id = EmployeesFormForIdForm(request.POST)
            form_for_name = EmployeesFormForNameForm
            object_list = EmployeeModel.objects.filter(id = request.POST['id'])
            return render(request, 'employees/main.html', {'object_list': object_list, 'form_for_id': form_for_id, 'form_for_name': form_for_name})

        if 'search_by_name' in request.POST:
            form_for_id = EmployeesFormForIdForm
            form_for_name = EmployeesFormForNameForm(request.POST)
            object_list = EmployeeModel.objects.filter(name = request.POST['name'])
            return render(request, 'employees/main.html', {'object_list': object_list, 'form_for_id': form_for_id, 'form_for_name': form_for_name})

    else:
        object_list = EmployeeModel.objects.all()
        form_for_id = EmployeesFormForIdForm
        form_for_name = EmployeesFormForNameForm
        return render(request, 'employees/main.html',
                      {'object_list': object_list, 'form_for_id': form_for_id, 'form_for_name': form_for_name})


class DeleteEmployeeView(DeleteView):
    model = EmployeeModel
    template_name = 'employees/del.html'
    success_url = reverse_lazy('main')

class CreateEmployeeView(CreateView):
    template_name = 'employees/new.html'
    model = EmployeeModel
    form_class = EmployeeForm


class UpdateEmployeeView(UpdateView):
    template_name = 'employees/edit.html'
    model = EmployeeModel
    form_class = EmployeeForm






