from django.shortcuts import render, HttpResponse
import random
from posts.models import Post
from posts.forms import PostForm, PostForm2, PostBaseForm, PostModelForm

def test_view(request):
    return HttpResponse(f'hello, this is a test view, {random.randint(1, 100)}')

def homepage_view(request):
    if request.method == "GET":
        return render(request, 'base.html')

def posts_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, "posts/posts_list.html", context={"posts": posts})    

def post_detail_view(request, post_id):
    if request.method == "GET":
        try:
            post = Post.objects.get(id=post_id)
        except:
            return HttpResponse("Post not found")
        return render(request, "posts/post_detail.html", context={"post": post})
    
def post_create_view(request):
    if request.method == "GET":
        form = PostForm2()
        return render(request, "posts/post_create.html", context={"form": form})
    if request.method == "POST":
        form = PostForm2(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get("title")    # исправлено
            content = form.cleaned_data.get("content")
            image = form.cleaned_data.get("image")
            Post.objects.create(
                image=image,
                title=title,
                content=content
            )
            return HttpResponse("Post created")

        else:
            return render(request, "posts/post_create.html", context={"form": form})

        # data = request.POST
        # files = request.FILES
        # image = files.get("image")
        # title_data = data.get("title")
        # continue_data = data.get("content")
        # post = Post.objects.create(image=image, title=title_data, content=continue_data)

        # return HttpResponse("Post request received")
  
    # elif request.method == "POST":
    #     title = request.POST.get("title")
    #     content = request.POST.get("content")
    #     image = request.FILES.get("image")
    #     post = Post.objects.create(title=title, content=content, image=image)
    #     return HttpResponse(f"Post created with id: {post.id}")

def post_create_forms_form(request):
    if request.method == "GET":
        form = PostBaseForm() 
        return render(request, "posts/post_create_forms.html", {"form": form})
    
    elif request.method == "POST":
        form = PostBaseForm(request.POST, request.FILES) 
        if form.is_valid():
        
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            image = form.cleaned_data.get('image') 
            Post.objects.create(title=title, content=content, image=image)
            return HttpResponse("Пост успешно создан с помощью forms.Form!")
        
        else:
        
            return render(request, "posts/post_create_forms.html", {"form": form})
        
def post_create_model_form(request):
    if request.method == "GET":
        form = PostModelForm() # Создаем пустую форму, привязанную к модели
        return render(request, "posts/post_create_model_form.html", {"form": form})
    
    elif request.method == "POST":
        form = PostModelForm(request.POST, request.FILES) # Передаем данные из запроса и файлы
        if form.is_valid():
            # Для ModelForm достаточно просто вызвать save()
            # Это создаст и сохранит новый объект Post в базе данных
            form.save() 
            return HttpResponse("Пост успешно создан с помощью ModelForm!")
            # return redirect('posts_list')
        else:
            # Форма невалидна, отображаем ее снова с ошибками
            return render(request, "posts/post_create_model_form.html", {"form": form})        
        
