from core.style import Color, ColorMid

"""
1. 自动根据数据缩放轴区间，提供自定区间接口
2. 折线图可选关闭纵网格，柱状图无纵网格线可选关闭横网格
"""

# 折线图

# todo 普通柱状图

# todo 堆积柱状图

# todo 分组柱状图

  # 自定义x轴的形式再增加分组

def groupBarByGroup(
        main_groups: dict,
        input_values: dict,
        color: Color = ColorMid
    ):
    import matplotlib.pyplot as plt
    import numpy as np

    # 数据准备
    """
    main_groups = {
        'Main Group A': ['Sub X1', 'Sub X2'],
        'Main Group B': ['Sub Y1', 'Sub Y2', 'Sub Y3'],
        'Main Group C': ['Sub Z1']
    }

    input_values = {
        'Category X': [20, 34, 30, 25, 32, 35],
        'Category Y': [25, 32, 35, 20, 34, 30],
        'Category Z': [30, 28, 32, 25, 30, 33]
    }
    """

    # 所有子组的标签
    sub_groups = []
    for sub_group_list in main_groups.values():
        sub_groups.extend(sub_group_list)

    # 子组的位置
    x = np.arange(len(sub_groups))
    width = 1.0 / (len(input_values) + 1)  # 条形的宽度

    # 创建图形和轴
    fig, ax = plt.subplots(figsize=(16, 6))

    # 绘制条形图
    all_rects = []  # 用来存储所有的条形对象
    for index, (label, value) in enumerate(input_values.items()):
        bars = ax.bar(x + (index - 1.5) * width, value[:len(sub_groups)], width, label=label, color=color.get(index))
        all_rects.append(bars)

    # 设置 X 轴的刻度和标签
    ax.set_xticks(x)
    ax.set_xticklabels(sub_groups)

    # 在每个主组的中心位置标注主组名称
    current_position = 0
    for main_group, sub_group_list in main_groups.items():
        # 计算每个主组的中心位置
        center_position = current_position + (len(sub_group_list) - 1) / 2
        y_distance = -3
        ax.text(center_position, y_distance, main_group, ha='center', va='top', fontsize=12, color='black')
        
        # 更新当前位置
        current_position += len(sub_group_list)

    # 在组之间画竖线分割
    current_position = 0
    for sub_group_list in main_groups.values():
        end_position = current_position + len(sub_group_list)
        if end_position < len(sub_groups):  # 防止最后一个主组之后画线
            # 竖线应该放在每个主组的右边界
            ax.axvline(x=end_position - 2.5*width, color='black', linestyle='--', linewidth=2)
        current_position = end_position

    # 设置其他属性
    ax.set_ylabel('Values', fontsize=14)
    ax.set_title('Values by Main Groups and Sub Groups', fontsize=14, y=-0.2)
    
    # 美化图例并将其移动到上方
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.10), ncol=5, frameon=False, fontsize=12)

    # 自动为每个条形添加数值标签
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    # 为所有条形添加数值标签
    for bars in all_rects:
        autolabel(bars)

    # # 设置 X 轴范围，减少两侧空隙
    ax.set_xlim(-0.5, current_position - 2*width)  # 将 x 轴范围限制在数据的左右两侧

    # 显示图形
    plt.tight_layout()
    plt.show()



# todo 分组堆积柱状图



# 时频-步频图 matshow + colorbar

# 频率分布折线图