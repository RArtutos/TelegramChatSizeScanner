# TelegramChatSizeScanner

TelegramChatSizeScanner es un bot de Telegram desarrollado en Python que escanea y analiza el tamaño de los mensajes y archivos en un chat de Telegram, ya sea un grupo o un canal. Proporciona un conteo detallado del número de caracteres y el tamaño de los archivos, mostrando el progreso en tiempo real.

## Requisitos

- Python 3.7+
- Telethon
- tqdm

## Instalación

1. Clona este repositorio:
   git clone https://github.com/RArtutos/TelegramChatSizeScanner.git
   cd TelegramChatSizeScanner
   
3. Instala dependencias
   pip install -r requirements.txt

4. Edita el archivo config.py
   api_id = 'YOUR_API_ID'
   api_hash = 'YOUR_API_HASH'
   phone_number = 'YOUR_PHONE_NUMBER'
   chat_id =   # Reemplaza con tu chat_id
   request_delay = .02  # Retraso entre peticiones en segundos

## Uso
Ejecuta el archivo main.py
python main.py

## Contribuciones
¡Las contribuciones son bienvenidas! Si tienes alguna mejora o corrección, por favor abre un issue o envía un pull request.


MIT License

Copyright (c) 2024 RArtutos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
