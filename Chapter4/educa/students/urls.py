from django.urls import path
from . import views

# Create your url patterns here.

urlpatterns = [
    path('register/', views.StudentRegistrationView.as_view(),
         name='student_registration'),
    path('enroll-course/', views.StudentEnrollCourseView.as_view(),
         name='student_enroll_course'),
    path('cources/', views.StudentCourseListView.as_view(),
         name='student_course_list'),
    path('cources/<pk>', views.StudentCourseDetailView.as_view(),
         name='student_course_detail'),
    path('cources/<pk>/<module_id>/', views.StudentCourseDetailView.as_view(),
         name='student_course_detail_module'),

]
