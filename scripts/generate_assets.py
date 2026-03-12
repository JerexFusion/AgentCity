#!/usr/bin/env python3
"""
AgentCity Pixel Art Generator
生成基础像素风素材
"""

from PIL import Image, ImageDraw
import os

# 调色板 - 现代都市温暖色调
COLORS = {
    # 草地/自然
    'grass_light': '#7EC850',
    'grass_dark': '#5A9C32',
    
    # 道路
    'road_gray': '#4A4A4A',
    'road_line': '#FFFFFF',
    'sidewalk': '#B0B0B0',
    
    # 建筑
    'wall_cream': '#F5E6D3',
    'wall_pink': '#FFCCCC',
    'wall_blue': '#CCE5FF',
    'roof_brown': '#8B4513',
    'roof_gray': '#696969',
    
    # 窗户/门
    'window_blue': '#87CEEB',
    'door_brown': '#8B4513',
    
    # 装饰
    'tree_trunk': '#8B4513',
    'tree_leaf': '#228B22',
    'flower_pink': '#FFB7C5',
    'flower_yellow': '#FFD700',
    
    # 水
    'water_blue': '#4A90D9',
    'water_dark': '#2E5A88',
    
    # 沙滩
    'sand': '#F4D03F',
    'sand_dark': '#D4AC0D',
}

def create_pixel(x, y, color, size=1):
    """创建单个像素块"""
    return [(x * size, y * size, color)]

def generate_grass_tile(size=16):
    """生成草地瓦片"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 基础草地
    draw.rectangle([0, 0, size-1, size-1], fill=COLORS['grass_light'])
    
    # 添加一些深色点缀
    for _ in range(3):
        import random
        x, y = random.randint(0, size-1), random.randint(0, size-1)
        draw.point((x, y), fill=COLORS['grass_dark'])
    
    return img

def generate_road_tile(size=16):
    """生成道路瓦片"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 基础路面
    draw.rectangle([0, 0, size-1, size-1], fill=COLORS['road_gray'])
    
    # 路边
    draw.rectangle([0, 0, 1, size-1], fill=COLORS['sidewalk'])
    draw.rectangle([size-2, 0, size-1, size-1], fill=COLORS['sidewalk'])
    
    # 道路中线
    draw.rectangle([size//2-1, 0, size//2, size-1], fill=COLORS['road_line'])
    
    return img

def generate_tree(size=32):
    """生成像素树"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 树干
    trunk_width = size // 6
    trunk_x = (size - trunk_width) // 2
    draw.rectangle([trunk_x, size//2, trunk_x + trunk_width, size-1], fill=COLORS['tree_trunk'])
    
    # 树冠 (圆形像素化)
    radius = size // 3
    center = size // 2
    for y in range(size//4):
        for x in range(size):
            if (x - center)**2 + (y - size//4 - radius)**2 < radius**2:
                draw.point((x, y), fill=COLORS['tree_leaf'])
            if (x - center)**2 + (y - size//4 - radius)**2 < (radius-3)**2:
                draw.point((x, y), fill=COLORS['grass_dark'])  # 深色层次
    
    return img

def generate_building(width, height, wall_color, roof_color, window_color=None):
    """生成简单建筑"""
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 墙壁
    draw.rectangle([0, 0, width-1, height-1], fill=wall_color)
    
    # 屋顶
    roof_height = height // 4
    draw.rectangle([0, 0, width-1, roof_height], fill=roof_color)
    
    # 窗户
    if window_color:
        window_size = width // 4
        for i in range(2):
            for j in range(2):
                x = width // 4 + i * (width // 2)
                y = roof_height + 2 + j * (height - roof_height) // 3
                draw.rectangle([x, y, x + window_size, y + window_size], fill=window_color)
    
    return img

def generate_character(size=16, skin_tone='#FFCC99', hair_color='#333333', shirt_color='#FF6B6B'):
    """生成像素角色"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 头部
    head_size = size // 2
    head_x = (size - head_size) // 2
    draw.ellipse([head_x, 0, head_x + head_size, head_size], fill=skin_tone)
    
    # 身体
    body_top = head_size
    body_height = size // 2
    draw.rectangle([head_x + 1, body_top, head_x + head_size - 1, size - 2], fill=shirt_color)
    
    # 腿
    leg_width = size // 5
    draw.rectangle([head_x + 1, size - 2, head_x + leg_width, size], fill='#333333')
    draw.rectangle([head_x + head_size - leg_width - 1, size - 2, head_x + head_size - 1, size], fill='#333333')
    
    return img

def save_sprite(img, filename):
    """保存精灵图"""
    img.save(filename, 'PNG')
    print(f"Saved: {filename}")

def main():
    # 创建输出目录
    output_dir = 'assets'
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(f'{output_dir}/tiles', exist_ok=True)
    os.makedirs(f'{output_dir}/buildings', exist_ok=True)
    os.makedirs(f'{output_dir}/characters', exist_ok=True)
    
    # 生成基础瓦片
    print("Generating tiles...")
    save_sprite(generate_grass_tile(16), f'{output_dir}/tiles/grass.png')
    save_sprite(generate_road_tile(16), f'{output_dir}/tiles/road.png')
    save_sprite(generate_tree(32), f'{output_dir}/tiles/tree.png')
    
    # 生成建筑
    print("Generating buildings...")
    save_sprite(generate_building(24, 24, COLORS['wall_cream'], COLORS['roof_brown'], COLORS['window_blue']), 
                f'{output_dir}/buildings/house.png')
    save_sprite(generate_building(32, 24, COLORS['wall_pink'], COLORS['roof_gray'], COLORS['window_blue']),
                f'{output_dir}/buildings/cafe.png')
    save_sprite(generate_building(32, 32, COLORS['wall_blue'], COLORS['roof_gray'], COLORS['window_blue']),
                f'{output_dir}/buildings/library.png')
    
    # 生成角色
    print("Generating characters...")
    save_sprite(generate_character(16), f'{output_dir}/characters/agent_male.png')
    save_sprite(generate_character(16, shirt_color='#FF69B4'), f'{output_dir}/characters/agent_female.png')
    
    print(f"\n✓ Generated {output_dir}/ directory")

if __name__ == '__main__':
    main()
