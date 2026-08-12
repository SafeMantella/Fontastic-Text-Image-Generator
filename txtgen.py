"""
txtgen_fixed.py — versão corrigida/estendida do txtgen.py original
(https://github.com/SafeMantella/Fontastic-Text-Image-Generator)

O script original tinha 3 bugs que impediam uso confiável via terminal:
1. create_image() ignorava o --output_dir (o main chamava create_image(..., args.output_dir)
   passando a pasta no lugar do parâmetro `invert`).
2. Só aceitava nomes de cor do Pillow (black, white, red...), não hex (#1E3A47).
3. Sem suporte a variable fonts (Sora e Inter da Google Fonts vêm como variable font
   de eixo único `wght` — precisa selecionar a instância/peso via set_variation_by_axes).

Uso:
    python txtgen_fixed.py <text_size> "<texto>" <font_path> <cor> <output_path> [--weight N] [--bg TRANSPARENT|hex]

Exemplo (título do banner, Sora peso 500, âmbar):
    python txtgen_fixed.py 120 "PEDRO ARFUX" fonts/Sora-Variable.ttf "#F7F5F0" out/titulo.png --weight 500
"""
import argparse
import os
from PIL import Image, ImageDraw, ImageFont


def parse_color(c):
    """Aceita 'transparent', nome do Pillow, ou hex (#RRGGBB / #RRGGBBAA)."""
    if c.lower() == "transparent":
        return (255, 255, 255, 0)
    if c.startswith("#"):
        h = c.lstrip("#")
        if len(h) == 6:
            r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
            return (r, g, b, 255)
        if len(h) == 8:
            r, g, b, a = (int(h[i:i + 2], 16) for i in (0, 2, 4, 6))
            return (r, g, b, a)
    return c  # nome do Pillow (black, white, red, etc.)


def load_font(font_path, size, weight=None, instance_name=None):
    font = ImageFont.truetype(font_path, size)
    try:
        axes = font.get_variation_axes()
    except Exception:
        axes = None  # fonte estática, não é variable font

    if axes:
        if instance_name:
            font.set_variation_by_name(instance_name)
        elif weight:
            # assume eixo único 'wght' (caso do Sora e do Inter usados neste projeto)
            font.set_variation_by_axes([weight])
    return font


def create_image(text_size, text, font_path, color, output_path, weight=None,
                  instance_name=None, bg="transparent", padding=0):
    fill = parse_color(color)
    background = parse_color(bg)

    font = load_font(font_path, text_size, weight=weight, instance_name=instance_name)

    dummy = Image.new("RGBA", (1, 1))
    draw = ImageDraw.Draw(dummy)
    bbox = draw.textbbox((0, 0), text, font=font)
    width = bbox[2] - bbox[0] + padding * 2
    height = bbox[3] - bbox[1] + padding * 2

    image = Image.new("RGBA", (width, height), background)
    draw = ImageDraw.Draw(image)
    draw.text((padding - bbox[0], padding - bbox[1]), text, font=font, fill=fill)

    out_dir = os.path.dirname(output_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir)
    image.save(output_path)
    return output_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerar uma imagem PNG com texto (fundo transparente por padrão).")
    parser.add_argument("text_size", type=int)
    parser.add_argument("text", type=str)
    parser.add_argument("font_path", type=str)
    parser.add_argument("color", type=str, help="Nome Pillow ou hex (#RRGGBB)")
    parser.add_argument("output_path", type=str)
    parser.add_argument("--weight", type=int, default=None, help="Peso variável (ex: 400, 500, 700) para variable fonts")
    parser.add_argument("--instance", type=str, default=None, help="Nome da instância nomeada (ex: Medium, Bold)")
    parser.add_argument("--bg", type=str, default="transparent", help="'transparent' ou cor hex de fundo")
    parser.add_argument("--padding", type=int, default=0)

    args = parser.parse_args()
    result = create_image(
        args.text_size, args.text, args.font_path, args.color, args.output_path,
        weight=args.weight, instance_name=args.instance, bg=args.bg, padding=args.padding,
    )
    print(f"Imagem salva em: {result}")
