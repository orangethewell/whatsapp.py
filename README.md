# whatsapp.py
A biblioteca Whatsapp.py foi criada com o objetivo de facilitar a criação para bots no **Whatsapp Web**, assim, você pode criar bots que vão transformar mensagens como stickers, imagens, áudios e outros tipos em objetos dentro do python, tornando possível a interação da linguagem com os diferentes tipos de mensagem.

---
## Como instalar?

Ainda não é possivel instalar a biblioteca do Whatsapp.py, porém esse é um dos objetivos para a biblioteca e assim que for possível, essa área será atualizada com as instruções.

Porém, caso você queira testar, poderá clonar o repositório e criar um script que importe o módulo Whatsapp dentro da pasta do repostório, assim como o `testbot.py` presente no repositório.

---
## Quais são os comandos?

Os comandos são:

* `Classe Client` : Você precisa criar um objeto com a classe Client, esse objeto poderá usar os comandos a seguir.
    * `Client.start(perma_connection = False)` : É o comando para iniciar a conexão com o **webdriver**, é executado para abrir o Whatsapp Web e esperar até que você conecte uma conta válida do whatsapp escaneando o QR Code. Quando conectado ao Whatsapp Web, ele entra no loop principal.
       * `perma_connection` : Usado para caso você queira manter o seu whatsapp sempre aberto no webdriver, ativando ou desativando a conexão permanente, recebe os  valores `True` e `False`. 
    
    * `Client.select_contact(contact)`: Seleciona um contato para mandar e receber mensagens. O parâmetro `contact` recebe o **nome exibido no contato** (ou seja, não é possível pegar um contato por número se ele já estiver registrado na lista de contatos).
    
    * `Client.send_message(message)`: Envia uma mensagem para o contato selecionado.

    * `Client.listener()`: Inicia um loop para buscar novas mensagens, pode retornar funções indexadas pelo o decorador `@Client.event("on_message")` para serem executadas como um tipo de comando.

    
    * `Client.event()`: Usado apenas como decorador. Quando usado, coloca a função numa lista para ser executada a cada nova mensagem. Necessário usar dentro do comando embrulhado o trecho `if Client.get_message() == "your exec. command":` para não fazer um comando de spam.

    para mais informações, consulte o código `testbot.py` que possue um exemplo de uso.
---
## Futuros objetivos

- [x] Copiar e colar mensagem no Input;
- [x] Código assíncrono;
- [ ] Sistema de fila de tarefas; (?)
- [ ] Objetos para cada tipo de mensagem;
- [ ] Código no **PyPI**;
- [ ] Sistema de avisos de Update;
- [ ] Sistema anti-spam;
- [ ] Servidor para atualizar classes em caso de mudança;
- [x] Deixar o README em dia.
