Na Lenha com Ferreira - Website com Backend Python
Este projeto contém o site "Na Lenha com Ferreira", um serviço de personal chef e consultoria gastronômica, com backend em Python para exibir imagens dinâmicas do perfil do Instagram.

Recursos
🍽️ Site completo para serviço de personal chef
📸 Integração com fotos do Instagram @nalenhacomferreira
📱 Design responsivo para dispositivos móveis
📋 Formulário de orçamento integrado com WhatsApp
📅 Integração de agendamento com Google Calendar
💬 Depoimentos de clientes
📊 Backend em Flask para processamento de dados
Estrutura do Projeto
na-lenha-com-ferreira/
│
├── app.py                  # Aplicação Flask principal 
├── run.py                  # Script de inicialização
├── generate_placeholders.py # Gerador de imagens placeholder
├── requirements.txt        # Dependências Python
├── Dockerfile              # Configuração do Docker
│
├── static/                 # Arquivos estáticos
│   ├── css/
│   │   └── style.css       # Estilos CSS
│   ├── js/
│   │   └── main.js         # Scripts JavaScript
│   └── images/             # Imagens geradas e placeholders
│
└── templates/              # Templates HTML
    └── index.html          # Página principal
Requisitos
Python 3.8+
Flask
Instaloader (para buscar imagens do Instagram)
PIL (Pillow) para geração de imagens
Outras dependências listadas em requirements.txt
Instalação
Clone este repositório: git clone https://github.com/seu-usuario/na-lenha-com-ferreira.git cd na-lenha-com-ferreira

Crie e ative um ambiente virtual: python -m venv venv source venv/bin/activate # No Windows: venv\Scripts\activate

Instale as dependências: pip install -r requirements.txt

Configure o ambiente: python run.py --setup

Inicie a aplicação: python run.py

Acesse o site em http://localhost:5000

Uso com Docker
Construa a imagem: docker build -t nalenhacomferreira .

Execute o contêiner: docker run -p 5000:5000 nalenhacomferreira

Acesse o site em http://localhost:5000

Personalização
Edite templates/index.html para alterar o conteúdo da página
Modifique static/css/style.css para personalizar os estilos
Ajuste app.py para alterar a lógica de backend
Limitações da API do Instagram
Devido às restrições da API não oficial do Instagram usada (Instaloader), o sistema pode ter limitações de taxa de requisição. Para evitar problemas:

As imagens são armazenadas em cache por 1 hora
Imagens de fallback são usadas quando a API falha
São exibidas no máximo 8 imagens recentes
Licença
Este projeto está licenciado sob a licença MIT.