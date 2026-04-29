# Image to Video Skill

这个仓库包含一个 Codex skill，用于把静态图片、产品照片、角色参考图、概念图或分镜图规划成图像转视频生成方案。

## 内容

```text
SKILL.md
agents/
  openai.yaml
```

## 功能

这个 skill 帮助代理把参考图片转换成可直接用于视频生成工具的简报，或者在本地组装成可播放的视频文件。它覆盖：

- 源图片分析
- 视觉一致性和运动规划
- Prompt、negative prompt 和时长结构
- 含文字或分镜内容时的旁白与音频规划
- 没有 AI 视频模型时使用 `ffmpeg` 做本地组装
- 用 `hook -> conflict -> resolution` 讲更有吸引力的解释型故事
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

如果已安装 `PyYAML`，可以用 `quick_validate.py` 验证：

```bash
python3 /Users/ljtian-mac-mini/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Volumes/data/git/image2video-skill
```

如果当前 Codex 环境使用 `RTK`，请在命令前加上 `rtk`：

```bash
rtk python3 /Users/ljtian-mac-mini/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Volumes/data/git/image2video-skill
```
