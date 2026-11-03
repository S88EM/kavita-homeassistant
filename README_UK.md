<p align="center">
  <img src="kavita/logo.png" alt="Логотип Kavita" width="120" />
</p>

# 📖 Репозиторій додатку Kavita для Home Assistant

<p align="center">
  <strong><a href="README.md">English</a></strong> | <strong><a href="README_UK.md">Українська</a></strong>
</p>

<p align="center">
  <a href="https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FS88EM%2Fkavita-homeassistant">
    <img src="https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg" alt="Відкрити Home Assistant та додати репозиторій" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/arch-aarch64%20%7C%20amd64%20%7C%20armv7-blue" alt="Підтримувані архітектури" />
  <img src="https://img.shields.io/badge/version-0.9.1.4-blue" alt="Версія додатку" />
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="Ліцензія" />
</p>

Цей репозиторій додає сервер цифрової бібліотеки **[Kavita](https://www.kavitareader.com)** як рідний додаток (Add-on) для **Home Assistant OS / Supervised** (Raspberry Pi 4/5, x86/ARM міні-ПК та віртуальні машини).

**Kavita** — це швидка, красива та автономна цифрова бібліотека, створена для читання манґи, вебтунів, коміксів та електронних книг.

---

## ✨ Особливості

* 🔒 **Постійне збереження бази даних:** База даних SQLite (`app.db`), закладки, прогрес читання та кеш обкладинок надійно зберігаються у персистентному розділі `/data/config` і не видаляються при оновленнях додатку.
* 📂 **Прямий доступ через Samba:** Заздалегідь підготовлені каталоги для завантаження книг через локальну мережу (`\\homeassistant.local\share\kavita\`).
* 📱 **Вбудований OPDS-сервер:** Повна сумісність із мобільними читалками для Android та iOS (Mihon / Tachiyomi, Panels, Chunky, Moon+ Reader, Paperback тощо).
* ⚡ **Мультиплатформність:** Підтримка архітектур `aarch64` (64-бітний ARM, наприклад Raspberry Pi 4/5), `amd64` (Intel/AMD) та `armv7`.
* 🌐 **Підтримка зворотних проксі та SSL:** Працює як у локальній мережі, так і через захищені хмарні тунелі (KeenDNS, Cloudflare Tunnel, NGINX Proxy Manager тощо).

---

## 🚀 Встановлення

### Варіант 1: Швидке встановлення в один клік
Натисніть кнопку нижче, щоб відкрити ваш Home Assistant та автоматично додати цей репозиторій:

[![Відкрити Home Assistant та додати репозиторій](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FS88EM%2Fkavita-homeassistant)

### Варіант 2: Встановлення вручну
1. У Home Assistant відкрийте: **Налаштування** → **Додатки** → **Магазин додатків**.
2. У правому верхньому кутку натисніть **три крапки** → **Репозиторії** (*Repositories*).
3. Додайте посилання на репозиторій:
   ```text
   https://github.com/S88EM/kavita-homeassistant
   ```
4. Натисніть **Додати**, закрийте вікно та оновіть сторінку магазину додатків.
5. Знайдіть **Kavita** у списку, натисніть **Встановити** (*Install*) і після завершення натисніть **Запустити** (*Start*).

---

## 📚 Додавання книг і манґи

Файли книг можна копіювати зі свого комп'ютера безпосередньо через мережевий диск Home Assistant (Samba Share):

| Тип контенту | Мережева папка Samba | Шлях усередині Kavita |
| :--- | :--- | :--- |
| **Книги (EPUB, PDF)** | `\\homeassistant.local\share\kavita\books` | `/books` |
| **Манґа (CBZ, CBR, ZIP)** | `\\homeassistant.local\share\kavita\manga` | `/manga` |
| **Комікси (CBZ, CBR, PDF)** | `\\homeassistant.local\share\kavita\comics` | `/comics` |
| **Будь-які інші медіа** | `\\homeassistant.local\media` | `/media` |

### Створення бібліотеки у Kavita:
1. Відкрийте вебінтерфейс Kavita на порту `5000` (або натисніть кнопку **Відкрити веб-інтерфейс** на сторінці додатку в ХА).
2. Створіть обліковий запис адміністратора.
3. Перейдіть у меню **Server Settings** → **Libraries** → **Add Library**.
4. Виберіть тип бібліотеки та вкажіть шлях: `/books`, `/manga` або `/comics`.
5. Натисніть **Save** для початку сканування файлів.

---

## 📱 Мобільні читалки (OPDS)

Kavita підтримує протокол OPDS для перегляду та завантаження книг прямо у мобільні додатки:

* **Android:** [Mihon](https://mihon.app/) (з розширенням Kavita), Moon+ Reader, Kuro Reader, CDisplayEx.
* **iOS:** Panels, Chunky Comic Reader, Paperback.

Персональне посилання OPDS та ключ доступу можна отримати в Kavita:  
**User Settings** → **3rd Party Clients** / **Auth Keys**.

---

## ⚙️ Налаштування

Параметри додатку можна змінити у вкладці **Конфігурація** в Home Assistant:

```yaml
timezone: "UTC" # Вкажіть ваш часовий пояс (наприклад Europe/Kyiv)
```

---

## 📁 Структура репозиторію

```text
├── kavita/             # Каталог додатку
│   ├── config.yaml     # Маніфест додатку Home Assistant
│   ├── build.yaml      # Архітектури та образ jvmilazz0/kavita
│   ├── Dockerfile      # Контейнеризація
│   ├── run.sh          # Ініціалізація та персистентне сховище
│   ├── DOCS.md         # Документація у вкладці додатку в ХА
│   ├── CHANGELOG.md    # Історія версій
│   ├── icon.png        # Іконка
│   └── logo.png        # Логотип
├── repository.yaml     # Маніфест репозиторію для Supervisor
├── LICENSE             # Ліцензія MIT
├── README.md           # Документація англійською
└── README_UK.md        # Документація українською
```

---

## 📄 Ліцензія

Цей проєкт поширюється за ліцензією [MIT](LICENSE).  
Сервер Kavita розробляється командою [Kareadita](https://github.com/Kareadita/Kavita) і поширюється за ліцензією GPL-3.0.
