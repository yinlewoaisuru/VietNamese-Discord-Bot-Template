<div align="center">

# ˚₊‧ **VietNamese Discord Bot** ‧₊˚

### A modular Discord Bot template built with Python & discord.py

<br>

<a href="https://github.com/nguyenphanno/VietNamese-Discord-Bot-Template">
  <img src="https://img.shields.io/github/stars/nguyenphanno/VietNamese-Discord-Bot-Template?style=for-the-badge&label=STARS&labelColor=ffffff&color=8b5cf6&logo=github&logoColor=18181b" alt="Stars">
</a>
<a href="https://github.com/nguyenphanno/VietNamese-Discord-Bot-Template/network/members">
  <img src="https://img.shields.io/github/forks/nguyenphanno/VietNamese-Discord-Bot-Template?style=for-the-badge&label=FORKS&labelColor=ffffff&color=a78bfa&logo=github&logoColor=18181b" alt="Forks">
</a>
<a href="https://github.com/nguyenphanno/VietNamese-Discord-Bot-Template/issues">
  <img src="https://img.shields.io/github/issues/nguyenphanno/VietNamese-Discord-Bot-Template?style=for-the-badge&label=ISSUES&labelColor=ffffff&color=c4b5fd&logo=github&logoColor=18181b" alt="Issues">
</a>

<br>

<img src="https://img.shields.io/badge/Python-3.10%2B-ffffff?style=for-the-badge&logo=python&logoColor=3776AB&labelColor=ffffff" alt="Python">
<img src="https://img.shields.io/badge/discord.py-2.x-ffffff?style=for-the-badge&logo=discord&logoColor=5865F2&labelColor=ffffff" alt="discord.py">

<br><br>

<a href="https://discord.gg/fccfwHzms8">
  <img src="https://img.shields.io/badge/Join%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord">
</a>
<a href="https://github.com/nguyenphanno/VietNamese-Discord-Bot-Template/issues">
  <img src="https://img.shields.io/badge/Report%20an%20Issue-18181B?style=for-the-badge&logo=github&logoColor=white" alt="Issues">
</a>

<br><br>

> **Gọn gàng · Modular · Dễ mở rộng · Tự động load Cogs**

</div>

---

## 01 · Overview

**VietNamese Discord Bot** là một template Discord Bot được xây dựng bằng **Python + discord.py**, được thiết kế để trở thành nền tảng khởi đầu cho những project Discord Bot mới.

Thay vì đặt toàn bộ logic trong một file duy nhất, project sử dụng kiến trúc **Services / Commands / Events**, giúp source dễ đọc, dễ bảo trì và dễ mở rộng.

### Project Information

| Component              | Details                           |
| :--------------------- | :-------------------------------- |
| **Language**           | Python 3.10+                      |
| **Framework**          | discord.py 2.x                    |
| **Command System**     | Prefix + Slash Commands           |
| **Architecture**       | Modular / Cog-based               |
| **Auto Loader**        | Automatic `.py` Cog loading       |
| **Configuration**      | `Setting/Config.json`             |
| **Entry Point**        | `main.py`                         |
| **Security**           | Ghost Ping Detection + Lockdown   |
| **Command Categories** | Utilities / Moderation / Security |
| **Extensibility**      | Commands / Events / Services      |

### What is this project?

Project được xây dựng để bạn có thể nhanh chóng bắt đầu phát triển Discord Bot mà không phải thiết lập lại toàn bộ architecture từ đầu.

* Source code được phát triển chủ yếu bởi **nguyenphanno**
* Hỗ trợ **Prefix Commands**
* Hỗ trợ **Slash Commands**
* Hỗ trợ **Events**
* Tự động load Cogs trong `Services`
* Commands được chia theo từng category
* Configuration được tách khỏi source code
* Có sẵn moderation và security utilities
* Có thể mở rộng thêm database, logging và các service khác

> Project được cung cấp cho mục đích học tập, phát triển và xây dựng Discord Bot. Người sử dụng tự chịu trách nhiệm với cách triển khai và sử dụng source code.

---

## 02 · Repository Statistics

<div align="center">

<a href="https://github.com/nguyenphanno/VietNamese-Discord-Bot-Template">
<img src="https://github-readme-stats.vercel.app/api?username=nguyenphanno&repo=VietNamese-Discord-Bot-Template&show_icons=true&hide_border=true&bg_color=ffffff&title_color=8b5cf6&icon_color=8b5cf6&text_color=52525b&include_all_commits=true&count_private=true" height="170">
</a>

<a href="https://github.com/nguyenphanno/VietNamese-Discord-Bot-Template">
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=nguyenphanno&layout=compact&hide_border=true&bg_color=ffffff&title_color=8b5cf6&text_color=52525b&langs_count=8" height="170">
</a>

</div>

<br>

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=nguyenphanno&theme=default" width="92%">

</div>

---

## 03 · Quick Start

### Clone

```bash
git clone https://github.com/nguyenphanno/VietNamese-Discord-Bot-Template.git
cd VietNamese-Discord-Bot-Template
```

### Virtual Environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install

```bash
pip install -r requirements.txt
```

### Configure

Mở:

```text
Setting/Config.json
```

```json
{
    "TOKEN": "YOUR_BOT_TOKEN",
    "PREFIX": "!",
    "OWNER_ID": 123456789012345678,
    "CLIENT_ID": 123456789012345678
}
```

### Run

```bash
python main.py
```

> [!IMPORTANT]
> Không commit `TOKEN` lên GitHub. Nếu token đã bị lộ, hãy reset token ngay trong Discord Developer Portal.

---

## 04 · Features

### Command System

| Feature           | Description                         |
| :---------------- | :---------------------------------- |
| Prefix Commands   | Commands sử dụng prefix             |
| Slash Commands    | Native Discord application commands |
| Command Sync      | Đồng bộ Slash Commands              |
| Permission Checks | Kiểm tra quyền trước khi thực thi   |

### Moderation

| Command     | Description                | Required Permission |
| :---------- | :------------------------- | :------------------ |
| `!clear`    | Xóa messages               | Manage Messages     |
| `/clear`    | Xóa messages               | Manage Messages     |
| `/kick`     | Kick member                | Kick Members        |
| `/ban`      | Ban member                 | Ban Members         |
| `/lock`     | Khóa channel               | Manage Channels     |
| `/unlock`   | Mở khóa channel            | Manage Channels     |
| `/lockdown` | Khóa toàn bộ text channels | Administrator       |

### Security

| Feature              | Description                 |
| :------------------- | :-------------------------- |
| Ghost Ping Detection | Phát hiện ghost ping        |
| Lockdown System      | Khóa toàn bộ text channels  |
| Permission Awareness | Kiểm tra permissions        |
| Owner Commands       | Commands dành cho Bot Owner |
| Error Handling       | Xử lý command errors        |

### Developer Experience

* Modular Cogs
* Automatic Cog Loading
* Category-based Commands
* Event separation
* Centralized configuration
* Easy-to-maintain structure
* Easy to add new Services

---

## 05 · Project Architecture

```text
VietNamese-Discord-Bot-Template/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── Setting/
│   ├── Config.json
│   └── Env/
│       └── .env
│
└── Services/
    │
    ├── Events/
    │   ├── ready.py
    │   └── command_errors.py
    │
    └── Commands/
        │
        ├── Prefix/
        │   ├── Utilities/
        │   ├── Moderation/
        │   └── Security/
        │
        └── Slash/
            ├── Utilities/
            ├── Moderation/
            └── Security/
```

### Runtime Flow

```text
                         main.py
                            │
                            ▼
                    ┌───────────────┐
                    │   Bot Setup   │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  Auto Loader  │
                    └───────┬───────┘
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
           Events        Prefix          Slash
              │             │             │
              │             └──────┬──────┘
              │                    │
              └────────────────────┤
                                   ▼
                         ┌──────────────────┐
                         │ Command Services │
                         └────────┬─────────┘
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
                Utilities     Moderation     Security
```

**Auto Loader** sẽ quét các module `.py` trong `Services` và load chúng khi bot khởi động.

---

## 06 · Commands

### Prefix Commands

| Command           | Description            | Permission      |
| :---------------- | :--------------------- | :-------------- |
| `!ping`           | Kiểm tra latency       | Everyone        |
| `!help`           | Xem Prefix Commands    | Everyone        |
| `!clear <amount>` | Xóa messages           | Manage Messages |
| `!syncslash`      | Đồng bộ Slash Commands | Bot Owner       |

### Slash Commands

| Command     | Description                | Permission      |
| :---------- | :------------------------- | :-------------- |
| `/ping`     | Kiểm tra latency           | Everyone        |
| `/userinfo` | Xem thông tin member       | Everyone        |
| `/clear`    | Xóa messages               | Manage Messages |
| `/ban`      | Ban member                 | Ban Members     |
| `/kick`     | Kick member                | Kick Members    |
| `/lock`     | Khóa channel               | Manage Channels |
| `/unlock`   | Mở khóa channel            | Manage Channels |
| `/lockdown` | Khóa toàn bộ text channels | Administrator   |

---

## 07 · Configuration

Configuration nằm tại:

```text
Setting/Config.json
```

### Available Keys

| Key         | Type    | Description              |
| :---------- | :------ | :----------------------- |
| `TOKEN`     | String  | Discord Bot Token        |
| `PREFIX`    | String  | Prefix của bot           |
| `OWNER_ID`  | Integer | Discord ID của Bot Owner |
| `CLIENT_ID` | Integer | Discord Application ID   |

Example:

```json
{
    "TOKEN": "YOUR_BOT_TOKEN",
    "PREFIX": "!",
    "OWNER_ID": 123456789012345678,
    "CLIENT_ID": 123456789012345678
}
```

---

## 08 · Creating a Cog

### Prefix Cog

```py
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="example")
    async def example(self, ctx):
        await ctx.send("Example command")


async def setup(bot):
    await bot.add_cog(Example(bot))
```

Place it in:

```text
Services/Commands/Prefix/Utilities/
```

### Slash Cog

```py
import discord
from discord import app_commands
from discord.ext import commands


class ExampleSlash(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="example",
        description="Example slash command"
    )
    async def example(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "Example slash command"
        )


async def setup(bot):
    await bot.add_cog(ExampleSlash(bot))
```

Place it in:

```text
Services/Commands/Slash/Utilities/
```

> [!NOTE]
> Mỗi Cog bắt buộc phải có `async def setup(bot)` để Auto Loader có thể load module.

---

## 09 · Permissions & Intents

### Permissions

| Permission             | Used For            |
| :--------------------- | :------------------ |
| `Send Messages`        | Gửi response        |
| `Read Message History` | Đọc message history |
| `Manage Messages`      | Clear messages      |
| `Kick Members`         | Kick members        |
| `Ban Members`          | Ban members         |
| `Manage Channels`      | Lock / Unlock       |
| `Administrator`        | Lockdown            |

### Gateway Intent

Nếu sử dụng Prefix Commands, cần bật:

```text
Message Content Intent
```

trong **Discord Developer Portal**.

Nếu Intent chưa được bật, bot có thể online nhưng Prefix Commands sẽ không hoạt động đúng.

---

## 10 · Development Guide

### Add Utility

```text
Services/
└── Commands/
    └── Prefix/
        └── Utilities/
            └── my_command.py
```

### Add Moderation

```text
Services/
└── Commands/
    └── Slash/
        └── Moderation/
            └── my_moderation.py
```

### Add Security

```text
Services/
└── Commands/
    └── Slash/
        └── Security/
            └── my_security.py
```

### Add Event

```text
Services/
└── Events/
    └── my_event.py
```

Nên giữ mỗi module tập trung vào một nhiệm vụ cụ thể. Điều này giúp project dễ debug, maintain và mở rộng.

---

## 11 · Troubleshooting

| Problem                      | Solution                                 |
| :--------------------------- | :--------------------------------------- |
| Bot không online             | Kiểm tra `TOKEN`                         |
| Prefix không hoạt động       | Bật `Message Content Intent`             |
| Slash command chưa xuất hiện | Chạy `!syncslash`                        |
| Cog không load               | Kiểm tra `async def setup(bot)`          |
| Permission error             | Kiểm tra Bot Permissions                 |
| Moderation không hoạt động   | Kiểm tra Role Hierarchy                  |
| Bot phản hồi chậm            | Kiểm tra network / hosting / Discord API |
| Slash command cũ             | Sync lại commands                        |

---

## 12 · Roadmap

### Completed

* [x] Prefix Commands
* [x] Slash Commands
* [x] Automatic Cog Loading
* [x] Events System
* [x] Moderation Commands
* [x] Security Utilities
* [x] Lockdown System
* [x] Error Handling

### Planned

* [ ] Advanced Logging
* [ ] Database Integration
* [ ] More Security Modules
* [ ] More Utility Commands
* [ ] Improved Configuration System
* [ ] Advanced Moderation
* [ ] Better Permission Management
* [ ] Expanded Event System

> Roadmap có thể thay đổi trong quá trình phát triển project.

---

## 13 · Contributing

Contributions, suggestions và bug reports đều được chào đón.

```text
1. Fork repository
2. Create a branch
3. Make your changes
4. Test your changes
5. Commit your work
6. Push your branch
7. Open a Pull Request
```

Example:

```bash
git checkout -b feature/new-command
git add .
git commit -m "feat: add new command"
git push origin feature/new-command
```

### Bug Reports

Khi mở Issue, hãy cung cấp:

* Mô tả lỗi
* Cách tái hiện
* Error log
* Python version
* discord.py version
* Các bước đã thử

---

## 14 · Community

<div align="center">

<a href="https://discord.gg/fccfwHzms8">
<img src="https://img.shields.io/badge/Discord-Join%20Community-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord">
</a>

<br><br>

**VietNamese Discord Bot Community**

Thảo luận · Hỗ trợ · Bug Reports · Development

</div>

---

## 15 · Credits

<div align="center">

### Built by **nguyenphanno**

<a href="https://github.com/nguyenphanno">
<img src="https://img.shields.io/badge/GitHub-nguyenphanno-ffffff?style=for-the-badge&logo=github&logoColor=18181b&labelColor=ffffff" alt="GitHub">
</a>

<br><br>

**Built with**

`Python` · `discord.py` · `Discord API`

<br>

<a href="https://github.com/nguyenphanno/VietNamese-Discord-Bot-Template">
<img src="https://img.shields.io/badge/Star%20this%20repository-8b5cf6?style=for-the-badge&logo=github&logoColor=white" alt="Star repository">
</a>

<br><br>

₊˚⊹ **Build · Learn · Improve** ⊹˚₊

</div>

---

<div align="center">

<sub>

**VietNamese Discord Bot** · Open Source Discord Bot Template

</sub>

</div>
