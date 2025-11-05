# YouTube Downloader GUI

**Простой GUI-загрузчик видео/аудио с YouTube** на PyQt5.  
Вставь ссылку, выбери качество — скачай с прогрессом.


## Особенности
- Поддержка MP4/MP3
- Выбор качества (720p, 1080p, аудио)
- Прогресс-бар (QProgressBar)
- Сохранение в папку
- Многопоточная загрузка (QThread)

## Технологии
- Python 3
- `PyQt5` — GUI (QtWidgets, QtCore, QThread, QProgressBar)
- `yt_dlp` — скачивание
- `threading` — асинхронность
- `sys`, `os` — утилиты

## Установка и запуск

git clone https://github.com/l4svl/YTdownloader.git
cd YTdownloader
pip install PyQt5==5.15.9, yt-dlp==2024.10.22
python main.py
