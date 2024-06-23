#  Автотесты для сайта [finam.ru](https://www.finam.ru)

## Описание проекта

**Список реализованных решений:**
- Разработаны 5 UI-автотестов  
- Подключены отчеты Allure Report  
- Настроена сборка проекта в Jenkins  
- Настроен запуск автотестов в Selenoid
- Уведомления в Telegram с результатами тестов

**Список автотестов:**
- Проверка раздела "Инвестиции"
- Проверка раздела "Премиум"     
- Проверка раздела "Обучение"  
- Проверка раздела "Программа лояльности"   
- Проверка раздела "Календарь IPO"   

**Используемый стэк**  
<p align="center">
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" height="40" width="40" />
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg" height="40" width="40" />
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="40" width="40" />
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" height="40" width="40" />
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original-wordmark.svg" height="40" width="40" />

---
## Описание запуска тестов в Jenkins  

**Cкрипт для установки виртуального окружения и запуска тестов которые используют requirements.txt**  
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```
---
**Команда для скачивания jar-файла с библиотекой если она не имеется в проекте**
```
cd ..
FILE=allure-notifications-4.6.1.jar
if [ ! -f "$FILE" ]; then
   wget https://github.com/qa-guru/allure-notifications/releases/download/4.6.1/allure-notifications-4.6.1.jar
fi
```
---
**Команда для считывания файла и отправки уведомления**
```
java "-DconfigFile=notifications/config.json" -jar ../allure-notifications-4.6.1.jar
```
---

## Пример запуска автотестов в Jenkins  

**Запускаем сборку в Jenkins**
<img align="center" src="![image](https://github.com/Ivan-Ne/finam/assets/74492605/c7434cec-e875-4191-b3c3-56eb3f1b2ea8)"/>  

**Отчет о запусках автотестов в Allure**
<img align="center" src="![image](https://github.com/Ivan-Ne/finam/assets/74492605/4da4f2e6-d3c4-44d2-8926-069546da08b1)"/>  

**Сообщение в Telegram** 
<img align="center" src="![image](https://github.com/Ivan-Ne/finam/assets/74492605/c5ea9d2f-e258-45dc-96e7-4dadc5277955)"/>  
