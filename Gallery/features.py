import cv2

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