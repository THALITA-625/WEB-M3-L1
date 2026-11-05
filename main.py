from flask import Flask
import random

app = Flask(__name__)
facts_list = ["Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten",
              "Elon Musk juga menganjurkan regulasi jejaring sosial dan perlindungan data pribadi pengguna. Dia mengklaim bahwa jejaring sosial mengumpulkan sejumlah besar informasi tentang kita, yang kemudian dapat digunakan untuk memanipulasi pikiran dan perilaku kita",
              "Menurut sebuah studi tahun 2019, lebih dari 60% orang merespons pesan pekerjaan di ponsel mereka dalam waktu 15 menit setelah pulang kerja",
              "Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.",
              "Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka"
]
facts2_list = ["i'm an omnivert", 
              "i like to play minecraft, mobile legends, and sometimes roblox",
              "my main hobby was speedcubing",
              "i can play piano",
              "sometimes i would code for some reason, idk why honestly",
              "i like soccer, archery, and lot more cuz i can't type it here biar SPJ(singkat padat jelas)",
              "my fav character is kai smith from ninjago",
              "i don't like being pictured but i like taking photos😭🥀",
              "my fav football player is harry kane"
]
@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1> <a href="/smth">View a random fact!</a>'

@app.route("/smth")
def something():
    return f'<h1>{random.choice(facts_list)}</h1><a href="/">Back</a>'

@app.route("/about")
def about():
    return '<h1>some facts about me</h1>''<h2>{random.choice(facts2_list)}</h2><a href="/">Back</a>''

app.run(debug=True)