from PIL import Image, ImageDraw, ImageFont


def add_text_to_image(text, image_path="static/gramot.png", output_path="output_image.png", font_size=30,
                      text_color=(0, 0, 0), font_path=None):
    # Открываем изображение
    text = text.replace(' ', '\n')
    text = f"Спасибо за участие \n в развивающемся проекте Flask \n с кодовым названием БТПМ \n Данной грамотой награждается: \n {text}"
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("font.ttf", size=font_size, encoding='UTF-8')
    # Определяем координаты для выравнивания по центру
    x = 100
    y = 400
    print(x, y)

    # Добавляем текст на изображение
    draw.text((x, y), text, fill=text_color, font=font)

    # Сохраняем измененное изображение
    image.save(output_path)
