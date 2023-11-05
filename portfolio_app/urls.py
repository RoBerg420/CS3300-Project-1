from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('students/', views.StudentListView.as_view(), name= 'students'),
        path('students/<int:pk>', views.StudentDetailView.as_view(), name= 'student-detail'),
        
        path('portfolios/', views.PortfolioListView.as_view(), name= 'portfolios'),
        path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name= 'portfolio-detail'),

        path('projects/', views.ProjectListView.as_view(), name= 'projects'),
        path('project/<int:pk>', views.ProjectDetailView.as_view(), name= 'project-detail'),

        path('portfolio/<int:pk>/create_project', views.CreateProjectView.as_view(), name='project-form'),
        path('portfolio/<int:pk>/update', views.update_portfolio, name='update-portfolio'),
        
        path('project/<int:pk>/delete', views.delete_project, name='delete-project'),
        path('project/<int:pk>/update', views.update_project, name='update-project'),
]
