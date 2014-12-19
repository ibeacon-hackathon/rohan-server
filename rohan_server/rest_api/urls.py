from django.conf.urls import patterns, url

# from rest_api import views
import views

urlpatterns = patterns('',
	# # url(r'^register$', views.register,
 # #        name='register'),
	url(r'^login$', views.login1,
        name='login'),

	# url(r'^login$', views.login_s,
 #        name='login'),

	
	url(r'^task/accept$', views.task_accept_s,
        name='task_accept'),
	url(r'^task/reject$', views.task_rejet_S,
        name='task_rejet'),
	url(r'^task/finish$', views.task_finish_s,
        name='task_finish'),
	url(r'^task/validate$', views.task_validate_S,
        name='task_validate'),
	url(r'^task/new$', views.task_new_S,
        name='task_new'),
	url(r'^task/list$', views.task_list_S,
        name='task_list'),

	# url(r'^task/accept$', views.task_accept,
     #    name='task_accept'),
	# url(r'^task/reject$', views.task_rejet,
     #    name='task_rejet'),
	# url(r'^task/finish$', views.task_finish,
     #    name='task_finish'),
	# url(r'^task/validate$', views.task_validate,
     #    name='task_validate'),
	# url(r'^task/new$', views.task_new,
     #    name='task_new'),
	#
	# url(r'^task/$', views_read.task,
     #    name='get_task'),
	# url(r'^list/$', views_read.list,
     #    name='get_list'),
	
	)