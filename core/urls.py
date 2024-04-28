from django.urls import path
from . import views
from diseasePrediction import views as v

urlpatterns = [
	path('', views.home, name='home'),
	path('Disease-Predictor',v.diagnosis,name='diagnosis'),
	path('BMI-Calculator', views.bmi, name='bmi'),
	#path('Daily-Calories-Requirement', views.calorie, name='calorie'),
	path('Workout-Plans', views.home, name='plans'),
	path('Blog', views.blog, name='blog'),
	path('Reviews', views.reviews, name='review'),
	path('Home', views.home, name='home'),
	path('Daily-Calories-Requirement/', views.calorie, name='home'),
	path('', views.home, name='home'),
	path('', views.home, name='home'),
]