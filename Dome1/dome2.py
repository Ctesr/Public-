from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# 配置邮件服务
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # 使用 Gmail SMTP 服务器
app.config['MAIL_PORT'] = 587  # SMTP 端口
app.config['MAIL_USE_TLS'] = True  # 启用 TLS
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # 填入你的邮箱
app.config['MAIL_PASSWORD'] = 'your-email-password'  # 填入你的邮箱密码或应用专用密码
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'  # 默认发件人

mail = Mail(app)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    message = data.get('message', '').strip()

    if not message:
        return jsonify({'error': 'Message cannot be empty'}), 400

    try:
        msg = Message('New Message from Your Website',
                      recipients=['fjc@idd.cool'])  # 收件人邮箱
        msg.body = message  # 邮件正文

        mail.send(msg)
        return jsonify({'message': 'Email sent successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
