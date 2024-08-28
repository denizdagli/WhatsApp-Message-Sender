# WhatsApp Message Sender

Bu proje, Selenium ve Python kullanarak WhatsApp'a mesaj göndermek için bir otomasyon aracıdır. `contact.csv` dosyasındaki telefon numaralarına ve mesajlara göre WhatsApp üzerinden mesaj gönderir.

## Gereksinimler

- Python 3.x
- Selenium
- Google Chrome ve ChromeDriver

## Kurulum

* Python ve gerekli kütüphaneleri yükleyin:

   ```pip3 install selenium ```(mac)
   ```pip install selenium ```(windows)

* Bu projedeki whatsapp_sender.py selenium script dosyasını indirin.

* contact.csv adlı dosyaya aşağıdaki formatta telefon numaraları ve mesajlar ekleyin:
```90536*******, test message```

## Kullanım

* Selenium scriptini çalıştırın:

```python3 whatsapp_sender.py```(mac)
```python whatsapp_sender.py```(windows)

* WhatsApp Web'e giriş yapın: Script çalıştırıldığında, WhatsApp Web sayfası açılır. QR kodunu tarayarak WhatsApp hesabınıza giriş yapın. Giriş yaptıktan sonra script, contact.csv dosyasındaki her bir telefon numarasına belirtilen mesajı gönderecektir.

## Dikkat Edilmesi Gerekenler
* WhatsApp Web'e giriş yapmanız gerektiği için scripti ilk çalıştırmada 10 saniye bekler. QR kodunu tarayarak giriş yapmalısınız.
* Bu scripti yalnızca izin verilen ve etik olan durumlarda kullanmalısınız.
