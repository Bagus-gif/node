import sys
import subprocess

def install_required_packages():
    required_packages = ['requests', 'flask', 'colorama']
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"{Fore.YELLOW}🔄 Installing {package}...{Style.RESET_ALL}")
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package, '--break-system-packages'])
                print(f"{Fore.GREEN}✨ {package} installed successfully!{Style.RESET_ALL}")
            except subprocess.CalledProcessError as e:
                print(f"{Fore.RED}❌ Error installing {package}: {e}{Style.RESET_ALL}")
                sys.exit(1)

install_required_packages()

# Import packages after installation
import os
import time
import logging
import requests
import threading
from flask import Flask, request
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

# Flask app setup
app = Flask(__name__)
token_list = []

# Disable Flask logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def linex():
    print(f"{Fore.CYAN}⚡️ {Fore.WHITE}═══════════════════════════════════════════════════════════════{Fore.CYAN} ⚡️{Style.RESET_ALL}")

logo = f"""
{Fore.BLUE}    ███╗   ██╗ ██████╗ ██████╗ ███████╗██████╗  █████╗ ██╗   ██╗
{Fore.BLUE}    ████╗  ██║██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
{Fore.BLUE}    ██╔██╗ ██║██║   ██║██║  ██║█████╗  ██████╔╝███████║ ╚████╔╝ 
{Fore.BLUE}    ██║╚██╗██║██║   ██║██║  ██║██╔══╝  ██╔═══╝ ██╔══██║  ╚██╔╝  
{Fore.BLUE}    ██║ ╚████║╚██████╔╝██████╔╝███████╗██║     ██║  ██║   ██║   
{Fore.BLUE}    ╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝   ╚═╝   
{Fore.GREEN}    V/0.2 Token Generator
{Fore.CYAN}⚡️ {Fore.WHITE}═══════════════════════════════════════════════════════════════{Fore.CYAN} ⚡️{Style.RESET_ALL}
{Fore.YELLOW}    👨‍💻 Developer : Saifur Rahman Siam (github.com/nbprg)
    🛠️ Recoder : Umar Al Atsary
{Fore.CYAN}⚡️ {Fore.WHITE}═══════════════════════════════════════════════════════════════{Fore.CYAN} ⚡️{Style.RESET_ALL}"""

@app.route('/post')
def post_token():
    global token_list
    token = request.args.get('token')
    token_list.append(token)
    return 'successful'

@app.route('/get')
def get_token_route():
    global token_list
    if not str(len(token_list)) == "0":
       for get_one in token_list:
           token_list.remove(get_one)
           break
       return str(get_one)
    else:
       return 'None'

@app.route('/total')
def total():
    global token_list
    return f"{token_list} \n\nTotal: {str(len(token_list))} "

def run_flask():
    app.run(port=5000, host='localhost', debug=False)

def get_token():
    while True:
         res = requests.get('http://localhost:5000/get').text
         if not 'None' in res:
              print(f"\r\r{Fore.BLUE}🎯 {Fore.WHITE}Captcha token get successful{Style.RESET_ALL}")
              return res
         else:
              time.sleep(0.5)

def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls')
        print(logo)
    else:
        os.system('clear')
        print(logo)

def get_headers(auth_token=None):
     headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://app.nodepay.ai',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
            }
     if auth_token:
            headers['Authorization'] = f'Bearer {auth_token}'
            headers['origin'] = 'chrome-extension://lgmpfmgeabnnlemejacfljbmonaomfmm'
     return headers

def login_acccaunts(email, password, captcha_token):
   try:
       start_time = time.time()
       json_data = {
           'user': email,
           'password': password,
           'remember_me': True,
           'recaptcha_token': captcha_token
       }
       headers = get_headers()
       url = "https://api.nodepay.ai/api/auth/login"
       response = requests.post(url, headers=headers, json=json_data, timeout=5)
       response.raise_for_status()
       end_time = time.time()
       login_duration = end_time - start_time
       if login_duration < 60:
           print(f"\r\r{Fore.BLUE}⏱️ {Fore.WHITE}Login time: {login_duration:.2f}s{Style.RESET_ALL}")
       elif login_duration < 3600:
           print(f"\r\r{Fore.BLUE}⏱️ {Fore.WHITE}Login time: {login_duration/60:.2f}m{Style.RESET_ALL}")
       else:
           print(f"\r\r{Fore.BLUE}⏱️ {Fore.WHITE}Login time: {login_duration/3600:.2f}h{Style.RESET_ALL}")
       return response.json()
   except Exception as e:
       print(f"\r\r{Fore.RED}⚠️ Error: {str(e)}{Style.RESET_ALL}")
       linex()
       time.sleep(1)
       return None

def save_results(email, password, auth_token):
    with open('new_tokens.txt', 'a') as f:
        f.write(f"{str(auth_token)}\n")

def read_accounts():
    accounts = []
    try:
        with open('accounts.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if '|' not in line:
                    continue
                parts = line.split('|')
                if len(parts) >= 2:
                    email = parts[0]
                    password = parts[1]
                    accounts.append((email, password))
    except Exception as e:
        print(f"\r\r{Fore.RED}⚠️ Error reading accounts.txt: {str(e)}{Style.RESET_ALL}")
        exit()
    return accounts

def main():
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    time.sleep(2)
    
    clear_screen()
    accounts = read_accounts()
    success_count = 0
    total_attempts = 0
    
    print(f"\r\r{Fore.BLUE}📊 {Fore.WHITE}Total accounts loaded: {len(accounts)}{Style.RESET_ALL}")
    linex()
    
    for email, password in accounts:
        try:
            total_attempts += 1
            print(f"\r\r{Fore.BLUE}🔄 {Fore.WHITE}Processing account {total_attempts}/{len(accounts)}{Style.RESET_ALL}")
            
            captcha_token = get_token()
            response_data = login_acccaunts(email, password, captcha_token)
            
            if response_data and response_data.get('msg') == 'Success':
                auth_token = response_data['data']['token']
                success_count += 1
                print(f"\r\r{Fore.BLUE}✨ {Fore.GREEN}Successfully got new token ({success_count}/{len(accounts)}){Style.RESET_ALL}")
                save_results(email, password, auth_token)
            else:
                print(f"\r\r{Fore.RED}❌ Failed to get token{Style.RESET_ALL}")
            
            linex()
            time.sleep(1)
            
        except Exception as e:
            print(f"\r\r{Fore.RED}⚠️ Error: {str(e)}{Style.RESET_ALL}")
            linex()
            time.sleep(1)
    
    print(f"\r\r{Fore.BLUE}🎉 {Fore.GREEN}Process Completed!{Style.RESET_ALL}")
    print(f"\r\r{Fore.BLUE}📊 {Fore.WHITE}Final Statistics:{Style.RESET_ALL}")
    print(f"\r\r{Fore.BLUE}✅ {Fore.WHITE}Total Successful: {success_count}{Style.RESET_ALL}")
    print(f"\r\r{Fore.BLUE}🔄 {Fore.WHITE}Total Attempts: {total_attempts}{Style.RESET_ALL}")
    print(f"\r\r{Fore.BLUE}📈 {Fore.WHITE}Success Rate: {(success_count/total_attempts*100):.2f}%{Style.RESET_ALL}")
    print(f"\r\r{Fore.BLUE}💾 {Fore.WHITE}New tokens saved to new_tokens.txt{Style.RESET_ALL}")
    exit()

if __name__ == "__main__":
    main()