#!/usr/bin/env python3
"""
生成技能雷达图的 Python 脚本
"""
import matplotlib.pyplot as plt
import numpy as np
import os

# 创建输出目录
os.makedirs('dist', exist_ok=True)

# 定义技能类别和熟练度（0-100）
categories = ['Python', 'Java', 'C++', 'AI/ML', 'Web前端', 'Web后端', '数据库', '工具链']
values = [85, 75, 70, 80, 70, 75, 70, 80]  # 根据实际情况调整

# 计算角度
num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
values += values[:1]  # 闭合图形
angles += angles[:1]

# 创建图形
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# 绘制雷达图
ax.plot(angles, values, 'o-', linewidth=2, color='#4A90E2', label='技能水平')
ax.fill(angles, values, alpha=0.25, color='#4A90E2')

# 设置标签
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold')

# 设置径向范围
ax.set_ylim(0, 100)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20', '40', '60', '80', '100'], fontsize=10)
ax.grid(True, linestyle='--', alpha=0.7)

# 添加标题
plt.title('技能雷达图', size=16, fontweight='bold', pad=20)

# 保存为 SVG
plt.tight_layout()
plt.savefig('dist/skills-radar-chart.svg', format='svg', bbox_inches='tight', facecolor='white')
plt.close()

print("技能雷达图已生成: dist/skills-radar-chart.svg")
