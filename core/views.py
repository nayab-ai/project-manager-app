from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Count, Q
from .models import Project, Task

# ==================== DASHBOARD (WITH SEARCH) ====================
@login_required(login_url='login')
def dashboard(request):
    projects = Project.objects.filter(user=request.user)
    tasks = Task.objects.filter(project__user=request.user)
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        projects = projects.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
        tasks = tasks.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Statistics
    total_projects = projects.count()
    total_tasks = tasks.count()
    pending_tasks = tasks.filter(status='pending').count()
    in_progress_tasks = tasks.filter(status='in_progress').count()
    completed_tasks = tasks.filter(status='completed').count()
    
    # Recent projects (last 5)
    recent_projects = projects.order_by('-created_at')[:5]
    
    # Search result counts
    search_projects_count = total_projects
    search_tasks_count = total_tasks
    
    context = {
        'projects': projects,
        'total_projects': total_projects,
        'total_tasks': total_tasks,
        'pending_tasks': pending_tasks,
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks,
        'recent_projects': recent_projects,
        'search_query': search_query,
        'search_projects_count': search_projects_count,
        'search_tasks_count': search_tasks_count,
    }
    
    return render(request, 'core/dashboard.html', context)

# ==================== LOGIN ====================
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'core/login.html')

# ==================== LOGOUT ====================
def logout_page(request):
    logout(request)
    return redirect('login')

# ==================== SIGNUP ====================
def signup_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1
                )
                user.save()
                messages.success(request, 'Account created! Please login')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
    
    return render(request, 'core/signup.html')

# ==================== ADD PROJECT ====================
def add_project(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        Project.objects.create(
            name=name,
            description=description,
            user=request.user
        )
        return redirect('dashboard')
    
    return render(request, 'core/add_project.html')

# ==================== EDIT PROJECT ====================
def edit_project(request, project_id):
    project = Project.objects.get(id=project_id, user=request.user)
    
    if request.method == 'POST':
        project.name = request.POST.get('name')
        project.description = request.POST.get('description')
        project.save()
        return redirect('project_detail', project_id=project.id)
    
    return render(request, 'core/edit_project.html', {'project': project})

# ==================== DELETE PROJECT ====================
def delete_project(request, project_id):
    project = Project.objects.get(id=project_id, user=request.user)
    
    if request.method == 'POST':
        project.delete()
        return redirect('dashboard')
    
    return render(request, 'core/delete_project.html', {'project': project})

# ==================== PROJECT DETAIL ====================
def project_detail(request, project_id):
    project = Project.objects.get(id=project_id, user=request.user)
    tasks = project.tasks.all()
    return render(request, 'core/project_detail.html', {
        'project': project,
        'tasks': tasks
    })

# ==================== ADD TASK ====================
def add_task(request, project_id):
    project = Project.objects.get(id=project_id, user=request.user)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        
        Task.objects.create(
            title=title,
            description=description,
            status=status,
            project=project
        )
        return redirect('project_detail', project_id=project_id)
    
    return render(request, 'core/add_task.html', {'project': project})

# ==================== UPDATE TASK STATUS ====================
def update_task_status(request, task_id):
    task = Task.objects.get(id=task_id, project__user=request.user)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        task.status = new_status
        task.save()
        return redirect('project_detail', project_id=task.project.id)
    
    return render(request, 'core/update_task.html', {'task': task})

# ==================== DELETE TASK ====================
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, project__user=request.user)
    project_id = task.project.id
    
    if request.method == 'POST':
        task.delete()
        return redirect('project_detail', project_id=project_id)
    
    return render(request, 'core/delete_task.html', {'task': task})
