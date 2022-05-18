from flask import Flask, render_template,request

app = Flask(__name__)

def isPrime(n):
  if n < 2:
    # 2未満は素数でない
    return False
  if n == 2:
    # 2は素数
    return True
  for p in range(2, n):
      if n % p == 0:
        # nまでの数で割り切れたら素数ではない
        return False
  # nまでの数で割り切れなかったら素数
  return True

@app.route('/')
def index():
    return render_template('index.html', message="数字を入力してください")

@app.route('/result', methods=["GET"])
def result_get():
    # GET送信の処理
    field = request.args.get("field","")
    if int(field) % 2 == 0:
        t = "偶数"
    else:
        t = "奇数"
    return render_template('result.html', number=str(field), jatchi="{}である".format(t))

@app.route('/result', methods=["POST"])
def result_post():
    # POST送信の処理
    field = request.form["field"]

    if isPrime(int(field)):
        t = "素数である"
    else:
        t = "素数でない"
    return render_template('result.html', number=str(field), jatchi=t)

if __name__ == '__main__':
    app.run()