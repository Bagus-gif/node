"NODEPAY REF BOT"

	Step by step
1. noderef.py
	a. salin isi javascript.txt ke extension violentmonkey, create new > kosongkan > paste > sesuaikan port yg diminta oleh noderef.py > save
	```
	https://chromewebstore.google.confdagail/violentmonkey/jinjaccalgkegednnccohejagnlnfdag```
	atau jika menggunakan android, bisa gunakan via browser, pergi ke pengaturan > skrip > paste > sesuaikan port yg diminta oleh noderef.py > save 
	```
	https://play.google.com/store/apps/details?id=mark.via.gp```
	
	b. jika menggunakan browser selain via browser, gunakan tambahan extension untuk bypass cloudflare 
	```
	https://chromewebstore.google.com/detail/cloudfreed-cloudflare-sol/hjbjibnjdammlhgfidinkhghelcmenjd```
	
	c. jalankan noderef.py, lihat port berapa yg diminta, sesuaikan pada extension
		jika belum menginstal modul, maka dengan sendirinya akan menginstal
		```
		function sendTokenToAvailablePort(captchaValue, ports = [5000])```
		pada javascript sesuaikan port nya [5000]
		port biasanya mulai dari 5000 hingga 5010
	
	d. salin kode ref bukan linknya 
	e. hasil ref akan disimpan dalam accounts.txt dan token.txt
2. newtoken.py
	a. hanya menggunakan 1 port 5000 saja, jika terjadi tabrakan port, ubah manual didalam skrip newtoken.py
	b. input dari accounts.txt yg berformat :
		email|password
	c. output new_token.txt
	d. cara kerja sama dengan noderef.py
3. Browser
	a. buka https://app.nodepay.ai/login
	b. browser harus tetap terbuka saat proses noderef maupun newtoken
	c. pastikan sudah terinstal extension yg diminta diatas dan sudah memasukkan javascript di violentmonkey atau via skrip
	
Terimakasih 