# 将Markdown中的数学公式标识转换成LaTex中的数学公式标识

## 需求分析

在 Markdown 中插入数学公式时，我们使用的是如下的格式：

```
$数学公式$
```

或者：

```
$$数学公式$$
```

而在有些地方则要求使用 LaTex 语法才能表示这是一个数学公式，例如在 WordPress 中插入数学公式的时候。这时，我们就需要把 Markdown 中的数学公式标识符转换成 LaTex 语法中的数学公式标识符。转换完成之后应该是这个样子的：

```
[latex]数学公式[/latex]
```

手动替换这些标识符很是机械且繁琐，于是我就写了一个程序来完成。这个目录下的 `1.py` Python 小程序就可以自动完成这项工作。

## 运行环境
