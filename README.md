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

## Sobre as fotos

O Hero e o "Sobre" usam um retrato real dela (`assets/originais/foto_retrato/`),
processado em `ferramentas/build_imagens.py` (recorte + leve ajuste de cor/nitidez,
sem tratamento artificial). Substituiu a primeira versão do site, que usava a única
foto disponível na época — de um evento com banner rosa de patrocinador ("Amigas de
Peito"), ainda guardada em `assets/originais/fotos_leticia_caires/` mas **fora de
uso** no pipeline atual.

Os 5 cards de "Áreas de foco" usam textura botânica (SVG), não foto — de propósito,
pra não repetir a mesma foto em 5 lugares diferentes.

## Minimapa

No fim da seção de CTA final (antes do rodapé), incorporado do Google Maps,
centrado em "São Judas, Piracicaba - SP" (bairro citado no perfil dela no Google).
Sem chave de API — é o embed público (`?output=embed`), então não carrega em
navegador automatizado/headless durante testes locais, mas funciona normal em
navegador de verdade.

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
