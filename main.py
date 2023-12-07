import cv2

# img = cv2.imread("assets/img1.jpg", -1)
# img = cv2.resize(img, (700, 600))

# cv2.imshow("Image", img)

# cv2.waitKey(0)
# cv2.destroyALLWindows()

img_path = ["assets/img1.jpg", "assets/img2.jpg", "assets/img3.jpg"]

def resize_img(img):
    img = cv2.resize(img, (700, 600))
    return img

def get_images(arq_img):
    img = cv2.imread(arq_img)
    img = resize_img(img)
    return img

def show_img(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)

def slide_show(Slide):
    for img in Slide:
        show_img(Slide.pop())
        

def main():
    Slide = []

    for path in img_path:
        img = get_images(path)
        Slide.append(img)

    # cv2.destroyALLwindows()
    slide_show(Slide)

main()