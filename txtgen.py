import argparse
from PIL import Image, ImageDraw, ImageFont
import os

def create_image(text_size, text, font_path, color, invert):
    # background transparente
    background = (255, 255, 255, 0)

    # se invert for True, a cor do texto será a cor de fundo e a cor de fundo será a cor do texto
    if invert:
        color, background = background, color

    font = ImageFont.truetype(font_path, text_size) # Carrega a fonte

    # Cria uma imagem temporária para medir o tamanho do texto
    dummy_image = Image.new("RGBA", (1, 1)) # Imagem de 1x1 pixel
    draw = ImageDraw.Draw(dummy_image) # Cria um objeto para desenhar na imagem
    width, height = draw.textbbox((0, 0), text, font=font)[2:4] # Mede o tamanho do texto

    # Cria uma imagem com fundo transparente
    image = Image.new("RGBA", (width, height), background) # Imagem com fundo transparente
    draw = ImageDraw.Draw(image) # Cria um objeto para desenhar na imagem

    # Desenha o texto na imagem
    draw.text((0, 0), text, font=font, fill=color)# (0, 0) é a posição do texto

    # Nome do arquivo de saída
    output_file = f"{os.path.splitext(os.path.basename(font_path))[0]}-{text}-{color}.png"
    # output_path = os.path.join(output_dir, output_file)

    # output_path deve ser a pasta onde ficam as imagens, independente do sistema operacional
    # windows: C:\Users\usuario\Pictures\Fontastic
    # linux: /home/usuario/Images/Fontastic
    # mac: /Users/usuario/Pictures/Fontastic
    # se pasta não existir, criar

    if os.name == 'nt':
        if not os.path.exists(os.path.join(os.path.expanduser("~"), "Pictures", "Fontastic")):
            os.makedirs(os.path.join(os.path.expanduser("~"), "Pictures", "Fontastic"))
        output_path = os.path.join(os.path.expanduser("~"), "Pictures", "Fontastic", output_file)
    elif os.name == 'posix':
        if not os.path.exists(os.path.join(os.path.expanduser("~"), "Images", "Fontastic")):
            os.makedirs(os.path.join(os.path.expanduser("~"), "Images", "Fontastic"))
        output_path = os.path.join(os.path.expanduser("~"), "Images", "Fontastic", output_file)
    else:
        if not os.path.exists(os.path.join(os.path.expanduser("~"), "Pictures", "Fontastic")):
            os.makedirs(os.path.join(os.path.expanduser("~"), "Pictures", "Fontastic"))
        output_path = os.path.join(os.path.expanduser("~"), "Pictures", "Fontastic", output_file)

    if invert:
        output_path = output_path.replace(".png", "-inverted.png")

    # Salva a imagem
    image.save(output_path)
    
    return(f"Imagem salva em: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Gerar uma imagem PNG com texto.')
    parser.add_argument('text_size', type=int, help='Tamanho do texto')
    parser.add_argument('text', type=str, help='Texto a ser renderizado')
    parser.add_argument('font_path', type=str, help='Caminho para o arquivo de fonte TTF')
    parser.add_argument('color', type=str, help='Cor do texto (black, white, red, green, blue, yellow, purple, orange)')
    parser.add_argument('--output_dir', type=str, help='Diretório para salvar a imagem (padrão: Imagens)')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    print(create_image(args.text_size, args.text, args.font_path, args.color, args.output_dir))
