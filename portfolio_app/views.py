from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views import generic
from .models import Student
from django.urls import reverse_lazy
from .models import Portfolio
from .models import Project
from .forms import ProjectForm, PortfolioForm

# Create your views here.
def index(request):
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})

def delete_project(request, pk):
    proj = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        portfolio = proj.portfolio.id
        proj.delete()
        messages.success(request, "Deleted!")
        return redirect('portfolio-detail', pk=portfolio)

    return render(request, 'portfolio_app/confirm_delete.html', {'proj':proj})

def update_project(request, pk):
    proj = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=proj)
        form.save()
        return redirect('project-detail', pk=pk)
    else:
        form = ProjectForm(instance=proj)
    return render(request, "portfolio_app/project_form.html", {'form': form})

def update_portfolio(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)

    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        form.save()
        return redirect('portfolio-detail', pk=pk)
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, "portfolio_app/project_form.html", {'form': form})



class StudentListView(generic.ListView):
    model = Student

class StudentDetailView(generic.DetailView):
    model = Student

class PortfolioListView(generic.ListView):
    model = Portfolio

class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    def get_context_data(self, **kwargs):
        projects = Project.objects.all()
        student_portfolio_projects = []
        for project in projects:
            if project.portfolio.id == self.object.id:
                student_portfolio_projects.append(project)
        context = super(PortfolioDetailView, self).get_context_data( **kwargs)
        context["student_portfolio_projects"] = student_portfolio_projects
        return context 
    
    def get_context_data2(self, **kwargs):
        students = Student.objects.all()
        student_portfolio = []
        for student in students:
            if student.portfolio.id == self.object.id:
                student_portfolio.append(student)
        context = super(PortfolioDetailView, self).get_context_data( **kwargs)
        context["student_portfolio"] = student_portfolio

    def __str__(self):
        return self.id

class UpdateProjectView(generic.edit.FormView):
    template_name = "portfolio_app/project_form.html"
    form_class = ProjectForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CreateProjectView(generic.edit.FormView):
    template_name = "portfolio_app/project_form.html"
    form_class = ProjectForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProjectListView(generic.ListView):
    model = Project

class ProjectDetailView(generic.DetailView):
    model = Project
