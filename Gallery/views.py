from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Img_Files
from django.contrib import messages
from django.utils import timezone
from . import features 
import os

def gallery_posts(request):
    All_Posts = Post.objects.all()
    return render(request, 'index.html', {'Posts': All_Posts})


def view_album(request, pk):
    album = get_object_or_404(Post, pk=pk)

    # Images = features.get_image_path(album)
    # features.slide_images(Images)

    return render(request, 'album.html', {'album':album} )


def new_album(request, pk=''):
    if request.method == "POST":
        
        if 'update_author' in request.POST:
            post = get_object_or_404(Post, pk=pk)
        
            post.author = request.POST['update_author']
            post.title = request.POST['title']
            post.text = request.POST['text']
            
            imagens = request.FILES.getlist('imgs')
            for img in imagens:
                img_file = Img_Files.objects.create(img=img)
                post.posted_imgs.add(img_file)
            
            post.save()
            return redirect('view_album', pk=post.pk)
        
        else:
            new_post = Post.objects.create(
                author = request.POST['author'],
                title = request.POST['title'],
                text = request.POST['text'],
                created_date = timezone.now()
            )

            imagens = request.FILES.getlist('imgs')
            for img in imagens:
                img_file = Img_Files.objects.create(img=img)
                new_post.posted_imgs.add(img_file)
            
            new_post.save()
            return redirect('view_album', pk=new_post.pk)

    else:
        if pk != '':
            post = get_object_or_404(Post, pk=pk)
            return render (request, 'new_album.html', {'post':post})
        else:
            return render (request, 'new_album.html')
            
    
def remove_album(request, pk):
    album = get_object_or_404(Post, pk=pk)

    for img in album.posted_imgs.all():
        os.remove(img.img.path)


    album.posted_imgs.all().delete()
    album.delete()

    messages.success(request, 'Album Removido')

    return redirect('gallery_posts')
    
def remove_photo(request, pk):
    imgUrl = request.GET.get("imgUrl")
    album = get_object_or_404(Post, pk=pk)

    img_to_delete = album.posted_imgs.filter(img=imgUrl).first()

    if img_to_delete:
        img_to_delete.delete()
    
    album.save()

    return redirect('view_album', pk=pk)