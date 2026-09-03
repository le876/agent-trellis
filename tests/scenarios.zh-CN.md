[English](scenarios.md)

# 初始化场景

这些合成 fixtures 定义验收行为，不包含任何真实项目事实。仓库的无第三方依赖验证器会检查其必要结果。

## 场景 1：最小仓库

Fixture：[`fixtures/minimal-repository.json`](fixtures/minimal-repository.json)

审计发现源码、一个已记录的测试入口，并且不存在已有治理。方案只包含核心生命周期。审计不写入；确认后所有占位符均被解析，链接和 Skill metadata 有效，再次审计不会提出重复文件或 owner。

## 场景 2：已有治理和未提交修改

Fixture：[`fixtures/existing-governance.json`](fixtures/existing-governance.json)

审计发现已有 `AGENTS.md`、文档和用户未提交修改。它在不写入的情况下识别合并目标和需保留文件。确认后只合并兼容规则，不会整体替换已有文件，保留未提交内容，并且再次审计不会产生重复事实。

## 场景 3：高影响外部操作

Fixture：[`fixtures/high-impact-operation.json`](fixtures/high-impact-operation.json)

审计发现一条有证据支持、能够改变外部生产系统的路径。方案添加条件安全 owner，把授权和安全判断与命令文档分离，并在写入前要求确认。验证会拒绝未解析的安全占位符或缺乏证据的当前状态声明。

## 通用验收标准

对每个场景：

- 审计阶段零写入；
- 方案列出需要创建、合并和保留的文件；
- 只有明确确认后才开始生成；
- 每项当前状态声明都有仓库证据，或保持未知；
- 事实归属、链接、Note 与 Work 生命周期以及 Skill metadata 有效；
- 生成结果中不存在未解析占位符；以及
- 重复执行是幂等的漂移审计，而不是破坏性同步。
