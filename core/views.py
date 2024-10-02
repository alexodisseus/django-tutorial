from django.shortcuts import render , redirect , get_object_or_404



from core.models import Todo


from core.forms import FormTodo

def list(request):
	todo_tasks = Todo.objects.all()
	
	print(todo_tasks)

	return render(request , 'core/list.html', context = {'todo_tasks': todo_tasks})

def create(request):
	if request.method == "POST":
		form = FormTodo(request.POST)
		
		if form.is_valid():

			object = form.save()
			return redirect( 'list')
		return render(request , 'core/create.html', context = {'form': form})
	
	form = FormTodo()
	return render(request , 'core/create.html', context = {'form': form})

def details(request , id):
	object = get_object_or_404(Todo , id= id)
	return render(request , 'core/details.html', context = {'object': object})

def delete(request , id):
	
	object = get_object_or_404(Todo , id= id)
	object.delete()
	return redirect( 'list')
	

def update(request , id):
	instance = get_object_or_404(Todo, id=id)
	if request.method == "POST":
		form = FormTodo(request.POST , instance = instance)
		
		if form.is_valid():

			object = form.save()
			return redirect( 'list')
		return render(request , 'core/create.html', context = {'form': form})
	
	form = FormTodo(instance = instance)
	return render(request , 'core/create.html', context = {'form': form})
