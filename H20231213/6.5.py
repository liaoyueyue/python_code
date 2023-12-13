# 为绿色麦田图片添加水印效果，文字为学号姓名。
# 安装了PIL库 pip install pillow

from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image_path, output_image_path, watermark_text):
    # 打开原始图片
    base_image = Image.open(input_image_path)

    # 创建一个与原始图片大小相同的透明图层
    transparent = Image.new('RGBA', base_image.size, (0, 0, 0, 0))

    # 在透明图层上绘制水印文字
    draw = ImageDraw.Draw(transparent)
    font = ImageFont.truetype("msyh.ttc", 150)  # 设置字体和大小
    draw.text((0, 0), watermark_text, font=font, fill=(255, 0, 0, 128))  # 设置水印颜色和透明度

    # 将透明图层与原始图片合并
    watermarked = Image.alpha_composite(base_image.convert('RGBA'), transparent)

    # 保存带有水印的图片
    watermarked.save(output_image_path)

# 使用示例
add_watermark('绿色麦田.jpeg', '绿色麦田加水印.png', 'student_num')
