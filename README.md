# ChefCasa 🍽️

O **ChefCasa** é uma plataforma que conecta clientes a chefs de cozinha para refeições personalizadas no conforto do lar. Semelhante ao iFood, mas focado na contratação de chefs, permitindo que os usuários agendem serviços diretamente pelo aplicativo.

## 🚀 Tecnologias Utilizadas

- **Frontend:** React Native (com Expo)
- **Backend:** FastAPI (Python)
- **Banco de Dados:** PostgreSQL
- **Autenticação:** JWT
- **Armazenamento:** AWS S3 ou Firebase Storage (planejado)

## 📂 Estrutura do Projeto

```
ChefCasa/
│── backend/    # Código da API FastAPI
│── frontend/   # Código do aplicativo React Native
│── docs/       # Documentação do projeto
│── .gitignore  # Arquivos ignorados pelo Git
│── README.md   # Este arquivo
```

## 🛠️ Como Rodar o Projeto

### 1️⃣ Clonar o Repositório
```sh
git clone https://github.com/Joaos32/ChefCasa.git
cd ChefCasa
```

### 2️⃣ Configurar o Backend (FastAPI)
```sh
cd backend
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # Configurar as variáveis de ambiente
uvicorn main:app --reload
```
A API estará rodando em `http://127.0.0.1:8000`

### 3️⃣ Configurar o Frontend (React Native)
```sh
cd ../frontend
yarn install  # ou npm install
expo start
```

## 🧑‍💻 Como Contribuir
1. **Faça um Fork** deste repositório.
2. **Crie uma Branch** com a nova funcionalidade: `git checkout -b feature/nova-funcionalidade`
3. **Commit suas alterações**: `git commit -m "feat: adicionar nova funcionalidade"`
4. **Faça um Push** para sua branch: `git push origin feature/nova-funcionalidade`
5. **Abra um Pull Request** 🚀

---

📌 **Em desenvolvimento**: Estamos implementando autenticação, pagamento e melhorias na interface! Fique ligado!

