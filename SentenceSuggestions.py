from flask import Flask, request, render_template, jsonify
import Trie
from Trie import Trie
from DataUpload import service_data


app = Flask(__name__)


@app.route('/')
def entry_point():
    return render_template('InitialPage.html')


@app.route('/autocomplete', methods=['GET'])
def suggestions():

    # Receiveing the parameters from the GET request
    queryParams = request.args.get('q')
    if queryParams=="":
        return 'null'
    # Creating a Trie object
    trie=Trie()

    # Creating a Full Trie from the corpus received
    sentences = service_data
    for sentence in sentences:
        trie.addSentence(sentence)

    # Getting the list of suggestions by supplying query
    result=trie.generate_completions(queryParams)

    return jsonify(Completions=result)


if __name__ == '__main__' :
    app.run(port=12345)
