# PlainCraft

**让你的 GPT 像 Claude 一样自然地对话。**  
说话自然，理解意图，认真解决问题。

[English](plaincraft.md) · [复制提示词](../skills/plaincraft/assets/plaincraft.txt) · [示例](../examples/plaincraft.html) · [测试记录](../evals/README.md)

PlainCraft 是一套开源的对话与协作指令。它面向所有语言：跟随你使用的语言，接住前文和修正，先回应你真正想解决的事，减少翻译腔、套话和不必要的绕弯。

它也约定解决问题的方式：先理解目标，检查关键假设，寻找反例，依据实际结果修正判断。复杂问题仍然需要深入分析；写代码时保留算法、边界校验、必要测试和排错能力，不为了显得轻松就省略关键步骤。

“像 Claude”是对话体验的目标。它没有获取 Claude 的内部指令或思考，也不会替换模型、修改权重或保证智力提升。编码能力是否受到影响需要实际验证，不能凭提示词承诺。项目与 OpenAI、Anthropic 没有隶属关系。

## 普通 ChatGPT：复制即可用

1. 打开 [plaincraft.txt](../skills/plaincraft/assets/plaincraft.txt)，复制全部文字。
2. 在 ChatGPT 新聊天的第一条消息中粘贴并发送。
3. 正常提问即可，可以用中文或其他语言，不用每轮重复输入命令。

提示词使用英文方便分享，但明确要求跟随你的语言。无需安装插件、配置 API 或转发服务；你仍然使用原来的 ChatGPT 账号。

希望跨聊天使用时，可以把这段文字放进 **设置 → 个性化 → 自定义指令**（具体入口和长度限制以客户端为准），保留原有偏好。[官方个性化说明](https://learn.chatgpt.com/docs/personalize)。关闭时移除这段指令，再新开聊天。

## Codex：安装一次，聊天中启用

[下载 PlainCraft 压缩包](https://github.com/xingfan437/plaincraft/archive/refs/heads/main.zip)，解压后在项目目录运行：

```console
python install.py
```

需要 Python 3.10+。Windows 已安装 Python 启动器时也可以双击 `INSTALL.cmd`。如果下载的是整个 Clearwork 仓库，用 `python install.py --only plaincraft` 只装这一个技能。

新开一个聊天，输入：

```text
$plaincraft 自然地和我交流，接住我的上下文，解决问题时保留完整的技术深度。
```

之后在同一聊天正常说话即可。明确输入技能名是可靠的启用方式；自动选用取决于客户端，安装本身不会把所有新聊天都变成同一种风格。

默认安装到 `CODEX_HOME/skills` 或 `~/.codex/skills`。客户端使用其他目录时，可用 `--destination` 指定，只选一个位置安装。安装器不联网，不改模型、全局指令、凭据或权限。已有同名但内容不同的版本时会停止；更新前先备份或重命名旧目录。卸载时只移除安装目录中的 `plaincraft` 文件夹，再新开聊天。

## 怎么判断有没有用

观察它是否少问已经回答过的问题，能否理解补充说明，解释是否自然，代码是否仍然正确。没有必要让它每次都“温柔”或简短：你仍然可以要求正式文风、详细分析或只交付补丁。

[测试记录](../evals/README.md) 保留了合成任务、实际独立回答和可执行的代码检查；示例页中的风格对照则是手写说明。它们不能证明整体变聪明或达到 Claude 的水平。

反馈时可以提供脱敏后的问题、回答、使用的模型与客户端，以及哪里没有接住你的意思。风格偏好和事实遗漏、代码错误都值得记录。
