# Kavita for Home Assistant

**Kavita** is a fast, self-hosted digital library designed for manga, comics, webtoons, and ebooks with a clean Web UI and a built-in OPDS server.

---

## 🚀 Quick Start / Швидкий старт

1. Go to Home Assistant: **Settings** → **Add-ons** → **Add-on Store**.
2. Click **Start** on the Kavita add-on.
3. Turn on **Start on boot** and **Watchdog**.
4. Open the interface by clicking **Open Web UI** or visiting:  
   👉 `http://homeassistant.local:5000` (or your Home Assistant IP).

---

## 📚 Adding Books & Manga / Додавання книг

Drop your books, manga, and comics directly via **Samba Share**:

- `\\homeassistant.local\share\kavita\books` (mapped to `/books` in Kavita)
- `\\homeassistant.local\share\kavita\manga` (mapped to `/manga` in Kavita)
- `\\homeassistant.local\share\kavita\comics` (mapped to `/comics` in Kavita)
- or any custom folder in `\\homeassistant.local\media`

### Library Setup in Kavita:
1. Register your initial admin account on first launch.
2. Navigate to **Server Settings** → **Libraries** → **Add Library**.
3. Select your library type (Manga, Comic, or Book).
4. Enter one of the pre-mapped paths:
   - `/books` (or `/share/kavita/books`)
   - `/manga` (or `/share/kavita/manga`)
   - `/comics` (or `/share/kavita/comics`)
5. Click **Save** and start scanning!

---

## 📱 Mobile Readers (OPDS) / Мобільні читалки

Connect your favorite mobile reading apps via OPDS:
- **Android:** Mihon / Tachiyomi, Moon+ Reader, Kuro Reader, CDisplayEx.
- **iOS:** Panels, Chunky Comic Reader, Paperback.

Your personal OPDS URL and API key can be found in Kavita:  
**User Settings** → **3rd Party Clients** / **Auth Keys**.

---

## 🌐 Home Assistant Sidebar Panel / Бічна панель

To embed Kavita into your Home Assistant sidebar, add the following to your `configuration.yaml`:

```yaml
panel_iframe:
  kavita:
    title: "Kavita"
    icon: "mdi:book-open-page-variant"
    url: "http://homeassistant.local:5000"
```
