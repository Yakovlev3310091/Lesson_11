
from flask import Flask

app = Flask(__name__)

@app.route("/")
def page_index():
    page_content = """ 
       <h1>Яковлев Александр</h1>
<h2>Привет, я студент Scypro</h2>
<img src="https://media.istockphoto.com/photos/funny-retro-sports-nerd-picture-id482708583?k=20&m=482708583&s=612x612&w=0&h=ZLSI_7Wsvyq2FJh0Iq7LMlj4V27cDYruUpjG3-p5m5U=" width="500" height="300" />
<br/>
<div>
В данный момент я работаю в компании Инверсия-Файбер
</div>
<div>
Наша компания производит одночастотные волоконные лазеры.
</div>
<div>
Я руковожу процессами продаж и логистики
</div>
<p>
    <strong>Женат</strong><br>
    <ins>Имею 3 детей</ins><br>
    <del>Воспитанием не занимаюсь</del><br>
    <em>По утрам хожу в спортзал</em></br>
    <mark>Раньше в свободное время читал, сейчас свободного времени нет</mark>
</p>
       
       """
    return page_content

app.run()


