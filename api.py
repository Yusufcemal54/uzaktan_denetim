from flask import Flask, request, jsonify
from datetime import datetime
import threading
import os
import subprocess
import pygetwindow as gw
import time
import winsound
import feedparser
from gtts import gTTS
import os
from playsound import playsound
import locale
import sys
import time
import subprocess

app = Flask(__name__)
api_running = True

@app.route('/')
def index():
    return """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bilgisayarı Uzaktan Yönet</title>
    <style>
        @font-face {
            font-family: 'MinecraftFont';
            src: url('https://uzaktandenetimapi.pages.dev/minecraft_font.ttf') format('truetype');
        }
        #onemli {
            color: red; 
            font-weight: 900
            }
        #baslik {
            color: red; 
            font-weight: bold; 
            }

        body {
            font-family: 'MinecraftFont', sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            flex-direction: column;
        }
        .container {
            text-align: center;
            background: white;
            padding: 2em;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin-bottom: auto; 
        }
        h1 {
            color: #333;
        }
        button {
            background-color: #008CBA;
            color: white;
            padding: 10px 20px;
            margin: 10px 0;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #005f73;
        }
        footer {
            color: red;
            text-align: center;
            font-size: 10px; 
            padding: 10px;
            width: 100%;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Bilgisayarı Uzaktan Yönet</h1>
        <form id="commandForm">
            <button type="button" onclick="sendSignal('derin_uyku')">Derin Uyku</button>
            <button type="button" onclick="sendSignal('shutdown')">Kapat</button>
            <button type="button" onclick="sendSignal('sound')">Ses Çal</button>
            <button type="button" onclick="sendSignal('eglence')">Eğlence</button>
        </form>
    </div>
    <footer>
    <p id="baslik">© 2024 YCŞ HOLDİNG. Tüm hakları EBEDİYYEN saklıdır.
    <p id="onemli">BU SİTEYİ KULLANARAK TELİF HAKKI BİLDİRGESİNİ OKUMUŞ VE KABUL ETMİŞ SAYILIRSINIZ</p>
        <p>Eser sahibi YCŞ HOLDİNG, bu web sitesi ve içeriğinde bulunan tüm materyallerin telif hakkını elinde bulundurur. Bu içerikler, yazılar, görseller, grafikler, logolar, markalar, ses kayıtları, videolar, yazılımlar, kodlar, veri tabanları ve diğer her türlü sanatsal ve entelektüel materyaller dahil olmak üzere, Türkiye Cumhuriyeti'nin yasal düzenlemeleri ve uluslararası telif hakları anlaşmaları kapsamında korunmaktadır. Bu yasal düzenlemeler ve anlaşmalar, telif haklarını ve fikri mülkiyet haklarını düzenleyen ve eser sahiplerinin haklarını koruyan hükümleri içerir.</p>
<p></p>
<p id="baslik">## Türkiye'de Telif Hakları Uygulamaları##:</p>
<p></p>
<p>Türkiye Cumhuriyeti Fikir ve Sanat Eserleri Kanunu, eser sahiplerinin mali ve manevi haklarını koruyan temel yasal çerçevedir. Bu kanun, eserlerin izinsiz çoğaltılmasına, dağıtılmasına, değiştirilmesine, umuma iletilmesine ve yayılmasına karşı koruma sağlar. Eser sahipleri, eserlerinin izinsiz kullanımına karşı çeşitli haklara sahiptir ve bu haklar, izinsiz kullanım durumunda cezai ve hukuki sonuçlar doğurabilir.</p>
<p></p>
<p>Kanun, eser sahiplerinin haklarını doğrudan korur ve eser sahiplerine geniş yetkiler tanır. Eserin yaratıcısı, eser üzerinde tam hakka sahiptir ve bu haklar eser sahibinin izni olmadan kullanılamaz. Kanun, eserin izinsiz olarak çoğaltılması, yayılması, umuma iletilmesi veya eser üzerinde değişiklik yapılması gibi eylemleri yasaklar ve bu tür eylemlere karşı eser sahibini korur.</p>
<p></p>
<p>Kanunun 71. maddesi, eser sahibinin mülkiyet haklarına tecavüz edenlere ciddi cezai yaptırımlar öngörür ve bu tür tecavüzlere karşı hapis cezasını hükme bağlar. Aynı zamanda, 68. madde, eser sahibinin mali haklarının ihlali halinde zararını talep etme ve eserinin izinsiz kullanımına karşı tazminat talep etme hakkını korur. Bu maddeler, eser sahiplerinin haklarını etkin bir şekilde koruyarak, izinsiz kullanımın önüne geçer.</p>
<p></p>
<p>Türk Ceza Kanunu, telif hakkı ihlallerine karşı cezai yaptırımlar içerir. Özellikle 157. ve 158. maddeler, eserlerin izinsiz istimalini ve eser sahiplerinin haklarına karşı haksız fiilleri cezalandırır. Bu maddeler, telif haklarının izinsiz ihlalinin ciddi neticelerini tayin eder ve eser sahiplerinin haklarını koruma altına alır.</p>
<p></p>
<p>Sınai Mülkiyet Kanunu, fikri mülkiyet ve marka haklarını düzenleyen bir yasadır. Web sitesinde bulunan markaların, logoların ve tasarımların izinsiz kullanımı yasa dışıdır ve cezai yaptırımlara neden olabilir. Bu kanun, marka ve tasarım haklarının ihlaline karşı çeşitli önlemler ve cezalar öngörür. Eser sahiplerinin marka ve tasarım hakları, izinsiz kullanımın engellenmesi için yasal olarak güvence altına alınmıştır.</p>
<p></p>
<p>Türkiye'de telif haklarının uygulanması için özel kanunlar, tüzükler ve yönetmelikler mevcuttur. Bu düzenlemeler, fikri mülkiyet haklarının ve telif haklarının çeşitli alanlarda korunmasını ve düzenlenmesini sağlar. Eserlerin yaratıcısına geniş haklar tanırken, bu hakların belirli durumlarda kısıtlanabileceğini de belirtir. Eser sahiplerinin hakları, belirli durumlarda yasal düzenlemelerle sınırlanabilir.</p>
<p></p>
<p id="baslik">## Uluslararası Telif Hakları Uygulamaları##:</p>
<p></p>
<p>Türkiye, uluslararası telif haklarının korunması için çeşitli anlaşmalara taraf olmuştur. Bu anlaşmalar, telif haklarının milletlerarası düzeyde korunmasını sağlar ve üye ülkelerin telif haklarına ilişkin yasalarının uluslararası standartlara uygun olmasını garanti eder.</p>
<p></p>
<p>Bern Sözleşmesi, edebiyat ve sanat eserlerinin korunması için uluslararası bir anlaşmadır. Türkiye, bu sözleşmeye taraf olan ülkeler arasında yer almaktadır. Bern Sözleşmesi, eser sahiplerinin haklarını küresel ölçekte güvence altına alır ve eserlerin izinsiz çoğaltılması, yayılması veya umuma iletilmesi gibi eylemler için eser sahibinin iznini gerektirir.</p>
<p></p>
<p>TRIPS Anlaşması, Dünya Ticaret Örgütü'nün (WTO) bir anlaşması olup Türkiye de bu anlaşmaya taraftır. TRIPS Anlaşması, üye ülkelerin telif hakkı korumasını en az 50 yıl boyunca sağlamasını gerektirir ve bu korumayı üye ülkeler arasında milletlerarası standartlara uygun hale getirir.</p>
<p></p>
<p>WIPO Telif Hakları Anlaşması (WCT), dijital ortamda telif hakkı korumasını güçlendirmeyi hedefler. Bu anlaşma, internet ve dijital ortamda eser sahiplerinin haklarının daha iyi korunmasını amaçlar. Ayrıca, WIPO İcralar ve Fonogramlar Sözleşmesi (WPPT), icracı sanatçıların ve fonogram yapımcılarının haklarının korunmasını sağlar.</p>
<p></p>
<p>Roma Sözleşmesi, icracı sanatçıların, fonogram yapımcılarının ve yayıncı kuruluşlarının haklarının korunmasını temin eder. Türkiye, bu sözleşmeye de taraftır ve bu sözleşme kapsamında eser sahiplerinin ve sanatçıların hakları korunmaktadır.</p>
<p></p>
<p>Bu web sitesine erişim ve kullanım, kullanıcıların bu telif hakkı bildirimini ve web sitesinin kullanım şartlarını kabul ettiği anlamına gelir. Kullanıcılar, eser sahiplerinin mülkiyet haklarını ve yasal haklarını tanıyarak web sitesini kullanmayı kabul ederler.</p>
<p></p>
<p>YCŞ HOLDİNG, telif hakları ihlallerine karşı sıfır tolerans politikası benimser ve ihlallerin cezai ve hukuki sonuçlar doğurabileceğini belirtir. Telif hakları ihlallerine karşı yasal işlem başlatma hakkını saklı tutar. Bu adımlar, mahkeme kararları, ihtar mektupları veya diğer yasal girişimler yoluyla gerçekleştirilebilir. Kullanıcıların bu web sitesinde yer alan materyalleri izinsiz kullanmamaları önemlidir. İzinsiz kullanım, telif hakkı ihlaline ve yasal yaptırımlara yol açabilir.</p>
<p></p>
<p>Ayrıca, uluslararası düzeyde telif haklarının korunması, eser sahiplerine küresel ölçekte eserlerini güvence altına alma imkânı sunar. Türkiye'nin taraf olduğu bu sözleşmeler, eser sahiplerinin yararına birçok avantaj getirir ve eserlerin korunması için ek olanaklar sağlar. Eser sahipleri, uluslararası anlaşmaların sağladığı hakları etkin bir şekilde kullanarak, eserlerinin izinsiz çoğaltılmasına, dağıtılmasına veya umuma iletilmesine karşı korunabilir.</p>
<p></p>
<p>Sonuç olarak, kullanıcılar, bu web sitesinin telif haklarını ve fikri mülkiyet haklarını ciddiyetle ele almalı ve eserin izinsiz kullanımının telif hakkı ihlaline yol açabileceğini bilmelidir. İzinsiz kullanım, hem yerel hem de uluslararası düzeyde cezai ve hukuki yaptırımlarla karşılaşma riskini taşır. Dolayısıyla, eser sahiplerinin haklarını gözeterek ve web sitesinde yer alan içerikleri izinsiz kullanmaktan kaçınarak, hem yasaları ihlal etmemiş hem de eser sahiplerinin haklarına saygı göstermiş olursunuz.</p>
    </footer>
    <script>
        function sendSignal(command) {
            fetch('/api/assistant', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({ 'voice': command })
            });
        }
        document.getElementById('commandForm').addEventListener('submit', function(event) {
            event.preventDefault();
        });
    </script>
</body>
</html>







    """

def kill_process_after_delay(process, delay):
    def kill_process():
        try:
            process.kill()
        except Exception as e:
            print(str(e))
    threading.Timer(delay, kill_process).start()

@app.route('/api/assistant', methods=['POST'])
def process_voice_command():
    try:
        voice_command = request.form.get('voice', '')
        print("API'den gelen veri:", voice_command)  # Konsola veriyi yazdır
        if voice_command == 'derin_uyku':
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif voice_command == 'shutdown':
            os.system("shutdown -p")
        elif voice_command == 'sound':
            winsound.Beep(1500, 1500)
        if voice_command == 'eglence':
            
            os.system("mode con: cols=220 lines=60")
            
            curl_process = subprocess.Popen(["start", "cmd", "/c", "color a && curl ascii.live/can-you-hear-me"], shell=True)
            
            time.sleep(1)  
            cmd_window = gw.getWindowsWithTitle('cmd')[0]  
            cmd_window.maximize() 
            
            playsound('C:\\Users\\HP\\Desktop\\PCyonetim\\Never Gonna Give You Up.mp3') #BURAYI KENDİNİZE GÖRE DOLDURUN
            
            subprocess.Popen(["timeout", "/t", "212", "/nobreak", "&&", "taskkill", "/f", "/t", "/pid", str(curl_process.pid)], shell=True)
                
        return jsonify({"response": "Komut alındı: " + voice_command})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def print_date_info():
    
    
    locale.setlocale(locale.LC_TIME, 'tr_TR.UTF-8')
    
    
    now = datetime.now()
    
   
    day = now.day
    month = now.strftime('%B')
    weekday = now.strftime('%A')
    
    charge_level = sarz()

   
    baslangic = f"Merhaba, bugün {day} {month} {weekday} saat {now.strftime('%H:%M:%S')} , şarjınız {charge_level}% ve "
    
   
    hava_durumu = hava()  
    
    
    baslangic += hava_durumu
    
    
    print("APİ AKTİF")
    print(baslangic)
    speak(baslangic)


def loading_animation(duration=10, interval=0.4):
    
    start_time = time.time()
    
    
    while time.time() - start_time < duration:
        
        for i in range(1, 4):
            
            sys.stdout.write('\r' + '.' * i)
            sys.stdout.flush()
            
            
            time.sleep(interval)
            
        
        sys.stdout.write('\r' + ' ' * 3)
        sys.stdout.flush()
        
        
        sys.stdout.write('\r' + '.')
        sys.stdout.flush()
        time.sleep(interval)
def sarz():
   
    result = subprocess.run(
        ['WMIC', 'PATH', 'Win32_Battery', 'Get', 'EstimatedChargeRemaining'],
        capture_output=True,
        text=True
    )
    
   
    output = result.stdout.strip() 
    lines = output.split('\n')  
    
    
    for line in lines:
        line = line.strip()  
        
        
        if line.isdigit():  
            return line
    
   
    return None
def hava():
    parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|06420|SAKARYA|")
    parse = parse["entries"][0]["summary"]
    parse = parse.split()
    
    
    hava_durumu = f"{parse[2]} {parse[4]} {parse[5]}"
    
    
    return(hava_durumu)
def speak(text):
    
    tts = gTTS(text, lang='tr')
    filename = 'temp.mp3'
    tts.save(filename)
    playsound(filename)
    os.remove(filename)
def apiaciliyo():
    print("APİ BAŞLATILIYOR...")
def run_api():
    app.run(host='192.168.1.105', port=5000)

if __name__ == "__main__":
    apiaciliyo()
    loading_animation()
    print_date_info()
    api_thread = threading.Thread(target=run_api)
    api_thread.start()
    while api_running:
        pass
