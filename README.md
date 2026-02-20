# INSSClaw 🦅 - Assistente Local de IA

**INSSClaw** é um framework personalizado de Agente de Inteligência Artificial focado no fluxo de trabalho e rotinas de um servidor do INSS. Inspirado em arquiteturas descentralizadas e seguras (como ZeroClaw, IronClaw e AgentZero), este projeto traz o poder analítico da IA para o terminal local do servidor, agilizando tarefas repetitivas, pesquisa legislativa e formulação de despachos.

⚠️ **DISCLAIMER OFICIAL E RESPONSABILIDADE DOS DADOS** ⚠️

> Esta ferramenta **NÃO** é uma aplicação oficial do Governo Federal ou do INSS. É um projeto auxiliar construído para uso pessoal/estudo de produtividade no serviço público.
>
> **Atenção Servidor:** Ao lidar com dados sensíveis de cidadãos brasileiros (CPFs, NBs, Nomes, Informações Previdenciárias e Bancárias), o servidor público federal está sob o escopo da Lei Geral de Proteção de Dados (LGPD) e normativos internos de segurança da informação do Governo. **O INSSClaw não exime o servidor dessa responsabilidade.** Dados reais de segurados jamais devem ser transmitidos sem o devido mascaramento para servidores externos ou LLMs não-homologados.

## 🛡️ Foco Central: Segurança e Privacidade (Privacy-First)

A arquitetura do INSSClaw foi desenhada sob a premissa de **Zero Trust** com provedores externos de IA. Nossos principais mecanismos de segurança são:

### 1. Modelo de IA Local (Ollama)

O ambiente ideal e arquitetura primordial deste projeto preveem o uso de modelos hospedados **100% localmente via [Ollama](https://ollama.com/)**. Isso assegura que nenhum trecho de texto saia do computador institucional, eliminando qualquer chance de vazamento de dados de Segurados para a nuvem.

### 2. PII Masker (O Escudo de Anonimização)

Para cenários onde modelos locais pesados (ex: Llama-3 70b) não podem rodar devido a hardware limitado, e o uso de APIs robustas (ex: Anthropic Claude, OpenAI) se faz extraordinariamente necessário, o INSSClaw conta com um **Motor de Anonimização Obrigatório (`pii_masker.py`)**.
Antes de o texto sair da máquina, CPF's, Números de Benefício (NB) e Nomes Completos são varridos por Expressões Regulares (Regex) e substituídos por "Tokens" (`[CPF_X]`, `[NOME_Y]`).
A IA em nuvem processa os tokens falsos, e somente ao encerramento a inteligência local reconstitui os dados no documento final. **Nenhum dado real cruza a rede.**

## ⚙️ Funcionalidades Internas

- **Memória Infinita de Legislação (RAG Local):** Um hub com banco de dados vetorial (ChromaDB) acoplado, permitindo que milhares de PDFs (INs, Portarias, Leis) fiquem guardados localmente. O Agente é capaz de ler milhares de páginas em segundos para localizar a fundamentação legal correta e entregar um resumo referenciado.
- **Automação Nível-Navegador:** Abandono da antiga dependência de extensões de Firefox. O agente opera automação de cliques (Browser Subagent / Playwright) simulando o servidor e preenchendo as planilhas complexas nos sistemas (SABI / PMF / Salweb) sem interação de terceiros.
- **Despachos Limpos (Texto Puro):** Fim dos enfeites de "Markdown", títulos e listas gerados por IAs que quebram formatações. O Output System do INSSClaw gera blocos de texto puro, projetados exclusivamente para o Ctrl+C e Ctrl+V direto no PMF/SGI.

## 📁 Estrutura de Diretórios e Ocultamento

Os dados privados **NÃO fazem parte deste repositório**. Nosso `.gitignore` restringe severamente os arquivos que são versionados.

- `scripts/` -> Automações, Motor PII e Motor Chroma (Código Aberto)
- `.agents/workflows/` -> Skills padronizadas do Agente de Despacho (Código Aberto)
- `pdfs/` -> **[IGNORADO PELO GIT]** Repositório local secreto de PDFs (Leis Privadas, Documentos INSS)
- `chroma_db/` -> **[IGNORADO PELO GIT]** Banco de dados vetorial de uso isolado da máquina.

---

_Inspirado nas melhores práticas globais de construção de Agentes IA (Store Concepts: OpenClaw, NanoClaw e IronClaw Sandbox). Feito de servidor para servidor, focado no Brasil._
