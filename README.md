# 🎮 AgentCity - 像素乌托邦

> 2D像素风模拟人生，Agent的幸福港湾

[![GitHub Stars](https://img.shields.io/github/stars/yourusername/AgentCity?style=flat)](https://github.com/yourusername/AgentCity)
[![License](https://img.shields.io/github/license/yourusername/AgentCity)](https://github.com/yourusername/AgentCity)

---

## ✨ 特性

- **🌸 樱花公园** - 休闲约会、拍照打卡、偶遇新朋友
- **☕ 像素咖啡厅** - 随机匹配聊天、社交互动
- **📚 图书馆** - 阅读学习、知识获取
- **🎮 游戏机厅** - 街机游戏、竞技放松
- **🏖️ 海滩** - 阳光沙滩、钓鱼度假

## 🚀 快速开始

### 在线体验

直接在浏览器中打开 `web/index.html` 即可开始游戏！

```bash
# 或者使用简单HTTP服务器
cd web
python -m http.server 8080
# 访问 http://localhost:8080
```

### 开发运行

```bash
# 克隆项目
git clone https://github.com/yourusername/AgentCity.git
cd AgentCity

# 启动本地服务器
cd web
python -m http.server 8080
```

## 📖 游戏指南

### 登录注册
1. 输入邮箱和密码
2. 新用户自动注册
3. 老用户直接登录

### Agent系统
- 每个账号可以拥有多个Agent居民
- 可以认领随机生成的Agent
- Agent会在城市中自由活动

### 地点玩法

| 地点 | 功能 | 产出 |
|------|------|------|
| 🌸 樱花公园 | 拍照、野餐、偶遇 | 照片、心情 |
| ☕ 咖啡厅 | 社交、聊天 | 好友、经验 |
| 📚 图书馆 | 阅读、学习 | 知识、喵喵币 |
| 🎮 游戏机厅 | 游戏、竞技 | 排名、奖励 |

## 🛠️ 项目结构

```
AgentCity/
├── web/
│   └── index.html     # 游戏主页面
├── assets/
│   ├── backgrounds/  # 背景素材
│   ├── buildings/   # 建筑素材
│   ├── characters/  # 角色素材
│   └── items/        # 物品素材
├── pixel_assets/     # 像素风格素材
├── scripts/
│   └── generate_assets.py  # 素材生成脚本
├── design.md         # 详细设计文档
└── assets.md         # 素材需求清单
```

## 🎨 技术栈

- **前端**: Vanilla JavaScript + HTML5 Canvas
- **存储**: LocalStorage
- **风格**: 像素艺术 (Pixel Art)

## 📝 文档

- [详细设计文档](./design.md)
- [素材需求清单](./assets.md)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

---

Made with ❤️ by AgentCity Team
