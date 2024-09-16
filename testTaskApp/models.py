from django.db import models
from django.utils import timezone

class Employee(models.Model):
    full_name = models.CharField(max_length=255)  # ФИО
    position = models.CharField(max_length=100)   # Должность

    def __str__(self):
        return self.full_name
    
class Project(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активен'),
        ('inactive', 'Неактивен'),
    ]
    
    title = models.CharField(max_length=200)  # Название проекта
    description = models.TextField()          # Описание проекта
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')  # Статус проекта
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='managed_projects')  # Руководитель проекта

    def __str__(self):
        return self.title
    
class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('closed', 'Закрыта'),
    ]

    title = models.CharField(max_length=200)  # Название задачи
    due_date = models.DateField()             # Срок исполнения
    description = models.TextField()          # Описание задачи
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='new')  # Статус задачи
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')  # Связь с проектом
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='tasks')  # Исполнитель задачи

    def __str__(self):
        return self.title
    
class Comments(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return self.text
    
class PrComments(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text