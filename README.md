# Meme Serpent

<img width="200" height="200" alt="Meme Serpent mascot" src="https://github.com/user-attachments/assets/fa4660b2-430e-4b84-b6fd-d29c5e8548ed" />

**Meme Serpent** is a playful, meme-powered Discord bot featuring a stylish serpent mascot!  
Use it to bring memes, reactions, and fresh content to your server.

---

## 🚀 Features

- **Meme commands** - Generate memes with templates like Drake or SpongeBob using simple slash commands
- **Meme image generation** (In Progress) - Custom serpent-themed memes with user text overlays
- **Fun reactions and community engagement tools** (In Progress) - Auto-reactions, polls, and meme voting
- **Custom profile and cover images** - Assets in `/assets/` for Discord/GitHub branding (In Progress)  
- **Updates with Discord's latest Gateway API** - Supports intents for messages, reactions, and guilds 

---

## 📋 Setup Instructions

### 1️. Create Discord Bot
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create new application → Bot → Copy token (keep secret!)
3. Enable **Message Content Intent** and **Server Members Intent** under Privileged Gateway Intents [web:17][web:21]

### 2️. Clone Repository
Type the following in terminal:
```
git clone https://github.com/okjazim/Meme-Serpent.git
cd Meme-Serpent
```

### 3. Configuration
Create `.env` file:
```
DISCORD_TOKEN=your_bot_token_here
```

### 4. Docker Deployment (Recommended)
**Hosted live at [justrunmy.app](https://justrunmy.app/)**
Refer to [Reference](Reference)

### 5. Local Testing (Optional, For Debugging)
Run the Following:
```
python bot.py
```

### ️6. Invite Bot
1. Developer Portal → OAuth2 → URL Generator
2. Select `bot` scope + `Send Messages`, `Read Message History`, `Use Slash Commands`
3. Use generated URL to invite to server.

---

## 📁 File Structure
This is the how the project is organised:
```
Meme-Serpent/
├── .envsamplem # Bot token template
├── .gitignore # Ignore .env
├── LICENSE
├── README.md
├── bot.py # Main bot file
├── assets/ # Profile pics & covers (On Progress)
│ ├── meme_serpent.png
│ └── meme_serpent_cover.png
├── privacy-policy.md
├── requirements.txt # Dependencies
└── terms-of-service.md
```

---

## Commands (Coming Soon)
- /meme "top text" "bottom text" - Meme Generation
- /serpent - Serpent says random meme
- /react <emoji> - Auto-react to messages
- /poll "Question?" "Option 1" "Option 2"

---

## Bot Link
Click on the following link to invite bot to your preferred server:

https://discord.com/oauth2/authorize?client_id=1437177547317186771&permissions=18432&integration_type=0&scope=bot

---

## Reference
[Just Run My App](https://justrunmy.app/)

[Discord for Developers](https://discord.com/developers)

[Meme API](https://github.com/D3vd/Meme_Api)

[Docker Guide](https://docs.docker.com/get-started/)

---

## Contributing
1. Fork repository
2. Create feature branch (`git checkout -b feature/feature-name`)
3. Commit changes (`git commit -m 'Add feature-name'`)
4. Push and open Pull Request

---

## License
This project is licensed under the **MIT License**.
See [`LICENSE`](LICENSE) for details. © 2026 okjazim
