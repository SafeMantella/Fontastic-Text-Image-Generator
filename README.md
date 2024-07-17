
# Text Image Generator

Este projeto gera uma imagem PNG com fundo transparente contendo texto utilizando uma fonte TTF. Ele inclui uma interface gráfica para facilitar a navegação.

## Requisitos

- Python 3.x
- Pillow
- Tkinter
- PyInstaller (para gerar executáveis)

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
python txtgen.py <text_size> <text> <font_path> <color> [--output_dir <output_dir>]
```

Exemplo:

```sh
python txtgen.py 64 "Hello, World!" "CloisterBlack.ttf" black
```

## Uso via Interface Gráfica

1. Execute o script `window.py` para abrir a interface gráfica.

```sh
python window.py
```

2. Preencha os campos necessários e clique em "Generate Image" para criar a imagem.

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

## Links de Download

- [Download do executável para Windows](link-para-download-windows)
- [Download do executável para macOS](link-para-download-macos)

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
