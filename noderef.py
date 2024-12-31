import sysimport subprocessdef install_required_packages():    required_packages = ['requests', 'flask', 'colorama']        for package in required_packages:        try:            __import__(package)        except ImportError:            print(f"🔄 Installing {package}...")            try:                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package, '--break-system-packages'])                print(f"✨ {package} installed successfully!")            except subprocess.CalledProcessError as e:                print(f"❌ Error installing {package}: {e}")                sys.exit(1)install_required_packages()import osimport timeimport signalimport socketimport stringimport randomimport loggingimport requestsimport datetimeimport threadingfrom flask import Flask, requestfrom werkzeug.serving import run_simplefrom colorama import init, Fore, Back, Style# Initialize coloramainit(autoreset=True)# Flask app setupapp = Flask(__name__)token_list = []# Disable Flask logginglog = logging.getLogger('werkzeug')log.setLevel(logging.ERROR)def find_available_port():    port = 5000    while True:        try:            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:                s.bind(('localhost', port))                return port        except OSError:            port += 1            if port > 5010:  # batas maksimal port                print(f"{Fore.RED}❌ No available ports found between 5000-5010{Style.RESET_ALL}")                sys.exit(1)@app.route('/post')def post_token():    global token_list    token = request.args.get('token')    if token not in token_list:        token_list.append(token)        return 'successful'    else:        return 'token_used'@app.route('/get')def get_token_route():    global token_list    if not str(len(token_list)) == "0":       for get_one in token_list:           token_list.remove(get_one)           break       return str(get_one)    else:       return 'None'@app.route('/total')def total():    global token_list    return f"{token_list} \n\nTotal: {str(len(token_list))} "@app.route('/shutdown', methods=['POST'])def shutdown():    func = request.environ.get('werkzeug.server.shutdown')    if func is None:        raise RuntimeError('Not running with the Werkzeug Server')    func()    return 'Server shutting down...'def run_flask(port):    app.run(port=port, host='localhost', debug=False)def get_token(port):    while True:        try:            res = requests.get(f'http://localhost:{port}/get').text            if not 'None' in res:                return res            else:                time.sleep(0.5)        except requests.exceptions.ConnectionError:            print(f"\r\r{Fore.RED}⚠️ Connection error, retrying...{Style.RESET_ALL}")            time.sleep(1)def shutdown_flask(port):    try:        requests.post(f'http://localhost:{port}/shutdown')        print(f"\r\r{Fore.YELLOW}⚠️ Flask server on port {port} is shutting down...{Style.RESET_ALL}")        time.sleep(1)        print(f"\r\r{Fore.GREEN}✅ Flask server successfully closed{Style.RESET_ALL}")        linex()    except:        print(f"\r\r{Fore.RED}❌ Failed to shutdown Flask server{Style.RESET_ALL}")        linex()logo = f"""{Fore.BLUE}    ███╗   ██╗ ██████╗ ██████╗ ███████╗██████╗  █████╗ ██╗   ██╗{Fore.BLUE}    ████╗  ██║██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝{Fore.BLUE}    ██╔██╗ ██║██║   ██║██║  ██║█████╗  ██████╔╝███████║ ╚████╔╝ {Fore.BLUE}    ██║╚██╗██║██║   ██║██║  ██║██╔══╝  ██╔═══╝ ██╔══██║  ╚██╔╝  {Fore.BLUE}    ██║ ╚████║╚██████╔╝██████╔╝███████╗██║     ██║  ██║   ██║   {Fore.BLUE}    ╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝   ╚═╝   {Fore.GREEN}V/0.1{Fore.CYAN}⚡️ {Fore.WHITE}═══════════════════════════════════════════════════════════════{Fore.CYAN} ⚡️{Style.RESET_ALL}{Fore.YELLOW}    💻 Developer : Saifur Rahman Siam (github.com/nbprg)    🛠️ Recoder   : Umar Al Atsary{Fore.CYAN}⚡️ {Fore.WHITE}═══════════════════════════════════════════════════════════════{Fore.CYAN} ⚡️{Style.RESET_ALL}"""def linex():    print(f"{Fore.CYAN}⚡️ {Fore.WHITE}═══════════════════════════════════════════════════════════════{Fore.CYAN} ⚡️{Style.RESET_ALL}")def get_headers(auth_token=None):    headers = {        'accept': '*/*',        'accept-language': 'en-US,en;q=0.9',        'content-type': 'application/json',        'origin': 'https://app.nodepay.ai',        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'    }    if auth_token:        headers['Authorization'] = f'Bearer {auth_token}'        headers['origin'] = 'chrome-extension://lgmpfmgeabnnlemejacfljbmonaomfmm'    return headersdef generate_username():    vowels = 'aeiou'    consonants = 'bcdfghjklmnpqrstvwxyz'        def create_syllable():        patterns = [            lambda: random.choice(consonants) + random.choice(vowels),            lambda: random.choice(consonants) + random.choice(vowels) + random.choice(vowels),            lambda: random.choice(consonants) + random.choice(vowels) + random.choice(consonants)        ]        return random.choice(patterns)()    # Generate base username (5-10 huruf)    base_length = random.randint(2, 4)  # Jumlah suku kata    username = ''    for _ in range(base_length):        username += create_syllable()        # Tambahkan angka (0-4 digit)    num_digits = random.randint(0, 4)    if num_digits > 0:        username += ''.join(random.choice(string.digits) for _ in range(num_digits))        # Pastikan panjang total 8-12 karakter    while len(username) < 8:        username += create_syllable()    if len(username) > 12:        username = username[:12]        return username.lower()    def reg_account(email, password, username, ref_code, captcha_token=None):    try:        start_time = time.time()        register_data = {            'email': email,            'password': password,            'username': username,            'referral_code': ref_code,            'recaptcha_token': captcha_token        }        headers = get_headers()        url = "https://api.nodepay.ai/api/auth/register"        response = requests.post(url, headers=headers, json=register_data, timeout=5)        response.raise_for_status()        end_time = time.time()        reg_duration = end_time - start_time        if reg_duration < 60:            print(f"\r\r{Fore.BLUE}⏱️ {Fore.WHITE}Account creation time: {reg_duration:.2f}s{Style.RESET_ALL}")        elif reg_duration < 3600:            print(f"\r\r{Fore.BLUE}⏱️ {Fore.WHITE}Account creation time: {reg_duration/60:.2f}m{Style.RESET_ALL}")        else:            print(f"\r\r{Fore.BLUE}⏱️ {Fore.WHITE}Account creation time: {reg_duration/3600:.2f}h{Style.RESET_ALL}")        return response.json()    except Exception as e:        print(f"\r\r{Fore.RED}⚠️ Error: {str(e)}{Style.RESET_ALL}")        linex()        time.sleep(1)        return Nonedef login_accounts(email, password, captcha_token):    try:        start_time = time.time()        json_data = {            'user': email,            'password': password,            'remember_me': True,            'recaptcha_token': captcha_token        }        headers = get_headers()        url = "https://api.nodepay.ai/api/auth/login"        response = requests.post(url, headers=headers, json=json_data, timeout=5)        response.raise_for_status()        end_time = time.time()        login_duration = end_time - start_time        if login_duration < 60:            print(f"\r\r{Fore.BLUE}⏱️ {Fore.WHITE}Account login time: {login_duration:.2f}s{Style.RESET_ALL}")        elif login_duration < 3600:            print(f"\r\r{Fore.BLUE}⏱️ {Fore.WHITE}Account login time: {login_duration/60:.2f}m{Style.RESET_ALL}")        else:            print(f"\r\r{Fore.BLUE}⏱️ {Fore.WHITE}Account login time: {login_duration/3600:.2f}h{Style.RESET_ALL}")        return response.json()    except Exception as e:        print(f"\r\r{Fore.RED}⚠️ Error: {str(e)}{Style.RESET_ALL}")        linex()        time.sleep(1)        return Nonedef active_recent_account(auth_token):    try:        start_time = time.time()        json_data = {}        url = "https://api.nodepay.ai/api/auth/active-account"        headers = get_headers(auth_token)        response = requests.post(url, headers=headers, json=json_data, timeout=5)        response.raise_for_status()        if not response.json()['msg'] == 'Success':            response = requests.post(url, headers=headers, json=json_data, timeout=5)        if not response.json()['msg'] == 'Success':            response = requests.post(url, headers=headers, json=json_data, timeout=5)        end_time = time.time()        activate_duration = end_time - start_time        if activate_duration < 60:            print(f"\r\r{Fore.BLUE}⏱️ {Fore.WHITE}Account activation time: {activate_duration:.2f}s{Style.RESET_ALL}")        elif activate_duration < 3600:            print(f"\r\r{Fore.BLUE}⏱️ {Fore.WHITE}Account activation time: {activate_duration/60:.2f}m{Style.RESET_ALL}")        else:            print(f"\r\r{Fore.BLUE}⏱️ {Fore.WHITE}Account activation time: {activate_duration/3600:.2f}h{Style.RESET_ALL}")        return response.json()    except Exception as e:        print(f"\r\r{Fore.RED}⚠️ Error: {str(e)}{Style.RESET_ALL}")        linex()        time.sleep(1)        return Nonedef save_results(email, password, auth_token, ref_code):    current_time = time.strftime("%d/%m/%Y %H:%M:%S")    expiry_date = (datetime.datetime.now() + datetime.timedelta(days=14)).strftime("%d/%m/%Y")        # Cek apakah file sudah ada dan kosong    file_exists = os.path.exists('accounts.txt')    file_empty = not file_exists or os.path.getsize('accounts.txt') == 0        with open('accounts.txt', 'r+' if file_exists else 'w+') as f:        # Baca semua konten file        content = f.read()                # Jika file kosong atau ref_code baru berbeda dari yang terakhir        if file_empty or f"Referral Code: {ref_code}\n" not in content:            # Jika file tidak kosong, tambahkan baris kosong sebagai pemisah            if not file_empty:                f.write("\n\n")                        # Tulis header baru            f.seek(0, 2)  # Pindah ke akhir file            f.write(f"Referral Code: {ref_code}\n")            f.write(f"Created Date: {current_time}\n")            f.write(f"Token Expiry Date: {expiry_date}\n")                # Selalu tambahkan data akun baru        f.seek(0, 2)  # Pindah ke akhir file        f.write(f"{email}|{password}|{auth_token}\n")        # Simpan token secara terpisah    with open('token.txt', 'a') as f:        f.write(f"{auth_token}\n")def clear_screen():    if sys.platform.startswith('win'):        os.system('cls')        print(logo)    else:        os.system('clear')        print(logo)def main():    install_required_packages()    port = find_available_port()    print(f"{Fore.GREEN}🚀 Running on port {port}{Style.RESET_ALL}")        with open('current_port.txt', 'w') as f:        f.write(str(port))        try:        flask_thread = threading.Thread(target=lambda: run_flask(port), daemon=True)        flask_thread.start()        time.sleep(2)                def signal_handler(signum, frame):            print(f"\n{Fore.YELLOW}⚠️ Program interrupted, cleaning up...{Style.RESET_ALL}")            shutdown_flask(port)            if os.path.exists('current_port.txt'):                os.remove('current_port.txt')                print(f"{Fore.GREEN}✅ Removed port configuration file{Style.RESET_ALL}")            linex()            sys.exit(0)                signal.signal(signal.SIGINT, signal_handler)        signal.signal(signal.SIGTERM, signal_handler)                clear_screen()        try:            target_success = int(input(f"{Fore.BLUE}🎯 {Fore.WHITE}Target Successful Referrals: {Style.RESET_ALL}"))        except:            print(f"{Fore.YELLOW}⚠️ Input Wrong Default Target is 100{Style.RESET_ALL}")            target_success = 100            time.sleep(1)        ref_code = input(f"{Fore.BLUE}🔑 {Fore.WHITE}Input referral code: {Style.RESET_ALL}")        clear_screen()        success_crt = 0        total_attempts = 0                while success_crt < target_success:            try:                total_attempts += 1                print(f"\r\r{Fore.BLUE}📊 {Fore.WHITE}Progress: {success_crt}/{target_success} successful ({(success_crt/target_success*100):.2f}%) | Total attempts: {total_attempts}{Style.RESET_ALL}")                                username = generate_username()                domains = ["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com"]                email = f"{username}{random.choice(domains)}"                password = str(''.join(random.choice(string.ascii_letters) for _ in range(6)) + 'Rc3@' + ''.join(random.choice(string.digits) for _ in range(3)))                                captcha_token = get_token(port)                response_data = reg_account(email, password, username, ref_code, captcha_token)                                if response_data and response_data.get('msg') == 'Success':                    print(f"\r\r{Fore.BLUE}🎯 {Fore.GREEN}Account Create Successful{Style.RESET_ALL}")                    captcha_token = get_token(port)                    response_data = login_accounts(email, password, captcha_token)                                        if response_data and response_data.get('msg') == 'Success':                        print(f"\r\r{Fore.BLUE}🎯 {Fore.GREEN}Account Login Successful{Style.RESET_ALL}")                        auth_token = response_data['data']['token']                        response_data = active_recent_account(auth_token)                                                if response_data and response_data.get('msg') == 'Success':                            success_crt += 1                            print(f"\r\r{Fore.BLUE}🎯 {Fore.GREEN}Successfully Referral Done ({success_crt}/{target_success}){Style.RESET_ALL}")                            save_results(email, password, auth_token, ref_code)                            print(f"\r\r{Fore.BLUE}📈 {Fore.WHITE}Success Rate: {(success_crt/total_attempts*100):.2f}%{Style.RESET_ALL}")                        else:                            print(f"\r\r{Fore.RED}🌲 Referral Error, Not Success{Style.RESET_ALL}")                            continue                    else:                        print(f"\r\r{Fore.RED}🌲 Account Login Failed{Style.RESET_ALL}")                        continue                else:                    print(f"\r\r{Fore.RED}🌲 Account Create Failed{Style.RESET_ALL}")                    continue                linex()                time.sleep(1)            except Exception as e:                print(f"\r\r{Fore.RED}⚠️ Error: {str(e)}{Style.RESET_ALL}")                linex()                time.sleep(1)        print(f"\r\r{Fore.BLUE}🎉 {Fore.GREEN}Target Completed!{Style.RESET_ALL}")        print(f"\r\r{Fore.BLUE}📊 {Fore.WHITE}Final Statistics:{Style.RESET_ALL}")        print(f"\r\r{Fore.BLUE}✅ {Fore.WHITE}Total Successful: {success_crt}{Style.RESET_ALL}")        print(f"\r\r{Fore.BLUE}🔄 {Fore.WHITE}Total Attempts: {total_attempts}{Style.RESET_ALL}")        print(f"\r\r{Fore.BLUE}📈 {Fore.WHITE}Success Rate: {(success_crt/total_attempts*100):.2f}%{Style.RESET_ALL}")        print(f"\r\r{Fore.BLUE}💾 {Fore.WHITE}Results saved to accounts.txt and token.txt{Style.RESET_ALL}")        linex()    finally:        shutdown_flask(port)        if os.path.exists('current_port.txt'):            os.remove('current_port.txt')            print(f"{Fore.GREEN}✅ Removed port configuration file{Style.RESET_ALL}")        linex()        print(f"{Fore.GREEN}👋 Program terminated successfully{Style.RESET_ALL}")        linex()if __name__ == "__main__":    main()