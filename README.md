# Letícia Caires | Psicanálise

Site institucional de uma página. HTML/CSS/JS puro, sem build, sem framework —
abre local com duplo clique em `index.html` ou serve estático em qualquer host.

## Paleta e tipografia

- **Verde escuro** `#1E3A2C` / `#142822` + **dourado** `#B8934A` + **creme** `#F7F2E4`,
  motivos botânicos discretos (as texturas de folha nos cards de "Áreas de foco" são
  SVG desenhado à mão, não fabricado por IA nem stock).
- Tipografia: **Libre Bodoni** (títulos e wordmark, itálico na marca) + **Public Sans**
  (corpo) — serifada elegante + sans limpa, evitando o par Playfair+Inter (o "óbvio"
  de qualquer gerador de site).
- CTA em dourado, não no verde do WhatsApp — o verde já é a cor da marca dela, um
  botão verde-WhatsApp por cima ficaria confuso com a identidade.

## ⚠️ Sobre as fotos — leia antes de publicar

Só chegou **uma foto real** pra esse projeto: `foto_evento_01.png`, do evento
"Amigas de Peito" (banner rosa, cheio de logo de patrocinador — provavelmente
campanha de Outubro Rosa). É exatamente a foto que o próprio briefing avisou que
precisava de confirmação por estar ligada a uma causa de terceiros.

**Decisão tomada (a pedido do Maxwel, sem confirmação direta da Letícia):** usar
essa foto mesmo assim no Hero e em Sobre, tratada em `ferramentas/build_imagens.py`
com um efeito de profundidade de campo falso (fundo desfocado + tingido bem forte
na cor da marca, pra virar uma mancha verde abstrata em vez do banner de
patrocinador legível) e ela nítida no centro. **Isso não é um cutout perfeito** —
tentei remoção de fundo de verdade (`rembg`) duas vezes e o ambiente não conseguiu
carregar o modelo (erro de alocação de memória); o resultado final é o melhor que
deu pra chegar só com desfoque + cor, sem segmentação real.

**Antes de publicar de verdade, vale conseguir com ela:**
- Uma foto de rosto sem o banner de fundo (mesmo que informal, celular mesmo) —
  troca simples em `assets/originais/` + rodar o pipeline de novo.
- Confirmação de que pode usar essa foto específica do evento (é campanha de
  terceiros, não da marca dela).

Os 5 cards de "Áreas de foco" usam textura botânica (SVG), não foto — de propósito,
pra não repetir a única foto disponível em 5 lugares diferentes.

## Setembro Amarelo (banner sazonal)

Existe um banner pronto no topo do site (`#banner-setembro` em `index.html`),
**desligado por padrão** (atributo `hidden`). Pra ativar em setembro: apague o
`hidden` do elemento. Pra desligar de novo: coloque `hidden` de volta. Não precisa
mexer em CSS nem JS.

## Pontos em aberto pra confirmar com a cliente

- **FAQ:** as respostas sobre plataforma de atendimento, critério de adulto vs.
  infantil e a política de valor social foram escritas de forma genérica/honesta,
  sem inventar detalhe que não veio no briefing (ex.: não citei o valor de R$50
  como preço atual, só a existência de vagas sociais). Revisar com ela antes de
  publicar.
- **Selo "presença em mídia"** (podcast/TV) do briefing original foi **deixado de
  fora** dos selos de confiança — o briefing pedia pra citar "se ela confirmar
  quais", e isso não foi confirmado. Se ela topar, é só trocar um dos 4 selos
  atuais.
- **Link do WhatsApp** usado: `wa.me/message/BXXV2KBYNVWLM1`, exatamente como veio
  no briefing.

## Estrutura

```
index.html
assets/css/style.css
assets/js/main.js          -- so o comportamento do acordeao do FAQ
assets/img/                -- hero, sobre, og, favicon
assets/originais/          -- foto original, nao usada direto no site
ferramentas/build_imagens.py -- pipeline de tratamento da foto
```
