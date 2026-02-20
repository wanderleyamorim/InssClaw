---
description: INSS Despacho - Gera uma resposta em formato de texto puro (sem markdown) prontas para "Copiar e Colar" em sistemas do INSS (SABI, PMF, etc).
---

Este workflow atua como uma **Skill** ou instrução nativa do assistente para garantir que as análises documentais do INSS sempre produzam saídas em **TEXTO PURO**, prontas para o funcionário do INSS copiar e colar no sistema, sem dor de cabeça com formatações.

**Regras estritas deste workflow:**

1. A resposta final deve ser **APENAS TEXTO PURO**.
2. **NÃO utilize** tags ou estilos do Markdown. Sem negritos (`**`), sem itálicos (`*` ou `_`), sem títulos com cercadilhas (`#`), sem listas com marcadores (`-` ou `*`).
3. O texto deve ser formatado em blocos de parágrafos simples, limpos e separados por pular linha.
4. **Resumo direto:** Evite saudações excessivas ou frases genéricas no início ou no fim do texto (como "Aqui está o despacho solicitado" ou "Espero ter ajudado"). Entregue DIRETAMENTE o cerne do despacho.
5. Quando for fornecer valores (R$), alinhe-os perfeitamente em modo de texto puro, se necessário.

**Exemplo Prático de Uso da Skill:**

1. _Usuário:_ "Execute o workflow inss_despacho para analisar este CNIS e diga se ele atinge os requisitos para LC123, gerando o parecer do benefício."
2. _Agente:_ O agente fará o raciocínio interno ou via `<thought>`, mas a resposta amigável ao usuário será APENAS O TEXTO DO DESPACHO como se fosse digitado no Bloco de Notas (Notepad).

**Integração PII Masker:**

- Se o usuário solicitou PII masking de dados confidenciais, o script `pii_masker.py` deve ser usado antes de rodar a inteligência, processando os CPFs, NBs e nomes. No fim, a formatação limpa final (inss_despacho) sairá com as tags (ex: `[[CPF_1]]`) para posterior restauração ou o próprio usuário os preencherá na tela.
