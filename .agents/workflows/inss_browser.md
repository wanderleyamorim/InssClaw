---
description: INSS Browser Automation - Como o agente deve operar sistemas web do INSS (Meu INSS, PMF, Salweb).
---

Este workflow orienta o assistente (Antigravity) a usar sua própria ferramenta interna `browser_subagent` para cuidar de tarefas de preenchimento repetitivo nos sistemas web do INSS, ajudando a aposentar velhas extensões do Firefox.

**Instruções de Uso para o Agente:**

1. Quando o usuário disser algo como "Preencha o Salweb para este caso" ou "Lance os dados deste CNIS no Meu INSS", você **NÃO** deve dar apenas instruções textuais de como fazer.
2. Você DEVE ser proativo e acionar a sua ferramenta de `browser_subagent`.
3. O parâmetro `Task` enviado para o `browser_subagent` deve ser claro, passo a passo, detalhando exatamente quais dados preencher.
   - Exemplo de `Task` para o browser: _"Abra a URL do sistema do INSS. Aguarde a página carregar. Localize o campo de 'CPF' e preencha com '12345678900'. Clique no botão 'Avançar'. Na próxima tela de 'Renda', insira os valores mês a mês [1000, 1100, 1200...]. Terminando tudo, tire um print ou valide que a tela final de 'Sucesso' apareceu."_
4. O usuário confirmou (no Pilar 2 dos requisitos) que ele continuará efetuando os downloads manualmente, portanto, o agente deve focar exclusivamente em **Preenchimento de Formulários** e **Trabalho Mecânico de Cliques**.
5. Mantenha o usuário informado com mensagens curtas e diretas sobre o andamento e a conclusão da automação.
