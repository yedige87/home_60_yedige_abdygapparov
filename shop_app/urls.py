from django.urls import path

# from shop_app.views.todos import ToDoDetail, ToDoUpdateView, ToDoCreateView, ToDoDeleteView, ProjectTasksView, ProjectsView, ProjectCreateView, ProjectToDoCreateView
from shop_app.views.base import IndexView
from shop_app.views.products import Product_Detail, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    BasketAddView, BasketView, check_product, change_product, create_order, basket_delete, OrderView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', Product_Detail.as_view(), name='product_view'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/edit', ProductUpdateView.as_view(), name='product_edit'),
    path('todo/<int:pk>/confirm_delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('basket_add/<int:pk>', BasketAddView.as_view(), name='basket_add'),
    path('basket_check/<int:pk>', check_product, name='check_basket'),
    path('basket_view', BasketView.as_view(), name='basket_view'),
    path('change_product/<int:pk>', change_product, name='change_product'),
    path('basket/delete/<int:pk>', basket_delete, name='basket_delete'),
    path('create_order', create_order, name='create_order'),
    path('order_view', OrderView.as_view(), name='order_view'),
)

# path('products/add', product_add_view, name='product_add'),
#
# path('product/<int:pk>/delete', product_delete_view, name='product_delete'),
# path('product/delete/<int:pk>', confirm_delete, name='confirm_delete'),
# path('products/<str:cat_id>', category_view, name='category_view'),











# path('todo/add/', ToDoCreateView.as_view(), name='todo_add'),
# path('todo/<int:pk>', ToDoDetail.as_view(), name='todo_detail'),
# path('todo/<int:pk>/update/', ToDoUpdateView.as_view(), name='todo_update'),
# path('todo/<int:pk>/delete/', ToDoDeleteView.as_view(), name='todo_delete'),
# path('todo/<int:pk>/confirm_delete/', ToDoDeleteView.as_view(), name='confirm_delete'),
# path('project/<int:project_id>', ProjectTasksView.as_view(), name='project_detail'),
# path('projects/', ProjectsView.as_view(), name='projects_view'),
# path('project/add', ProjectCreateView.as_view(), name='project_add'),
# path('project/add/<int:pk>', ProjectToDoCreateView.as_view(), name='todo_project_add'),