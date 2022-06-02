import discord

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def word_check(word,msg):
    if word in msg:
        return True

introduction= "Comment puis-je vous aider ? Vous pouvez utiliser !help connaitre les commandes !"
help_text= "Vous avez la commande !bot pour appeler le bot ! Pour avoir de l'aide, demandez en ! Pour retourner en arrière il suffit de demander de l'aide !"
aide_text= "Quel type d'aide avez vous besoin ? (doc, tuto)"
type_text= "Sur quel language ? (python, javascript)"



first_node =Node("!bot","!help","aide")
first_node.left= Node(None,None,None)
first_node.left.left= Node(None,None,None)

client = discord.Client()

@client.event
async def on_message(message):
    help_channel= client.get_channel(981838602126364692)
    if message.author == client.user:
        return

    if message.content == "!help":
        await help_channel.send(help_text)
    
    if message.content == "!bot":
        await help_channel.send(introduction)
    
    if word_check(first_node.right,message.content):
        first_node.left = Node("aide",None,None)
        await help_channel.send(aide_text)

    if word_check("doc",message.content) == True and first_node.left.left == None:
        first_node.left = Node("aide","doc",None)
        first_node.left.left= Node("doc", None, None)
        await help_channel.send(type_text)
    
    if word_check("tuto",message.content) == True and first_node.left.left == None:
        first_node.left = Node("aide","tuto",None)
        first_node.left.left = Node("tuto", None, None)
        await help_channel.send(type_text)

    if word_check("python",message.content) == True and first_node.left.left.left == None:
        if first_node.left.left.data == "doc":
            await help_channel.send("https://docs.python.org/3/library/index.html")
            first_node.left.left= Node(first_node.left.data,"python",None)
        elif first_node.left.left.data == "tuto":
            await help_channel.send("https://docs.python.org/fr/3/tutorial/")
            first_node.left.left= Node(first_node.left.data,"python",None)

    if word_check("javascript",message.content) == True and first_node.left.left.left == None:
        if first_node.left.left.data == "doc":
            await help_channel.send("https://devdocs.io/javascript/")
            first_node.left.left= Node(first_node.left.data,"javascript",None)
        elif first_node.left.left.data == "tuto":
            await help_channel.send("https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/JavaScript_basics")
            first_node.left.left= Node(first_node.left.data,"javascript",None)


client.run("OTgwNzM0MTk0OTExMTgyOTE4.GZqat8.-x58lCKSwI8Z39LtWsv7VKpHQT1wBtMxntAC_k")