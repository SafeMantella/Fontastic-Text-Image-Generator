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
git clone https://github.com/SafeMantella/Fontastic-Text-Image-Generator.git
cd Fontastic-Text-Image-Generator
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

---

## `txtgen_fixed.py` — versão corrigida e estendida (2026)

O `txtgen.py` original tem 3 bugs que atrapalham o uso real via terminal/automação:

1. **`--output_dir` nunca era realmente usado.** O bloco `__main__` chamava `create_image(args.text_size, args.text, args.font_path, args.color, args.output_dir)` — mas a assinatura da função é `create_image(text_size, text, font_path, color, invert)`. Ou seja, o valor de `output_dir` era passado no lugar de `invert`, e a imagem sempre ia parar em `~/Pictures/Fontastic` ou `~/Images/Fontastic`, nunca onde o `--output_dir` pedia.
2. **Só aceitava nomes de cor do Pillow** (`black`, `white`, `red`...), não hex (`#1E3A47`) — inviável pra trabalhar com uma paleta de marca definida em hex.
3. **Sem suporte a variable fonts.** Fontes modernas do Google Fonts (Sora, Inter, etc.) costumam vir como variable font de eixo único `wght` num arquivo só, em vez de um arquivo por peso. `ImageFont.truetype()` sozinho carrega sempre a instância default — pra pegar um peso específico (ex: 500/Medium) é preciso `font.set_variation_by_axes([peso])` ou `font.set_variation_by_name("Medium")`, que o script original não fazia.

`txtgen_fixed.py` corrige os três, mantendo a mesma ideia (texto → PNG transparente com uma fonte TTF qualquer):

```sh
python txtgen_fixed.py <text_size> "<texto>" <font_path> <cor> <output_path> [--weight N] [--instance NOME] [--bg transparent|hex] [--padding N]
```

Exemplo (título em Sora peso 500, cor hex, fundo transparente):
```sh
python txtgen_fixed.py 120 "PEDRO ARFUX" fonts/Sora-Variable.ttf "#F7F5F0" out/titulo.png --weight 500
```

`window.py` (a GUI) continua valendo como está — os fixes são só na ponta de terminal, que é a que faz sentido pra automação/agentes.

---

## Fontes (TTF) — não incluídas neste repositório

As fontes usadas nos exemplos acima (Sora, Inter, JetBrains Mono) **não são commitadas aqui** — são propriedade de terceiros, e mesmo estando sob licenças abertas (SIL Open Font License), esse repo não redistribui os arquivos binários de ninguém. Baixe localmente numa pasta `fonts/` (já ignorada pelo `.gitignore`) antes de rodar os exemplos:

```sh
mkdir -p fonts && cd fonts

# Sora e Inter (variable fonts, direto do repo oficial do Google Fonts)
git clone --depth 1 --filter=blob:none --sparse https://github.com/google/fonts.git gfonts
cd gfonts && git sparse-checkout set ofl/sora ofl/inter && cd ..
cp "gfonts/ofl/sora/Sora[wght].ttf" Sora-Variable.ttf
cp "gfonts/ofl/inter/Inter[opsz,wght].ttf" Inter-Variable.ttf 2>/dev/null || echo "confira o nome exato do arquivo em gfonts/ofl/inter/"
rm -rf gfonts

# JetBrains Mono (repo oficial da JetBrains, TTFs estáticos)
git clone --depth 1 https://github.com/JetBrains/JetBrainsMono.git jbmono
cp jbmono/fonts/ttf/JetBrainsMono-Regular.ttf .
cp jbmono/fonts/ttf/JetBrainsMono-Medium.ttf .
rm -rf jbmono

cd ..
```

Qualquer outra fonte TTF sua (ou baixada de onde você tiver licença de uso) funciona normalmente — é só apontar `font_path` pro arquivo.

---

## Por que isso é útil pra agentes de IA (Claude Code, Cursor, e afins)

Esse projeto nasceu antes da onda de agentes de codificação, mas é um exemplo bom do tipo de ferramenta que funciona *muito bem* como peça de um pipeline operado por um agente de IA:

- **Contrato de entrada/saída simples e determinístico.** `argumentos → arquivo PNG`. Um agente consegue chamar isso repetidamente, em lote, sem ambiguidade sobre o que vai ser gerado.
- **Sem dependência de GUI pra automação.** A versão de terminal roda em qualquer sandbox headless (é exatamente o que um agente de codificação usa).
- **Contorna uma limitação real de ferramentas de design com IA.** APIs de geração de design (Canva, por exemplo) frequentemente não dão controle fino sobre fonte exata — o modelo de geração escolhe uma fonte "parecida", não a que você pediu. Renderizar o texto localmente com a fonte real e depois compor/inserir isso na peça final é um jeito simples de recuperar esse controle.
- **Fácil de estender.** É só Pillow + Tkinter, então um agente consegue ler, entender e corrigir o código inteiro em segundos (foi assim que os 3 bugs acima foram encontrados e corrigidos).

Se você (humano ou agente) está montando um pipeline de geração de imagens de marca — banners, thumbnails, tags técnicas, capas — e a ferramenta de design que você tem não dá controle de fonte via API, esse é o padrão: gerar o texto como PNG transparente aqui, depois compor sobre o fundo (localmente com Pillow, ou inserindo manualmente numa ferramenta como o Canva).

---

## Uso real: sistema de conteúdo automatizado (Pedro + Claude, Cowork)

Esse repositório voltou a ser usado em 2026 como parte de um sistema maior de automação de conteúdo pra redes sociais (Instagram, TikTok, YouTube, LinkedIn), construído em conjunto com o Claude dentro do Cowork.

Contexto rápido: o sistema tem uma identidade visual definida ("Autoridade quieta" — azul petróleo `#1E3A47`, off-white `#F7F5F0`, âmbar `#E0A458`, tipografia Sora/Inter/JetBrains Mono) e usa o Canva (via MCP) pra gerar parte das peças. Só que o MCP do Canva não permite setar a fonte de um elemento de texto via API (só cor/tamanho/peso/alinhamento) nem fazer upload de arquivo local (só URL pública) — então as peças geradas via IA do Canva saíam com fontes genéricas, fora do padrão.

A solução foi desenterrar esse projeto (feito antes dessa onda de ferramentas de IA), corrigir os bugs de compatibilidade com fontes variáveis modernas (seção acima) e usá-lo como a peça que gera o texto na fonte exata, fora do Canva — o resultado é composto localmente sobre o fundo da paleta (Pillow) ou inserido manualmente no Canva quando precisa de mais edição.

Esse é um caso real de "obstáculo → solução" documentado como conteúdo de bastidores do processo de construir esse sistema com IA — ver a série de posts sobre isso no Notion do projeto.

**Esse projeto deve continuar evoluindo conforme for sendo usado no pipeline.** Cada novo caso de uso, fix ou integração (ex: inserção automática numa ferramenta de design, geração em lote pro calendário editorial, etc.) deve virar uma atualização aqui — tanto no código quanto neste README.
