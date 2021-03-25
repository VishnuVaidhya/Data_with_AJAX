from django.urls import path
from . views import Register, Login_View, Home, Logout_view, Student_Add, Student_alldata

urlpatterns = [
    path('', Home, name="home"),
    path('register/', Register, name="register"),
    path('login/', Login_View, name="login"),
    path('logout/', Logout_view, name="logout"),
    path('student-add/', Student_Add, name='student_add'),
    path('students/list/', Student_alldata, name="students_list"),
]