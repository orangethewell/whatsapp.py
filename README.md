# whatsapp.py
A biblioteca Whatsapp.py foi criada com o objetivo de facilitar a criação para bots no **Whatsapp Web**, assim, você pode criar bots que vão transformar mensagens como stickers, imagens, áudios e outros tipos em objetos dentro do python, tornando possível a interação da linguagem com os diferentes tipos de mensagem.

**OBS: Essa Branch não é recomendada para uso, são testes para novas funcionalidades e que muitas das vezes são salvas como funcionalidades ainda não funcionais, se decidir clonar esse repositório para uso, poderá testar as novas funcionalidades, porém não substitua o código do branch original por esse, pois o mesmo pode causar incompatibilidades e erros.**

---
## Como instalar?

Ainda não é possivel instalar a biblioteca do Whatsapp.py, porém esse é um dos objetivos para a biblioteca e assim que for possível, essa área será atualizada com as instruções.

Porém, caso você queira testar, poderá clonar o repositório e criar um script que importe o módulo Whatsapp dentro da pasta do repostório, assim como o `testbot.py` presente no repositório.

---
## Quais são os comandos?

Os comandos são:

* `Classe Client` : Você precisa criar um objeto com a classe Client, esse objeto poderá usar os comandos a seguir.
    * `Client.start(perma_connection = False)` : É o comando para iniciar a conexão com o **webdriver**, é executado para abrir o Whatsapp Web e esperar até que você conecte uma conta válida do whatsapp escaneando o QR Code.
       * `perma_connection` : Usado para caso você queira manter o seu whatsapp sempre aberto no webdriver, ativando ou desativando a conexão permanente, recebe os  valores `True` e `False`. 
    
    * `Client.select_contact(contact)`: Seleciona um contato para mandar e receber mensagens. O parâmetro `contact` recebe o **nome exibido no contato** (ou seja, não é possível pegar um contato por número se ele já estiver registrado na lista de contatos).
    
    * `Client.send_message(message)`: Envia uma mensagem para o contato selecionado.
    
    * `Client.listen()`: Retorna a última mensagem para o contato selecionado. Recomendado criar um loop com `if` e `else` para programar comandos.
    (OBS: Esse comando irá mudar futuramente)
---
## Futuros objetivos

- [x] Copiar e colar mensagem no Input; **(Essa instrução é interna, sem necessidade de instruções)**
- [x] Código assíncrono; **(Pronto! Instruções serão atualizadas antes do merge)**
- [ ] Sistema de fila de tarefas;
- [ ] Objetos para cada tipo de mensagem;
- [ ] Código no **PyPI**
- [ ] Sistema de avisos de Update;
- [ ] Sistema anti-spam;
- [ ] Servidor para atualizar classes em caso de mudança;
- [ ] Deixar o README em dia.
