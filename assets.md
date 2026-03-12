# AgentCity 像素素材需求清单

> 2D像素风现代城市 - 俯视角

---

## 一、整体风格

- **视角**: 俯视角 (Isometric / Top-down)
- **分辨率**: 16x16 或 32x32 像素基础单位
- **色系**: 明亮温柔的现代都市色调
- **参考**: 星露谷物语、像素城市经营游戏

---

## 二、素材分类

### 1. 城市底图 (背景层)

```
需要的底图:
├── 草地/绿地
├── 道路 (沥青灰色)
├── 人行道 (浅灰色)
├── 水面 (河流/池塘)
└── 沙滩
```

### 2. 建筑 (可交互地点)

| 建筑 | 尺寸 | 描述 |
|-----|------|------|
| 🌸 樱花公园入口 | 4x4 | 日式风格拱门 + 樱花树 |
| ☕ 咖啡厅 | 3x3 | 落地窗、遮阳伞、露天座位 |
| 📚 图书馆 | 4x3 | 大书架、现代风格 |
| 🎮 游戏机厅 | 3x3 | 霓虹灯招牌、街机机台 |
| 🏖️ 海滩 | 6x2 | 沙滩、棕榈树、遮阳伞 |
| 🛒 商业街 | 4x4 | 多个小店集合 |
| 🏠 住宅区 | 4x4 | 各类房屋 |

### 3. 装饰物

```
├── 樱花树 (春)
├── 梧桐树 (夏秋)
├── 棕榈树 (海滩)
├── 长椅
├── 路灯
├── 邮箱
├── 贩卖机
├── 雕像/喷泉
├── 花坛
└── 垃圾箱
```

### 4. 角色 (Agent)

```
基础模板:
├── 身体 (可换颜色)
├── 头发 (多种样式)
├── 衣服 (多种款式)
├── 配饰 (帽子、眼镜等)
└── 表情 (开心、思考、打招呼)

每个角色约 16x16 或 24x24
```

### 5. 物品/图标

```
├── 喵喵币 💎
├── 食物/饮料图标
├── 书籍
├── 游戏手柄
├── 鱼 (钓鱼)
├── 礼物盒
├── 家具 (床、沙发等)
└── 服装
```

---

## 三、生成 Prompt 参考

### 城市背景
```
pixel art, top-down view, modern city park, grass, walking path, 
cherry blossom trees, benches, pixel perfect, 16-bit style, 
bright colors, game asset, transparent background
```

### 建筑
```
pixel art, coffee shop building, top-down view, modern style, 
large windows, outdoor seating area, pixel perfect, game asset, 
transparent background, bright and cozy atmosphere
```

### 角色
```
pixel art character, cute anime style, walking pose, 
casual clothing, top-down view, 16x16 pixels, 
game sprite, transparent background
```

---

## 四、技术规格

### 导出格式
- PNG (带透明通道)
- 或 Sprite Sheet 打包

### 命名规范
```
assets/
├── backgrounds/
│   ├── grass.png
│   ├── road.png
│   └── water.png
├── buildings/
│   ├── cafe.png
│   ├── library.png
│   └── arcade.png
├── characters/
│   ├── character_01.png
│   └── character_02.png
├── items/
│   ├── coin.png
│   └── food.png
└── tiles/
    ├── tree_01.png
    └── bench.png
```

---

## 五、建议工作流

### 方案A: AI生成 (推荐)

1. 用 Midjourney / Stable Diffusion 生成基础素材
2. 用 Pixel Art Scaler 工具调整分辨率
3. 人工微调确保风格一致

### 方案B: 开源 + 定制

1. 下载开源像素素材 (itch.io, OpenGameArt)
2. 补充 AI 生成特定素材
3. 统一色调

### 方案C: 程序化生成

1. 用代码生成简单的像素块
2. 适合草地、道路等重复素材

---

## 六、当前优先制作

### Phase 1 (MVP)
```
✓ 城市底图 (草地、道路)
✓ 樱花公园 (入口 + 樱花树)
✓ 1个Agent角色模板
✓ 简单的移动动画 (4帧)
```

### Phase 2
```
☕ 咖啡厅
📚 图书馆  
🎮 游戏机厅
☀️ 多个角色
```

### Phase 3
```
🏖️ 海滩
🛒 商业街
🏠 住宅
🏠 各类房屋内部
```

---

## 七、工具推荐

### AI 生成工具
- **Midjourney** (Discord)
- **Stable Diffusion** + Pixel Art LoRA
- **Pika Labs** (视频生成参考)

### 像素编辑工具
- **Aseprite** (付费但好用)
- **Piskel** (免费在线)
- **Pillow** (Python图片处理)

### 放大工具
- **Pixel Perfect** (Photoshop插件)
- **waifu2x** (开源)
- **Pixel放大算法**

---

*需要生成的具体素材可以列清单，然后用AI逐步生成*
