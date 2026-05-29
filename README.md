<div align="center">

# VietNam Discord Bot

**Discord Bot Template by Yinlewoaisuru**

<p>
  <a href="https://discord.gg/fccfwHzms8">
    <img alt="Discord Server" src="https://img.shields.io/badge/Discord-Tham_gia_may_chu-5865F2?style=for-the-badge&logo=discord&logoColor=white">
  </a>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="discord.py" src="https://img.shields.io/badge/discord.py-2.x-5865F2?style=for-the-badge">
  <img alt="Commands" src="https://img.shields.io/badge/Commands-Prefix_+_Slash-2EA44F?style=for-the-badge">
  <img alt="Cogs" src="https://img.shields.io/badge/Cogs-Auto_Load-FFB000?style=for-the-badge">
</p>

<p>
  <b>Gọn gàng</b> · <b>Dễ mở rộng</b> · <b>Tự động load cogs</b> · <b>Hỗ trợ Prefix và Slash</b>
</p>

<p>
  <a href="#cài-đặt-nhanh">Cài đặt</a>
  ·
  <a href="#cấu-trúc-thư-mục">Cấu trúc</a>
  ·
  <a href="#danh-sách-lệnh">Lệnh có sẵn</a>
  ·
  <a href="#tạo-cog-mới">Tạo cog</a>
  ·
  <a href="https://discord.gg/fccfwHzms8">Discord</a>
</p>

</div>

---

## Tổng quan

**VietNam Discord Bot** là template bot Discord viết bằng `discord.py`, được tổ chức theo cấu trúc module để dễ thêm lệnh, sự kiện và tính năng bảo mật.

- *Đây là source code bot Discord được viết chủ yếu bởi **Yinlewoaisuru***<br>
- *Source hỗ trợ lệnh Prefix, Slash Commands, Events và tự động load cogs trong thư mục `Services`*<br>
- *Lưu ý rằng chúng tôi sẽ không **chịu trách nhiệm** về những việc bạn làm khi mang source code đi quấy rối/gây hại cho<br>những cá nhân, tổ chức khác*<br>
- *Tham gia máy chủ Discord :* **https://discord.gg/fccfwHzms8**<br>
- *Bạn hoàn toàn có thể tạo pull requests nếu bot gặp lỗi hoặc contact discord của mình @iw.uyenn._*<br>

> [!NOTE]
> Dự án này ưu tiên cấu trúc sạch: `main.py` chỉ chạy bot và tự load cogs, còn tính năng được đặt trong `Services`.

> [!IMPORTANT]
> Không chia sẻ `TOKEN` bot công khai. Nếu token bị lộ, hãy reset token ngay trong Discord Developer Portal.

## Mục lục

- [Thông tin dự án](#thông-tin-dự-án)
- [Cài đặt nhanh](#cài-đặt-nhanh)
- [Cấu hình](#cấu-hình)
- [Cấu trúc thư mục](#cấu-trúc-thư-mục)
- [Tính năng](#tính-năng)
- [Danh sách lệnh](#danh-sách-lệnh)
- [Tạo cog mới](#tạo-cog-mới)
- [Quyền cần cấp](#quyền-cần-cấp)
- [Troubleshooting](#troubleshooting)
- [Tham khảo](#tham-khảo)

## Thông tin dự án

| Mục | Nội dung |
| --- | --- |
| Ngôn ngữ | Python |
| Thư viện chính | `discord.py` |
| Kiểu lệnh | Prefix Commands và Slash Commands |
| Cấu hình | `Setting/Config.json` |
| Module chính | `Services` |
| Entry point | `main.py` |
| Auto-load | Có, tự quét file `.py` trong `Services` |

## Cài đặt nhanh

### 1. Cài thư viện

```bash
pip install -r requirements.txt
```

### 2. Điền config

```txt
Setting/Config.json
```

### 3. Chạy bot

```bash
python main.py
```

> [!TIP]
> Nếu bạn đang dùng Windows PowerShell và muốn dùng môi trường ảo, có thể chạy:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Cấu hình

Mở file `Setting/Config.json` và điền thông tin bot:

```json
{
    "TOKEN": "TOKEN BOT CỦA BẠN Ở ĐÂY",
    "PREFIX": "!",
    "OWNER_ID": 0,
    "CLIENT_ID": 0
}
```

| Trường | Ý nghĩa | Ví dụ |
| --- | --- | --- |
| `TOKEN` | Token bot Discord | `"abc.xzy..."` |
| `PREFIX` | Prefix cho lệnh prefix | `"!"` |
| `OWNER_ID` | ID chủ bot | `123456789012345678` |
| `CLIENT_ID` | Application ID hoặc Client ID | `123456789012345678` |

> [!WARNING]
> `TOKEN` phải để trong `Setting/Config.json` hoặc hệ thống cấu hình riêng của bạn. Không đăng token lên GitHub, Discord hoặc gửi cho người khác.

## Cấu trúc thư mục

```txt
VietNamese-Discord-Bot-Template/
├─ main.py
├─ requirements.txt
├─ README.md
├─ .gitignore
├─ Setting/
│  ├─ Config.json
│  └─ Env/
│     └─ .env
└─ Services/
   ├─ Events/
   │  ├─ ready.py
   │  └─ command_errors.py
   └─ Commands/
      ├─ Prefix/
      │  ├─ Utilities/
      │  ├─ Moderation/
      │  └─ Security/
      └─ Slash/
         ├─ Utilities/
         ├─ Moderation/
         └─ Security/
```

> [!NOTE]
> Bạn chỉ cần thêm file `.py` mới vào đúng thư mục trong `Services`. Bot sẽ tự quét và load cog khi khởi động.

## Tính năng

| Nhóm | Mô tả |
| --- | --- |
| `Prefix` | Lệnh dạng `!ping`, `!help`, `!clear` |
| `Slash` | Lệnh dạng `/ping`, `/userinfo`, `/ban`, `/kick`, `/lock` |
| `Events` | Chứa listener như `on_ready`, error handler |
| `Security` | Có sẵn ghost ping detection và lockdown |
| `Auto Load` | Thêm file `.py` vào `Services` là bot tự load cog |
| `Clean Structure` | Tách rõ config, events, prefix commands và slash commands |

## Danh sách lệnh

### Prefix Commands

| Lệnh | Công dụng | Quyền |
| --- | --- | --- |
| `!ping` | Kiểm tra độ trễ bot | Tất cả |
| `!help` | Xem danh sách lệnh prefix | Tất cả |
| `!clear <số lượng>` | Xóa tin nhắn trong kênh | `Manage Messages` |
| `!syncslash` | Đồng bộ slash command | Owner bot |

### Slash Commands

| Lệnh | Công dụng | Quyền |
| --- | --- | --- |
| `/ping` | Kiểm tra độ trễ bot | Tất cả |
| `/userinfo` | Xem thông tin người dùng | Tất cả |
| `/clear` | Xóa tin nhắn | `Manage Messages` |
| `/ban` | Ban thành viên | `Ban Members` |
| `/kick` | Kick thành viên | `Kick Members` |
| `/lock` | Khóa kênh chat | `Manage Channels` |
| `/unlock` | Mở khóa kênh chat | `Manage Channels` |
| `/lockdown` | Khóa toàn bộ text channel | `Administrator` |

> [!TIP]
> Sau khi thêm hoặc sửa slash command, hãy dùng `!syncslash` để đồng bộ lại lệnh.

## Tạo cog mới

Đặt file `.py` vào một trong các thư mục sau:

```txt
Services/Commands/Prefix/Utilities/
Services/Commands/Prefix/Moderation/
Services/Commands/Prefix/Security/
Services/Commands/Slash/Utilities/
Services/Commands/Slash/Moderation/
Services/Commands/Slash/Security/
Services/Events/
```

Mẫu cog prefix:

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

Mẫu cog slash:

```py
import discord
from discord import app_commands
from discord.ext import commands


class ExampleSlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="example", description="Example slash command")
    async def example(self, interaction: discord.Interaction):
        await interaction.response.send_message("Example slash command")


async def setup(bot):
    await bot.add_cog(ExampleSlash(bot))
```

> [!IMPORTANT]
> Mỗi cog phải có `async def setup(bot): ...`. Nếu thiếu hàm này, `bot.load_extension()` sẽ không load được file đó.

## Quyền cần cấp

| Quyền | Dùng cho |
| --- | --- |
| `Send Messages` | Gửi phản hồi trong kênh |
| `Read Message History` | Đọc lịch sử tin nhắn |
| `Manage Messages` | Lệnh clear |
| `Kick Members` | Lệnh kick |
| `Ban Members` | Lệnh ban |
| `Manage Channels` | Lệnh lock, unlock, lockdown |
| `Administrator` | Một số thao tác moderation nâng cao |

> [!WARNING]
> Nếu dùng lệnh prefix, hãy bật `Message Content Intent` trong Discord Developer Portal. Nếu không bật, bot có thể online nhưng không đọc được nội dung tin nhắn như `!ping`.

## Troubleshooting

| Lỗi | Cách xử lý |
| --- | --- |
| Bot không online | Kiểm tra `TOKEN` trong `Setting/Config.json` |
| Prefix command không chạy | Bật `Message Content Intent` |
| Slash command chưa hiện | Chạy `!syncslash`, chờ Discord cập nhật |
| Cog không load | Kiểm tra file có `async def setup(bot)` |
| Lệnh moderation lỗi quyền | Đưa role bot lên cao hơn và cấp quyền cần thiết |

> [!CAUTION]
> Các lệnh như `ban`, `kick`, `clear`, `lockdown` có thể ảnh hưởng trực tiếp tới server. Hãy kiểm tra quyền và role hierarchy trước khi dùng.

## Tham khảo

- [GitHub Docs - Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Shields.io - Static Badge](https://shields.io/badges)
- [discord.py - Cogs](https://discordpy.readthedocs.io/en/v2.5.2/ext/commands/cogs.html)
- [discord.py - Bot commands framework](https://discordpy.readthedocs.io/en/v2.3.2/ext/commands/index.html)
- [Discord Developer Docs - Gateway Intents](https://docs.discord.com/developers/topics/gateway)

---

<div align="center">

**Made with care by Yinlewoaisuru**

**Join Discord:** https://discord.gg/A6sa9hARWA

</div>
