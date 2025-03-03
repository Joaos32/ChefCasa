# 📢 Política de Segurança do ChefCasa

Este documento define as diretrizes para reportar e corrigir vulnerabilidades no projeto ChefCasa.

## 🛡️ Relatando Problemas de Segurança

Se você encontrar uma vulnerabilidade de segurança no ChefCasa, siga estas etapas:

1. **Não crie uma issue pública.** Em vez disso, entre em contato diretamente pelo e-mail: `security@chefcasa.com`.
2. **Forneça detalhes completos** sobre a vulnerabilidade, incluindo:
   - Como reproduzir o problema.
   - Impacto potencial.
   - Possíveis soluções sugeridas.
3. Aguarde nossa equipe analisar o problema e fornecer uma resposta.

## 🔒 Boas Práticas de Segurança no Projeto

- **Nunca exponha credenciais no código-fonte.** Use arquivos `.env` para variáveis sensíveis.
- **Utilize hashing para senhas e tokens.** O ChefCasa usa `bcrypt` para senhas e JWT para autenticação.
- **Valide entradas do usuário** para evitar injeção de SQL e XSS.
- **Mantenha dependências atualizadas** para corrigir possíveis vulnerabilidades.
- **Restrinja permissões no banco de dados** para evitar acessos indevidos.

## 📆 Ciclo de Atualizações de Segurança

- **Monitoramos vulnerabilidades** em dependências usando ferramentas como Dependabot e Snyk.
- **Correções críticas** serão aplicadas e comunicadas rapidamente aos usuários.
- **Relatórios de segurança** serão publicados no repositório sempre que necessário.

---

Se tiver dúvidas ou sugestões, entre em contato pelo e-mail de segurança! 🚀

joaovitor3255silva@gmail.com