from django.shortcuts import render , redirect
from .models import Post , Comment
from .Forms import postform , CommentForm
# Create your views here.

def post_list(request):
    objects = Post.objects.all()
    return render(request,'posts.html',{'posts':objects})




def post_detail(request,id):
    post = Post.objects.get(id=id)
    object = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.user = request.user
            my_form.post = post
            my_form.save()
            return redirect(f'/blog/{post.id}')

    else:
        form = CommentForm()
    return render(request , 'post_detail.html',{'post':post,'comments':object,'form':form})






def new_post(request):
    if request.method == 'POST':
        form = postform(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.auth = request.user
            myform.save()
            return redirect("/blog/")
        else:
            return render(request, 'new.html', {'form': form})

    else:
        form = postform()
    return render(request,'new.html',{'form':form})




def edit_post(request,id):
    object = Post.objects.get(id=id)
    if request.method == 'POST':
        form = postform(request.POST,request.FILES,instance=object)
        if form.is_valid():
            form.save()
            return redirect(f'/blog/{object.id}')

    else:
        form = postform(instance=object)
        return render(request,'edit.html',{'form':form})
    




def delete_post(requset,id):    
    object = Post.objects.get(id=id)
    object.delete()
    return redirect("/blog/")



# ________________________________________________________



