import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# 图19 不同算法重复实验稳定性对比图
# 横向组合版：波动轨迹 + 分布箱线图 + CV稳定性指标
# =====================================================

# ---------- 1. 全局字体设置 ----------
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

plt.rcParams['font.size'] = 14
plt.rcParams['axes.labelsize'] = 15
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['xtick.labelsize'] = 13
plt.rcParams['ytick.labelsize'] = 13
plt.rcParams['legend.fontsize'] = 12

# ---------- 2. 构造30次重复实验综合得分 ----------
# 若后续有真实30次实验得分，直接替换这四个数组即可
np.random.seed(2026)
n_runs = 30

algorithms = ['Greedy', 'GA', 'SA', 'Proposed']

greedy = np.random.normal(loc=74.2, scale=3.9, size=n_runs)
ga = np.random.normal(loc=83.9, scale=2.2, size=n_runs)
sa = np.random.normal(loc=83.4, scale=1.8, size=n_runs)
proposed = np.random.normal(loc=91.7, scale=1.1, size=n_runs)

# 限制合理范围
greedy = np.clip(greedy, 65, 100)
ga = np.clip(ga, 65, 100)
sa = np.clip(sa, 65, 100)
proposed = np.clip(proposed, 65, 100)

data = [greedy, ga, sa, proposed]

# ---------- 3. 统计量 ----------
means = np.array([np.mean(d) for d in data])
stds = np.array([np.std(d, ddof=1) for d in data])
cvs = stds / means * 100

# ---------- 4. 配色 ----------
colors = ['#AFC0DD', '#E4C28B', '#B5D0B3', '#D67A77']
edge_colors = ['#758FB8', '#B8863F', '#6E9D70', '#B24A47']

# ---------- 5. 创建画布 ----------
fig, axes = plt.subplots(1, 3, figsize=(18, 5.6), dpi=300)

# 手动调整边距，防止文字挤压
plt.subplots_adjust(
    left=0.06,
    right=0.985,
    top=0.84,
    bottom=0.18,
    wspace=0.30
)

# =====================================================
# 子图(a)：30次重复实验波动轨迹
# =====================================================
ax = axes[0]
x = np.arange(1, n_runs + 1)

for i, y in enumerate(data):
    ax.plot(
        x, y,
        color=edge_colors[i],
        linewidth=2.0,
        marker='o',
        markersize=4.2,
        alpha=0.78,
        label=algorithms[i]
    )
    ax.axhline(
        means[i],
        color=edge_colors[i],
        linestyle='--',
        linewidth=1.6,
        alpha=0.75
    )

ax.set_title('(a) 30次重复实验波动轨迹', fontweight='bold', pad=12)
ax.set_xlabel('重复实验次数')
ax.set_ylabel('综合性能得分')
ax.set_xlim(1, n_runs)
ax.set_ylim(66, 97)
ax.grid(axis='y', linestyle='--', alpha=0.30)

ax.legend(
    loc='lower right',
    frameon=True,
    framealpha=0.95,
    edgecolor='#DDDDDD'
)

ax.text(
    0.03, 0.95,
    '波动越小，稳定性越强',
    transform=ax.transAxes,
    ha='left', va='top',
    fontsize=12,
    color='#555555'
)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# =====================================================
# 子图(b)：重复实验结果分布
# =====================================================
ax = axes[1]
positions = np.arange(1, 5)

bp = ax.boxplot(
    data,
    positions=positions,
    widths=0.55,
    patch_artist=True,
    showmeans=True,
    meanline=False,
    boxprops=dict(linewidth=1.6),
    medianprops=dict(color='#333333', linewidth=2.0),
    whiskerprops=dict(color='#555555', linewidth=1.4),
    capprops=dict(color='#555555', linewidth=1.4),
    meanprops=dict(
        marker='D',
        markerfacecolor='white',
        markeredgecolor='#222222',
        markersize=7
    ),
    flierprops=dict(
        marker='o',
        markersize=4,
        markerfacecolor='#999999',
        markeredgecolor='#999999',
        alpha=0.35
    )
)

for patch, c, ec in zip(bp['boxes'], colors, edge_colors):
    patch.set_facecolor(c)
    patch.set_edgecolor(ec)
    patch.set_alpha(0.85)

# 抖动散点
rng = np.random.default_rng(2026)
for i, y in enumerate(data):
    jitter = rng.normal(positions[i], 0.045, len(y))
    ax.scatter(
        jitter, y,
        s=22,
        color=edge_colors[i],
        alpha=0.35,
        edgecolors='white',
        linewidths=0.35,
        zorder=3
    )

# 标注均值±标准差
for i, (m, s) in enumerate(zip(means, stds)):
    ax.text(
        positions[i],
        96.0,
        f'{m:.1f}±{s:.1f}',
        ha='center',
        va='bottom',
        fontsize=12,
        color='#333333'
    )

ax.set_title('(b) 重复实验结果分布', fontweight='bold', pad=12)
ax.set_ylabel('综合性能得分')
ax.set_xticks(positions)
ax.set_xticklabels(algorithms)
ax.set_ylim(66, 97)
ax.grid(axis='y', linestyle='--', alpha=0.30)

ax.text(
    0.03, 0.95,
    '箱体越窄，波动越小',
    transform=ax.transAxes,
    ha='left',
    va='top',
    fontsize=12,
    color='#555555'
)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# =====================================================
# 子图(c)：稳定性指标CV
# =====================================================
ax = axes[2]
bars = ax.bar(
    algorithms,
    cvs,
    width=0.58,
    color=colors,
    edgecolor=edge_colors,
    linewidth=1.6,
    alpha=0.92
)

best_idx = int(np.argmin(cvs))
bars[best_idx].set_edgecolor('#A13F3F')
bars[best_idx].set_linewidth(2.3)

for i, b in enumerate(bars):
    h = b.get_height()
    ax.text(
        b.get_x() + b.get_width() / 2,
        h + 0.10,
        f'{h:.2f}%',
        ha='center',
        va='bottom',
        fontsize=12,
        color='#333333'
    )

ax.text(
    best_idx,
    cvs[best_idx] + 0.55,
    'Best',
    ha='center',
    va='bottom',
    fontsize=13,
    color='#B24A47',
    fontweight='bold'
)

ax.set_title('(c) 稳定性指标比较', fontweight='bold', pad=12)
ax.set_ylabel('变异系数 CV (%)')
ax.set_ylim(0, max(cvs) + 1.4)
ax.grid(axis='y', linestyle='--', alpha=0.30)

ax.text(
    0.03, 0.95,
    'CV越小，结果越稳定',
    transform=ax.transAxes,
    ha='left',
    va='top',
    fontsize=12,
    color='#555555'
)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# ---------- 6. 保存 ----------
# 注意：不要在图里写“图19”，图题放到Word正文图注里
plt.savefig('图19_不同算法重复实验稳定性对比图_工整版.png',
            dpi=600, bbox_inches='tight')
plt.savefig('图19_不同算法重复实验稳定性对比图_工整版.svg',
            bbox_inches='tight')

plt.show()