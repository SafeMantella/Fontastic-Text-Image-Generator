
# Fontastic Text Image Generator

Este script gera uma imagem PNG com fundo transparente contendo texto em um tamanho especificado e usando uma fonte TTF especificada.

## Rodando o programa



## Testando o código

Certifique-se de ter o Python e o `pip` instalados. Você também precisa instalar a biblioteca `Pillow`.

```sh
pip install pillow
```

## Uso

```sh
python create_text_image.py <text_size> <text> <font_path> <color>
```

### Parâmetros

- `text_size` (int): O tamanho do texto.
- `text` (str): O texto a ser renderizado na imagem.
- `font_path` (str): O caminho para o arquivo de fonte TTF.
- `color` (str): A cor do texto. Cores suportadas são: black, white, red, green, blue, yellow, purple, orange.
- `--output_dir` (opcional, str): O diretório para salvar a imagem. O padrão é `Imagens`.

### Exemplo

```sh
python create_text_image.py 64 "Hello, World!" "CloisterBlack.ttf" black
```

Isso irá gerar uma imagem com o texto "Hello, World!" no tamanho 64 usando a fonte `CloisterBlack.ttf` na cor preta. A imagem será salva no diretório `Imagens`.

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
