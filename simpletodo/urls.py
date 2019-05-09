#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path,include
from simpletodo import views

urlpatterns = [
path(r'',views.todolist),
path(r'addtodo/', views.addtodo,name='add'),
path(r'todofinish/<int:id>', views.todofinish,name='finish'),
path(r'todobackout/<int:id>', views.todoback,name='backout'),
path(r'updatetodo/<int:id>', views.updatetodo,name='update'),
path(r'tododelete/<int:id>', views.tododelete,name='delete')
]
