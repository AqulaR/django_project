from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task, Comments, PrComments
from .forms import CommentForm, PrCommentForm

def index(request):
	projects = Project.objects.all()
	return render(request, 'index.html', {'projects': projects})

def project_tasks(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = Task.objects.filter(project_id=project_id)
    comments = [[task, Comments.objects.filter(task=task)] for task in tasks]
    prComments = PrComments.objects.filter(project_id=project_id)
    
    if request.method == 'POST':
        if 'add_comment' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                task_id = form.cleaned_data['element_id']
                task = get_object_or_404(Task, id=task_id)
                comment = form.save(commit=False)
                comment.task = task
                comment.save()
                return redirect('project_tasks', project_id=project_id)
        elif 'add_Pr_com' in request.POST:
            form = PrCommentForm(request.POST)
            if form.is_valid():
                prcomment = form.save(commit=False)
                prcomment.project = project
                prcomment.save()
                return redirect('project_tasks', project_id=project_id)
    else:
        form = CommentForm()
        
    return render(request, 'project_tasks.html', {'tasks': tasks,
                                                  'project': project,
                                                  'comments': comments,
                                                  'prComments': prComments,
                                                  'form': form})