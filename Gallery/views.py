from django.shortcuts import render, get_object_or_404
from .models import Post, Img_Files
import cv2

def gallery_posts(request):
    All_Posts = Post.objects.all()
    return render(request, 'index.html', {'Posts': All_Posts})

def view_album(request, pk):
    album = get_object_or_404(Post, pk=pk)

    Images = get_image_path(album)
    slide_images(Images)

    return render(request, 'album.html', {'album':album} )

def get_image_path(post):
    Images = []

    for img in post.posted_imgs.all():
        path =(f"Gallery{img.img.url}")
        # print(path)
        
        Images.append(cv2.imread(path))
 
    return Images

def slide_images(images):
    for img in images:
        try:
            # print(img) 
            cv2.imshow('Image', img)
            cv2.waitKey(0)
        except Exception as e:
            print(f'Erro: {e}')
        
    cv2.destroyAllWindows()