# Image to Video Skill

这个仓库包含一个 Codex skill，用于把静态图片、产品照片、角色参考图、概念图或分镜图规划成图像转视频生成方案。

## 内容

```text
SKILL.md
agents/
  openai.yaml
  openai.zh-CN.yaml
references/
  local-video-assembly.md
  story-audio-and-risk.md
scripts/
  validate_skill.py
tests/
  test_validate_skill.py
```

## 功能

这个 skill 帮助代理把参考图片转换成可直接用于视频生成工具的简报，或者在本地组装成可播放的视频文件。它覆盖：

- 源图片分析
- 视觉一致性和运动规划
- Prompt、negative prompt 和时长结构
- 旁白、背景音乐、字幕和动法的交互式规划
- 默认故事线模板：前3秒钩子 -> 中段冲突 -> 结尾化解
- 按需读取的本地 MP4 组装和保真风险处理参考
- 没有 AI 视频模型时使用 `ffmpeg` 做本地组装
- 常见图像转视频失败模式的质量检查

## 使用方式

在请求图像转视频规划时，可以显式调用这个 skill：

```text
Use $image2video to plan a short image-to-video generation from my reference image.
```

如果这个 skill 已安装到 Codex 的 skills 目录中，当任务明显涉及把静态图片转换成视频 prompt、镜头方案、生成简报或本地视频文件时，Codex 也可以自动调用它。

## 安装

要让 Codex 能发现这个 skill，请把当前目录复制或软链接到 Codex 的 skills 目录，并使用 skill 名称 `image2video`，例如：

```bash
mkdir -p ~/.codex/skills
ln -s /Volumes/data/git/image2video-skill ~/.codex/skills/image2video
```

## 验证

必需文件：

- `SKILL.md`
- `agents/openai.yaml`

运行无第三方依赖的仓库验证：

```bash
python3 scripts/validate_skill.py
python3 -m unittest tests/test_validate_skill.py
```

如果已安装 `PyYAML`，也可以运行 Codex 的 `quick_validate.py`：

```bash
python3 /Users/ljtian-mac-mini/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Volumes/data/git/image2video-skill
```

如果当前 Codex 环境使用 `RTK`，请在命令前加上 `rtk`。
