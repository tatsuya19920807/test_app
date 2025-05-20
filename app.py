#flaskパッケージのFlaskクラスを使用する
from flask import Flask, render_template

#appというFlaskクラスのインスタンスを作成します。
#app.<Flaskクラスのメソッド名>とすることでFlaskクラスのメソッドを使えるようにします。
app = Flask(__name__)

#appにrootで実行　http://127.0.0.1:5000/ 以降のパスを指定する
@app.route('/')
#htmlを参照してウェブサイトを構成
def hello_world():
    return render_template('index.html')

#このファイルが直接指定された場合のみ実行
if __name__ == "__main__":
    app.run(debug=false)
