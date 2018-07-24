# pillow模块用来处理图像

## 基础

- 坐标系

> 图像的坐标系，左上角为（0,0），然后x轴向右递增;y轴向下递增。描述一个尺寸为600×800的图像的坐标系，可以使用（0,0,600,800）

- 图像尺寸（size）

> 图像尺寸由一个二元素元组表示，尺寸为600×800的图像表示为（600,800）

### Image对象

```python
# pillow 模块源自于PIL
from PIL import Image
# 打开一个Image对象
im = Image.open('flower.jpg')
# 查看图像大小
im.size
# 通过赋值获取
width,height = im.size
# 在进行操作前，可获取其一个副本对象
im_copy = im.copy()
# 剪裁图像，四元组参数分别为（x,y,x2,y2）
im_crop = im_copy.crop((200,200,400,400))
# 粘贴图像，二元组参数为（x,y）
im_copy.paste(im_crop,(100,100))
# 保存图像
im_copy.save('im_copy.jpg')
# 生成缩略图
im_thumail = im.thumnail((200,200))
# 改变图像大小
im_copy.resize((400,400))
# 翻转图像
im_copy.rotate(90)
```

### ImageDraw对象

- 添加文字水印和线条

```python
# coding=utf-8

from PIL import Image, ImageFont, ImageDraw

im = Image.new("RGBA", (1366, 768), color=(126, 126, 126, 100))
w, h = im.size
w_draw, h_draw = int(w * 0.84), int(h * 0.88)

# 创建ImageDraw.Draw对象，font对象
draw = ImageDraw.Draw(im)
fnt = ImageFont.truetype("monaco.ttf", size=18)
text = "pillow"

# 添加文字
draw.text((w_draw+15, h_draw+15), text, font=fnt, fill=(255, 255, 255, 80))

# 划线
draw.line(((0, h_draw-10), (w, h_draw-10)), fill=(255, 255, 255, 30), width=10)
draw.line(((w_draw-10, 0), (w_draw-10, h)), fill=(255, 255, 255, 30),
          width=10)

# 保存
im.save("pillow_draw.png")
```

- 生成照片墙

```python
from PIL import Image, ImageFont, ImageDraw

# 创建小图
pic = Image.new("RGBA", (50,50), color="grey")

# 创建大图
bg = Image.new("RGBA", (500,500), color="red")
p_w, p_h = pic.size
b_w, b_h = bg.size

# 设置字体
fnt = ImageFont.truetype("monaco.ttf", size=22)

# 创建Image.Draw对象
draw = ImageDraw.Draw(pic)

# 小图上添加文字
draw.text((int(p_w/3), int(p_h/3)), "*_*", fill=(255,255,255,60))

# 遍历大图，粘贴小图
for x in range(int(b_w/p_w)):
    for y in range(int(b_h/p_h)):
        bg.paste(pic, (x*p_w, y*p_h))

# 保存文件
bg.save("pic_wall.png")
```

- 实例
    - 生成缩略图
    - 添加水印
    - 生成照片墙
    - 混合图像
    - 滤波器
    -

