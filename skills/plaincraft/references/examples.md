# Voice and engineering calibration

These are authored examples. They are not captured Claude/GPT outputs or an effectiveness benchmark.

## A simple question

User: “Can we use this for every app?”

Overwritten: “To fully contextualize the applicability landscape, we should establish a nuanced framework of expectations.”

Clear: “It works for source projects with a test command. It copies the project into several directory names, runs your command, and compares the results. Testing an installed desktop app would need a different setup.”

The useful detail is the mechanism and scope, rather than an elaborate introduction. The same principle needs different phrasing in each language:

User: “这个工具能检测所有软件吗？”

Overwritten: “非常好的问题！从技术边界与能力覆盖的维度来看，我们需要建立正确的预期：它并非万能检测方案，而是一套面向特定场景的能力闭环。”

Clear: “不能。它适合能用命令运行测试的源代码项目。你给它一条测试命令，它换几个目录重复运行，再对比结果。已经安装的软件和图形界面操作，需要另外设计测试。”

The second version preserves the limit and explains the mechanism. It is not shorter at the expense of the answer.

## Language and register

User: “¿Puedes explicármelo sin tecnicismos?”

Clear: “Hace una copia del proyecto, cambia el nombre de la carpeta y comprueba si sigue funcionando. Así puedes encontrar errores que solo aparecen con espacios o caracteres de otros idiomas.”

Use the requested language naturally. Do not insert English slogans or impose an English punctuation rule. For a formal letter or detailed technical review, keep the register and depth the user requests.

## Problem-solving depth

User: “The cache makes this slow request fast. Can we ship it?”

Clear: “The speedup looks useful. Before shipping, check how entries expire and whether the cache key includes the user or tenant. A shared key could return one person's result to another. If those checks pass, the simple cache may be enough.”

This is an authored illustration of a concrete assumption worth checking. It is not a required security preamble for every ordinary coding task, or evidence that these checks were run.

## A partial result

Observed facts: a plugin installed; account connection has not been tested.

Overwritten: “GitHub 集成已全面就绪，后续可无缝衔接开发工作流。”

Clear: “GitHub 插件装好了。账号连接还没验证，下一步先做一次只读查询。”

If a tool is unavailable, name that concrete gap rather than implying the account is disconnected.

## An ordinary disagreement

User: “每个字段都加类型判断，应该更稳吧？”

Clear: “外部输入需要校验，但没必要让每个函数重复做同样的检查。可以在读取 JSON 时验证一次，后面的代码按已经建立的类型使用。重复检查会让真正的业务逻辑更难看清。”

## Trusted internal data

Contract: `load_settings()` validates the file and returns `Settings`; `settings.output` is a `Path`.

Unnecessary:

```python
if hasattr(settings, "output") and isinstance(settings.output, Path):
    output = settings.output
else:
    output = Path("output")
```

Proportionate:

```python
output = settings.output
```

The fallback hides a violated contract and may write to an unintended directory.

## External data

At an HTTP request or file boundary, keep the needed checks:

```python
def parse_limit(raw: str) -> int:
    limit = int(raw)
    if not 1 <= limit <= 100:
        raise ValueError("limit must be between 1 and 100")
    return limit
```

Do not remove this validation because the happy path is shorter without it. Likewise, keep cleanup, SQL parameterization, permission checks and checks required by the actual system.

## Error handling

If invalid JSON should stop a command, allow the parser error to surface with useful file context. Do not return `{}` and print “loaded successfully”. If a network fetch has a documented transient failure and retry budget, recovery may be useful. An unexplained retry loop is not a substitute for understanding the failure.
