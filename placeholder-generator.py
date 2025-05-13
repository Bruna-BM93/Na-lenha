import os
from PIL import Image, ImageDraw, ImageFont
import random

# Cores tema
COLORS = [
    (139, 69, 19),   # --primary: #8B4513
    (210, 105, 30),  # --secondary: #D2691E
    (255, 140, 0),   # --accent: #FF8C00
    (255, 248, 220), # --light: #FFF8DC
    (62, 39, 35)     # --dark: #3E2723
]

def generate_placeholder_images():
    """
    Gera imagens placeholder para uso quando a API do Instagram falha
    """
    output_dir = 'static/images'
    os.makedirs(output_dir, exist_ok=True)
    
    # Gerar 4 imagens placeholder
    categories = [
        {'name': 'Prato gourmet', 'file': 'placeholder1.jpg', 'text': 'Gastronomia'},
        {'name': 'Evento corporativo', 'file': 'placeholder2.jpg', 'text': 'Eventos'},
        {'name': 'Mesa de jantar', 'file': 'placeholder3.jpg', 'text': 'Jantares'},
        {'name': 'Buffet de evento', 'file': 'placeholder4.jpg', 'text': 'Buffet'},
    ]
    
    for item in categories:
        # Criar uma nova imagem
        img = Image.new('RGB', (600, 400), color=COLORS[4])
        draw = ImageDraw.Draw(img)
        
        # Desenhar padrão de fundo
        for i in range(20):
            x1 = random.randint(0, 600)
            y1 = random.randint(0, 400)
            x2 = x1 + random.randint(50, 150)
            y2 = y1 + random.randint(50, 150)
            
            color = random.choice(COLORS[:3])
            opacity = random.randint(30, 100)
            color_with_opacity = color + (opacity,)
            
            draw.rectangle([x1, y1, x2, y2], fill=color, outline=None)
        
        # Adicionar texto ao centro
        try:
            # Tenta carregar uma fonte (se disponível)
            font = ImageFont.truetype("arial.ttf", 40)
        except IOError:
            # Caso contrário, usa a fonte padrão
            font = ImageFont.load_default()
            
        text = item['text']
        text_width, text_height = draw.textsize(text, font=font) if hasattr(draw, 'textsize') else (200, 50)
        
        position = ((600 - text_width) // 2, (400 - text_height) // 2)
        
        # Desenhar um retângulo por trás do texto
        padding = 20
        draw.rectangle(
            [
                position[0] - padding, 
                position[1] - padding, 
                position[0] + text_width + padding, 
                position[1] + text_height + padding
            ],
            fill=COLORS[3]
        )
        
        # Desenhar o texto
        draw.text(position, text, fill=COLORS[0], font=font)
        
        # Adicionar o nome "Na Lenha com Ferreira" na parte inferior
        footer_text = "Na Lenha com Ferreira"
        footer_width, footer_height = draw.textsize(footer_text, font=font) if hasattr(draw, 'textsize') else (250, 50)
        
        # Desenhar um retângulo por trás do texto do rodapé
        draw.rectangle(
            [
                0, 
                400 - footer_height - 20, 
                600, 
                400
            ],
            fill=(0, 0, 0, 180)
        )
        
        # Desenhar o texto do rodapé
        draw.text(
            ((600 - footer_width) // 2, 400 - footer_height - 10),
            footer_text,
            fill=COLORS[3],
            font=font
        )
        
        # Salvar imagem
        output_path = os.path.join(output_dir, item['file'])
        img.save(output_path)
        print(f"Imagem placeholder gerada: {output_path}")

    # Gerar imagem do cabeçalho
    header_img = Image.new('RGB', (1200, 400), color=COLORS[0])
    draw = ImageDraw.Draw(header_img)
    
    # Criar um padrão de fundo
    for i in range(50):
        x1 = random.randint(0, 1200)
        y1 = random.randint(0, 400)
        x2 = x1 + random.randint(100, 300)
        y2 = y1 + random.randint(50, 150)
        
        color = random.choice(COLORS[1:3])
        opacity = random.randint(30, 80)
        color_with_opacity = color + (opacity,)
        
        draw.rectangle([x1, y1, x2, y2], fill=color, outline=None)
    
    # Adicionar o nome "Na Lenha com Ferreira" no centro
    header_text = "Na Lenha com Ferreira"
    
    try:
        # Tenta carregar uma fonte (se disponível)
        header_font = ImageFont.truetype("arial.ttf", 80)
    except IOError:
        # Caso contrário, usa a fonte padrão
        header_font = ImageFont.load_default()
        
    header_width, header_height = draw.textsize(header_text, font=header_font) if hasattr(draw, 'textsize') else (600, 100)
    
    # Desenhar um retângulo semitransparente por trás do texto
    draw.rectangle(
        [
            (1200 - header_width) // 2 - 40, 
            (400 - header_height) // 2 - 40, 
            (1200 + header_width) // 2 + 40, 
            (400 + header_height) // 2 + 40
        ],
        fill=(0, 0, 0, 150)
    )
    
    # Desenhar o texto
    draw.text(
        ((1200 - header_width) // 2, (400 - header_height) // 2),
        header_text,
        fill=COLORS[3],
        font=header_font
    )
    
    # Salvar imagem do cabeçalho
    header_path = os.path.join(output_dir, 'header-bg.jpg')
    header_img.save(header_path)
    print(f"Imagem do cabeçalho gerada: {header_path}")

if __name__ == "__main__":
    generate_placeholder_images()
