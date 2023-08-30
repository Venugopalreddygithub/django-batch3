from django.shortcuts import redirect, render 
from django.http import HttpResponse, JsonResponse 
from todo_app.models import Todo

convert_into_boolean = {
     "0": False,
     "1": True,
}
order_to_string = {
     "0": "created_at",
     "1": "-created_at"
}



def index(request):
    search = request.GET.get("todoSearch")
    completed = request.GET.get("completed")
    order = request.GET.get("order")
    all_todos = Todo.objects.all() 
    if search != None:  
            all_todos = all_todos.filter(title__icontains = search)
    if completed != None:
         value = convert_into_boolean.get(completed)
         all_todos = Todo.objects.filter(completed=value)
    if order != None:
         value = order_to_string.get(order)
         all_todos = all_todos.order_by(value)
         
    data = {
        "todo": all_todos
    }
    return render(request, "index.html", context=data)

def add_view(request):
    if request.method == "GET":
        return HttpResponse("Invalid Method")
    else:
        todo_input = request.POST['todoInput']
        print("todo_input:", todo_input)
        Todo.objects.create(title=todo_input)
        return redirect('todo_index')

def detailed_view(request, todo_id):
    if request.method == "POST":
        return HttpResponse("Invalid Method")
    else:
        try:
            todo_object = Todo.objects.get(id=todo_id)
            print(todo_object)
            data = {
                'id': todo_object.id,
                'title': todo_object.title,
                'completed': todo_object.completed,
                'created_at': todo_object.created_at,
                'updated_at': todo_object.updated_at,
            }
            return JsonResponse(data)
        except Todo.DoesNotExist:
            return HttpResponse("Error Todo not found")
def delete_todo(request, todo_id):
        if request.method == "GET":
            return HttpResponse("Invalid Method")
        else:
            try:
                todo_object = Todo.objects.get(id=todo_id)
                todo_object.delete()
                return redirect('todo_index')
            except Todo.DoesNotExist:
                return HttpResponse("Error Todo not found")
            
def mark_view(request, todo_id):
        if request.method == "GET":
            return HttpResponse("Invalid Method")
        else:
            try:
                todo_object = Todo.objects.get(id=todo_id)
                todo_object.completed = True 
                todo_object.save()
                return redirect('todo_index')
            except Todo.DoesNotExist:
                return HttpResponse("Error Todo not found")