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
    
    * `Client.start_client(perma_connection = False)` : É o comando para iniciar a conexão com o **webdriver**, é executado para abrir o Whatsapp Web e esperar até que você conecte uma conta válida do whatsapp escaneando o QR Code.
        * Atributo `perma_connection = True/False`: É usado para ativar ou desativar a conexão permanente do Whatsapp com o Whatsapp Web. Caso desativado, após um tempo ocioso, o Whatsapp Web será desativado do Whatsapp.
    
    * `Client.select_contact(contact)`: Seleciona um contato para mandar e receber mensagens. O parâmetro `contact` recebe o **nome exibido no contato** (ou seja, não é possível pegar um contato por número se ele já estiver registrado na lista de contatos).
   
    * `Client.send_message(message)`: Envia uma mensagem para o contato selecionado.
    
    * `Client.listen()`: Retorna a última mensagem para o contato selecionado. Recomendado criar um loop com `if` e `else` para programar comandos.
    (OBS: Esse comando irá mudar futuramente)

---
## Futuros objetivos

- [ ] Copiar e colar mensagem no Input;
- [ ] Código assíncrono;
- [ ] Sistema de fila de tarefas;
- [ ] Objetos para cada tipo de mensagem;
- [ ] Código no **PyPI**
- [ ] Sistema de avisos de Update;
- [ ] Sistema anti-spam;
- [ ] Servidor para atualizar classes em caso de mudança;
- [ ] Deixar o README em dia.
