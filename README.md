# Instagram Auto Follow Bot

Um bot automatizado para seguir usuários no Instagram de acordo com um nicho específico.

## Descrição

Este bot é desenvolvido em Python e utiliza a biblioteca Selenium para automatizar ações no Instagram. Ele permite que você faça login em sua conta do Instagram, pesquise um nicho específico, acesse a lista de pessoas que curtiram uma postagem relacionada a esse nicho e siga automaticamente um número definido de usuários.

O bot é útil para quem deseja expandir sua base de seguidores no Instagram, especialmente em um nicho específico, automatizando o processo de seguir outros usuários relevantes.

## Recursos

- Login automático na conta do Instagram
- Pesquisa de um nicho específico
- Acesso à lista de pessoas que curtiram uma postagem relacionada ao nicho
- Seguimento automático de um número definido de usuários
- Proteção contra limites de ações do Instagram

## Pré-requisitos

- Python 3
- Biblioteca Selenium: `pip install selenium`
- WebDriver para o navegador Firefox

## Configuração

1. Faça o download ou clone este repositório.
2. Instale as dependências necessárias executando o comando `pip install -r requirements.txt`.
3. Faça o download do WebDriver do Firefox apropriado para o seu sistema operacional e certifique-se de que o arquivo executável esteja no seu PATH.
4. Abra o arquivo `bot.py` em um editor de texto.
5. Preencha as informações de usuário, senha, nicho e quantidade de pessoas para seguir, nas variáveis correspondentes.
6. Salve as alterações no arquivo.

## Uso

1. Abra o terminal e navegue até o diretório do projeto.
2. Execute o comando `python bot.py` para iniciar o bot.
3. Aguarde enquanto o bot realiza as ações de login, busca e seguimento de usuários.
4. O bot finalizará automaticamente após seguir o número definido de usuários.

## Notas

- Este bot foi desenvolvido com base nas últimas informações disponíveis até setembro de 2021. No entanto, o Instagram pode fazer alterações em sua interface e políticas que podem afetar o funcionamento do bot.
- Utilize este bot com responsabilidade e dentro dos limites estabelecidos pelo Instagram para evitar restrições ou bloqueios de sua conta.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, correções de bugs ou novos recursos, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

