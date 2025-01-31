# 🛍️ Store (Docker + Django + PostgreSQL)

Этот проект — **интернет-магазин**, в котором можно искать товары, добавлять их в корзину, регистрироваться и авторизоваться. Разработан с использованием **Django**, **PostgreSQL** и **Docker**.

## 🚀 Функционал  

✅ **Поиск товаров** — фильтр по категориям, названию и цене  
✅ **Добавление в корзину** — удобное управление покупками  
✅ **Регистрация и авторизация** — вход через email и пароль  
✅ **Управление корзиной** — добавление и удаление товаров  
✅ **Хранение данных в PostgreSQL**  

## 📦 Технологии  

- **Django** — бэкенд на Python  
- **PostgreSQL** — база данных  
- **Docker & Docker Compose** — контейнеризация
  

## 🛠 Установка и запуск  

 **Клонируйте репозиторий**  


```
git clone https://github.com/Shoma0XCC/docker.git
```

 **Установите Docker Desktop**


```
https://www.docker.com/products/docker-desktop/
```


## 🏗 Setup
**Создайте виртуальное окружение**

🖥️ macOS / Linux


```
python3 -m venv venv
source venv/bin/activate

```

🖥️ Windows


```
python3 -m venv venv
.\venv\Scripts\activate.bat
```


**Установите зависимости**

```
pip install --upgrade pip
pip install -r requirements.txt
```

**Сделайте миграцию базы данных и создайте администратора**

```
python manage.py migrate
python manage.py createsuperuser
```


**Соберите Docker-контейнеры**

```
docker compose build
```

Запустите проект в Docker в фоновом режиме

```
docker compose up -d 
```


## 🛍️ **Использование**
**После установки можно:**

- Перейти в каталог товаров
- Использовать фильтр для поиска нужного товара
- Добавлять товары в корзину
- Авторизироваться или зарегистрироваться
- Удалять или добавлять товары в корзину

## 🔗 **Доступ к проекту:**
- Главная страница: http://localhost:8000
- Админ-панель: http://localhost:8000/admin/
  
## 📝 **Разработчик**
👤 **Shoma0XCC**

🔗 GitHub: [Shoma0XCC](https://github.com/Shoma0XCC)
