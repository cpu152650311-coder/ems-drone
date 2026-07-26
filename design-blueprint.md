# EMS Drone — Design Blueprint

## CATEGORY
UAV Components B2B — 无人机组件工程制造出口

## BRAND PERSONALITY（三轴定位）
- **技术先锋型** ← 偏技术：大胆配色、signal 绿强调技术感
- **高端精密型** ← 偏精密：留白适中、工程视觉语言
- **国际通路型** ← 英文优先、信任信号突出

## DESIGN DIFFERENTIATORS（差异化决策）
- [x] 主色：Signal 绿 (#b8f34a) 代替行业常见的蓝色系
- [x] 布局系统：Hero 居中大标题 + 全幅背景图（非图文分屏）
- [x] 字体个性：System sans-serif stack（现代/干净/技术感）
- [x] 密度节奏：中等信息密度（不稀疏也不拥挤）
- [x] CTA 策略：主导航固定 CTA 按钮 + 全局询盘弹窗 + 联系页表单
- [x] Hero 构图：无人机系统抽象概念图 + 深色渐变遮罩

## COLOR PALETTE
| Token | Value | Role |
|-------|-------|------|
| `--ink` | #080d0e | 暗色背景 |
| `--ink-2` | #111819 | 次暗背景 |
| `--ink-3` | #182223 | 三级暗背景 |
| `--paper` | #f2f1ea | 亮色背景 |
| `--paper-2` | #e7e7de | 次亮背景 |
| `--surface` | #ffffff | 卡片/表单白底 |
| `--text` | #152021 | 正文色 |
| `--muted` | #4a5556 | 弱化文字 |
| `--muted-dark` | #c5d0cf | 暗背景下的弱化文字 |
| `--signal` | #b8f34a | 主强调色（荧光绿） |
| `--aero` | #7dc9d4 | 次强调色（航空蓝） |
| `--line` | #cad0c9 | 分割线（亮） |
| `--line-dark` | #2b3737 | 分割线（暗） |
| `--warning` | #ff9a52 | 警告色 |
| `--error` | #d14343 | 错误色 |

## TYPOGRAPHY
- **正文**: System sans-serif stack — Arial, Helvetica Neue, Helvetica, sans-serif
- **代码/mono**: Consolas, SFMono-Regular, Liberation Mono, monospace
- **字号范围**: 16px 正文 → clamp(2rem, 3.5vw, 3.2rem) H1 → clamp(2.25rem, 4.2vw, 4.7rem) H2

## PAGE COLLECTION（38 页）
- 首页 + 17 核心信任页 + 6 能力子页 + 6 行业子页 + 2 项目案例 + 6 博客文章

## IMAGE STRATEGY
- 所有图片使用 GPT Image 2 生成，1024×1024，quality=low
- 每页子 hero 独立图片（不可复用）
- 每篇博客 5-8 张配图
- 风格：暗色科技感，匹配 `--signal` 和 `--aero` 色调

## VISUAL REFERENCES
- 品类视觉意象：碳纤维纹理、电路板、航空仪表、测试台
- 避免：人物面部、文字、logo、过于明亮的场景
