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

```python
from PIL import Image,ImageDraw

im = Image.open('flower.jpg')
width,height = im.size
# 创建画图对象
draw = ImageDraw.Draw(im)
# 对画图对象使用line方法,将图像四边中点连接起来，fill填充颜色，width表示线宽
draw.line((0,height/2)+(width/2,height)+(width,height/2)+(width/2,0)+(0,height/2),fill=(255,255,255,255),width=9)
im.save('line.jpg')

# 

```

- 实例
    - 生成缩略图
    - 添加水印
    - 生成照片墙
    - 混合图像
    - 滤波器
    -

