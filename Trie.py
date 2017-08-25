class Node:

    def __init__(self, label=None, data=None):
        self.label=label
        self.data=data
        self.children=dict()

    def addNode(self,key,data=None):
        self.children[key]=Node(key,data)

    def __getitem__(self, key):
        return self.children[key]

class Trie:

    def __init__(self):
        self.root=Node()

    def addSentence(self,sentence):

        currentNode=self.root
        duplicateSentence = sentence.lower()
        word = duplicateSentence.replace(" ","")
        word_finshed=True

        for i in range(len(word)):
            if word[i] in currentNode.children:
                currentNode=currentNode.children[word[i]]
            else:
                word_finshed=False
                break;

        if not word_finshed:
            while i < len(word):
                currentNode.addNode(word[i])
                currentNode=currentNode.children[word[i]]
                i +=1

        currentNode.data=sentence

    def generate_completions(self,pref):

        sentences=list()
        newWord = pref.replace(" ","")

        if(pref==None):
            raise ValueError('Requires Non-Null prefix')

        top_node = self.root

        for letter in newWord:
            if letter in top_node.children:
                top_node=top_node.children[letter]
            else:
                return sentences

        if top_node == self.root:
            queue = [node for key,node in top_node.children.iteritems()]
        else:
            queue = [top_node]

        while queue:
            current_node = queue.pop()
            if current_node.data != None:
                sentences.append(current_node.data)

            queue = [node for key,node in current_node.children.iteritems()] + queue

        return sentences



