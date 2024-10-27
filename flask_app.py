from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import google.generativeai as genai

app = Flask(__name__)
model = genai.GenerativeModel("gemini-1.5-pro")
genai.configure(api_key='AIzaSyBwlhNaCmKcmpAV_aYCsxnQvhOOIV4IO7g')

def generate_response(user_message):
    chat = model.start_chat(
        history=[]
    )
    response = chat.send_message(user_message).text
    print('Respuesta del modelo:', response)
    return response

@app.route('/whatsapp', methods=['POST', 'GET'])
def whatsapp():
    user_message = request.form.get('Body')  # Aquí obtienes el mensaje del usuario
    print('Mensaje del usuario:', user_message)

    response = MessagingResponse()

    response.message(generate_response(user_message))

    return str(response)

if __name__ == '__main__':
    app.run(port=8080)