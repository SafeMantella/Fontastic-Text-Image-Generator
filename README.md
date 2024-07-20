
# Text Image Generator

Este projeto gera uma imagem PNG com fundo transparente contendo texto utilizando uma fonte TTF. Ele inclui uma interface gráfica para facilitar a navegação.

## Requisitos

- Python 3.x
- Pillow
- Tkinter
- PyInstaller (para gerar executáveis)
- Um arquivo de fonte .ttf [como esses](https://www.dafont.com/ttf.d592)

## Instalação

1. Clone o repositório ou baixe os arquivos `window.py` e `txtgen.py`.

```sh
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Instale as dependências necessárias.

```sh
pip install pillow
```

## Uso via Terminal

1. Para gerar uma imagem diretamente pelo terminal, execute o script `txtgen.py` com os argumentos necessários.

```sh
python txtgen.py <text_size> <text> <font_path> <color> [--invert]
```

Exemplo (aqui eu baixei a fonte [Cloister Black](https://www.dafont.com/pt/cloister-black.font) e deixei na mesma pasta que o arquivo python):

```sh
python txtgen.py 64 "Hello, World!" "CloisterBlack.ttf" black
```

## Uso via Interface Gráfica

1. Execute o script `window.py` para abrir a interface gráfica.

```sh
python window.py
```

2. Preencha os campos necessários e clique em "Generate Image (Color on text)" para criar a imagem com texto colorido em fundo transparente, ou "Generate Image (Color on Backgound)" para criar a imagem com texto transparente em fundo colorido.

# Exemplos de imagens geradas
<img src="https://github.com/SafeMantella/Fontastic-Text-Image-Generator/blob/2b33d7fd9233909c8fdf224e0f4092fb5953484d/Generated%20Images/CloisterBlack-Demo-%230080ff.png" height="64"/>
<img src="https://github.com/SafeMantella/Fontastic-Text-Image-Generator/blob/2b33d7fd9233909c8fdf224e0f4092fb5953484d/Generated%20Images/CloisterBlack-THE%20GLORIOUS-white.png" height="64"/>
<img src="https://github.com/SafeMantella/Fontastic-Text-Image-Generator/blob/db2ffaeaaf6507a926a026250045620a27aa9963/Generated%20Images/Tomato%20Regular-ASTROWORLD-(255%2C%20255%2C%20255%2C%200)-inverted.png" height="64"/>

## Gerando Executáveis

### Windows

1. Abra o Prompt de Comando ou PowerShell e navegue até o diretório do projeto.
2. Execute o comando para criar o executável:

```sh
pyinstaller --onefile --windowed window.py
```

3. O executável será gerado na pasta `dist`.

### macOS

1. Abra o Terminal e navegue até o diretório do projeto.
2. Execute o comando para criar o executável:

```sh
pyinstaller --onefile --windowed window.py
```

3. O executável será gerado na pasta `dist`.
