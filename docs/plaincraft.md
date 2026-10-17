# PlainCraft

**Make your GPT talk like Claude.**  
Natural conversation. Thoughtful problem solving. Rigorous coding.

[简体中文](plaincraft.zh-CN.md) · [Copyable prompt](../skills/plaincraft/assets/plaincraft.txt) · [Examples](../examples/plaincraft.html) · [Evaluation](../evals/README.md)

PlainCraft is a small, open-source instruction kit for people who like GPT's coding ability and want conversation that feels more attentive and natural. It follows your language, carries forward relevant context, gets to the point, and explains decisions without a wall of canned framing.

It also guides **how to approach the task**: understand the intended outcome, examine important assumptions, look for counterexamples, and revise when the evidence changes. Hard problems still deserve deep work. Necessary validation, permissions, cleanup and tests remain part of good code.

“Like Claude” describes the conversational experience we aim for. PlainCraft does not contain Claude's instructions, reproduce its private reasoning, change model weights, or guarantee higher intelligence or unchanged performance on every coding task. It is an independent project, unaffiliated with OpenAI or Anthropic.

## Start in ChatGPT — no installation

1. Open [plaincraft.txt](../skills/plaincraft/assets/plaincraft.txt) and copy its contents.
2. Paste it as the first message in a ChatGPT conversation.
3. Ask your question normally, in any language. You do not need to type a command each turn.

The prompt is written in English for portability; it explicitly follows the language you use or request. No API key, proxy, browser extension or extra service is involved. Your normal ChatGPT access still applies.

For a preference across conversations, put the compact prompt in **Settings → Personalization → Custom instructions**, where available. Keep your existing preferences. Settings and instruction limits can vary between clients. See [OpenAI's personalization guide](https://learn.chatgpt.com/docs/personalize). To turn it off, remove that instruction and start a new conversation.

## Start in Codex

[Download the PlainCraft ZIP](https://github.com/xingfan437/plaincraft/archive/refs/heads/main.zip), extract it, then run in its extracted folder:

```console
python install.py
```

Requires Python 3.10+. On Windows with the Python launcher, double-click `INSTALL.cmd`. From the full Clearwork repository, install just PlainCraft with `python install.py --only plaincraft`.

Start a new chat, then write:

```text
$plaincraft Help me solve this. Use my language, keep the conversation natural, and preserve your full technical depth.
```

Continue talking normally in that chat. Explicit invocation is the reliable way to request the skill; automatic discovery depends on the host. Installation makes the skill available, rather than changing every future chat automatically.

The installer copies files into `CODEX_HOME/skills`, or `~/.codex/skills`. If your host uses a different skill directory, pass `--destination /your/skill/directory`. Install in one discovery location only. The installer makes no network calls and does not edit model settings, global instructions, credentials or permissions. It refuses to overwrite a different existing version: back up or rename that folder before installing an update. To uninstall, remove only the installed `plaincraft` skill folder and start a new chat.

## What should feel different?

| Situation | PlainCraft's intended behavior |
| --- | --- |
| You clarify a previous request | Carry forward the goal and constraints instead of restarting |
| You ask a simple question | Answer directly, with the detail needed to understand it |
| The problem is difficult | Work through assumptions and evidence; explain the useful rationale |
| You ask for code | Keep the algorithm correct and the design proportionate |
| A step is unverified | Say what is known and what still needs checking |
| You switch languages | Follow the requested language and its natural phrasing |

There is no fixed friendly persona, compulsory short answer, or universal list of forbidden words. You can still ask for detailed analysis, formal prose or a terse patch.

## Evidence and feedback

The repository includes synthetic test prompts, independent response samples, executable code checks and their limits in [the evaluation record](../evals/README.md). Examples on the showcase page are authored illustrations, clearly labeled. Neither source establishes Claude parity, a general coding guarantee, or a measured intelligence gain.

Useful feedback includes a redacted prompt, the response, the model/client when known, and what you expected. Report lost facts and broken code alongside style preferences. Never upload private conversations or credentials just to give feedback.
