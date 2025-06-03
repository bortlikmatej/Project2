# 🚴‍♂️ Bike Project – Django aplikace

Tento repozitář obsahuje jednoduchý konfigurační web pro stavbu kol pomocí Django. Níže najdeš návod, jak projekt spustit lokálně.

---

## 🔧 Jak spustit projekt lokálně

V cmd udělejte tyhle kroky:

### 1. Naklonování repozitáře
```bash
git clone https://github.com/VojtaR2/bike-project.git
cd bike-project
```

### 2. Nainstaluj virtualní prostředí
``` bash
python -m venv venv
venv\Scripts\activate

```
### 3. Instalace requirements.txt
``` bash
pip install -r requirements.txt
```
### 4. Migrace databáze
``` bash
python manage.py migrate
```
5. Spuštění webového serveru
   
``` bash
python manage.py runserver
```

Project by Bortlík, Rašťák, Večerka
