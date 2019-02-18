from django.urls import path, include
from rest_framework.routers import DefaultRouter
from budgy import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'bugets', views.BudgetViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'expenses', views.ExpenseViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),

]