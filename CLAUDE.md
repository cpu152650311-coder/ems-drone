# EMS Drone — UAV Component B2B Website

> 静态 HTML/CSS 站点，部署于 Cloudflare Pages

## 站点概览

| 项目 | 说明 |
|------|------|
| 域名 | `ems-drone.pages.dev` |
| 页面数 | 40（含 404 / thanks / welcome） |
| 部署 | Cloudflare Pages (`wrangler pages deploy ./ --branch=main --commit-dirty=true`) |
| 图片 | GPT Image 2 (1024×1024, quality=low) via `skills/ai-image-gen/scripts/gen-image.py` |

## 关键文件

| 文件 | 用途 |
|------|------|
| `design-tokens.css` | 全站 CSS 变量和基础样式，v=16 |
| `site.js` | 导航、弹窗、表单提交逻辑，v=9 |
| `reveal.js` | 滚动渐显动画，v=8 |
| `content-blueprint.md` | 产品参数/认证/产能/品质数据（博客工作流读取） |
| `design-blueprint.md` | 品牌人格/色彩/字体/差异化决策 |
| `image-strategy.json` | 全站图片角色和 prompt 策略 |
| `wrangler.toml` | Cloudflare Pages 部署配置 |

## 询盘系统

- **弹窗**：全站 38 页统一 `#inquiryModal`，由 `data-open-inquiry` 按钮触发
- **表单提交**：POST JSON → `https://inquiry-proxy.workers.dev/`
- **成功后**：自动跳转 `/thanks.html`
- **字段**：name / email / message + source (自动填充当前路径)
- **联系页**：contact/index.html 保留独立表单（id="inquiryForm"）
- **报价页**：quote/index.html 保留独立表单（data-preview-form）

## CTA 按钮模式

```
Nav:  <button class="btn btn-primary" data-open-inquiry>Start Your Build</button>
Page: <button class="btn btn-outline" data-open-inquiry>Open RFQ Brief</button>
```

所有 CTA 按钮使用 `data-open-inquiry` 触发弹窗，不再直接跳转 `/contact/`。

## 导航结构

```
Home → Capabilities → Services → Industries → Resources → Company → [Start Your Build]
```

- 首页 Home 链接有 `aria-current="page"`
- 联系页 Contact 菜单项有 `aria-current="page"`
- 其他页面当前页标记已正确设置

## CSS 版本管理

修改 CSS 后需全站更新 `?v=N`，用 Python 脚本批量替换：
```python
content.replace('design-tokens.css?v=16', 'design-tokens.css?v=17')
```

## 部署

```bash
cd ~/ClaudeCode/ems-drone
source .env  # CLOUDFLARE_API_TOKEN + CLOUDFLARE_ACCOUNT_ID
npx wrangler pages deploy ./ --branch=main --commit-dirty=true
```

## 博客工作流（blog-workflow v6.2）

服务器端 Agent 运行博客工作流时：
1. 进入此项目目录
2. 读取 `content-blueprint.md` + `design-blueprint.md` + `image-strategy.json`
3. 读取 `design-tokens.css` 获取品牌色
4. 检查 `/blog/index.html` 是否存在（✅ 已存在）
5. 自动选题 → 生成内容 → 配图 5-8 张 → 部署

## 当前状态（2026-07-26）

- CSS v=16, JS v=9
- 全站 38 页含 site-nav，6 篇博客文章
- 询盘系统：弹窗 + thanks 页跳转
- 404 / thanks / welcome 独立页面
- 图片全部保存在 `/generated/` 目录

## 已有博客文章

| 路径 | 标题 |
|------|------|
| `/blog/drone-powertrain-matching/` | UAV Powertrain Matching |
| `/blog/flight-controller-esc-matching/` | Flight Controller & ESC Matching |
| `/blog/low-altitude-economy-components/` | Low-Altitude Economy Components |
| `/blog/uav-airframe-materials-guide/` | UAV Airframe Materials Guide |
| `/blog/uav-component-build-vs-buy/` | UAV Component Build vs Buy |
| `/blog/uav-supply-chain-layers/` | UAV Supply Chain Layers |
