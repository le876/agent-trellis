[English](README.md)

# Agent Trellis

Agent Trellis 是一个随代码库共同生长的最小 Agent 治理系统。它为 Codex 提供仓库内的事实、归属、验证、长期决策和临时工作状态地图，同时不预设语言、框架或部署模型。

## 安装

让 Codex 使用 `$skill-installer`，从 `le876/agent-trellis` 安装 `skills/agent-trellis-init`。安装后新建一个任务，然后在需要初始化的仓库中调用 `$agent-trellis-init`。

版本 1 仅面向 Codex，并且有意不提供 CLI。

## 初始化方式

初始化器遵守明确的确认边界：

1. 只读审计仓库，不写入文件。
2. 仅从源码、配置、文档或可观察命令中提取有证据支持的事实；冲突和无法验证的内容保持未知。
3. 展示拟议的 owner map，以及每个需要创建、合并或保留的文件。
4. 等待用户明确确认。
5. 写入最小且有用的治理层，并完成验证。

它不会覆盖已有规则，不会提交或推送，也不会执行生产、硬件或其他会改变外部状态的操作。再次运行时，它会审计漂移并提出合并建议；它不是上游同步器，也不会删除项目定制。

## 生成的治理内容

核心输出包括：

- 根 `AGENTS.md`；
- 架构、开发和测试事实的 owner；
- 用于长期决策的 Agent Note 生命周期；
- 用于跨会话临时状态的 Active Work 生命周期；以及
- 通用的项目文档、行文、审查、简化和推送前检查 Skills。

只有当仓库证据表明确有需要时，才生成安全、信息安全、数据契约或其他专项 owner。生成语言跟随目标仓库已经建立的文档语言；证据不明确时，初始化器会询问用户。

## 仓库结构

- [`skills/agent-trellis-init/`](skills/agent-trellis-init/SKILL.zh-CN.md) 包含可安装的 Codex Skill。
- [`i18n/pairs.json`](i18n/pairs.json) 声明英文与中文文档配对。英文是 canonical 版本，中文是完整同步译本。
- [`scripts/validate.py`](scripts/validate.py) 使用标准库检查双语结构、链接、占位符、Skill metadata、模板和 fixtures。
- [`tests/scenarios.zh-CN.md`](tests/scenarios.zh-CN.md) 定义初始化验收场景。

## 验证

```sh
python3 scripts/validate.py
```

## 许可证与来源

Agent Trellis 使用 MIT 许可证。固定的 DeepSeek Harness 适配基线及其许可证声明见 [`THIRD_PARTY_NOTICES.zh-CN.md`](THIRD_PARTY_NOTICES.zh-CN.md)。
