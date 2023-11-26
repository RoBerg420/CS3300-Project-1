from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
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

        path('create_Account/', views.createAnAccount, name='create_Account'),

        path('login/', views.custom_login, name='login'),
        path('logout/', views.logout_view, name='logout'),
        
        path('upload/', views.upload_file, name='upload_file'),
        path('upload_success/', views.upload_success, name ="upload_success"),

        path('delete-file/<str:file_name>/', views.delete_file, name='delete_file'),
        
        path('download/<str:file_name>/', views.download_file, name='download_file'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
