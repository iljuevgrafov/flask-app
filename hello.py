from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'У меня получилось!'

'sdfsdfwefwvmdfnd ssopdruoghj;wegrhwqer98gvh8934v9vuwerv9wervhqiurhvuhwsar9hv8uqwervuophwer98vhshfruvhsdufphv9-8werhvupwerl;vhwe-89v-9uvh3u4vhq23-h4f3'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
