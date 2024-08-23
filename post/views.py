from django.shortcuts import render , redirect
from .models import Post
from .Forms import postform
# Create your views here.

def post_list(request):
    objects = Post.objects.all()
    return render(request,'posts.html',{'posts':objects})




def post_detail(request,id):
    object = Post.objects.get(id=id)
    return render(request , 'post_detail.html',{'post':object})






def new_post(request):
    if request.method == 'POST':
        form = postform(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.auth = request.user
            myform.save()
            return redirect("/blog/")

    else:
        form = postform()
    return render(request,'new.html',{'form':form})




def edit_post(request,id):
    object = Post.objects.get(id=id)
    if request.method == 'POST':
        form = postform(request.POST,request.FILES,instance=object)
        if form.is_valid():
            form.save()
            return redirect(F'/blog/{object.id}')

    else:
        form = postform(instance=object)
        return render(request,'edit.html',{'form':form})
    




def delete_post(requset,id):    
    object = Post.objects.get(id=id)
    object.delete()
    return redirect("/blog/")
