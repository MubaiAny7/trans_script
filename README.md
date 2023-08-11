# trans_script
Some transform script for team


## excel2jsonl.py
只需要命令行输入 即可快速将 表格excel 转换成 标准交付格式jsonl

>1. 使用方法：`python excel2jsonl.py example.xlsx -n prompt reference`
>2. `example.xlsx` 替换成自己的文件
>3. `-n` 参数后填写自己需要保留的列名
>4. 最后会在当前目录下生成`example.jsonl`

可以输入 `python excel2jsonl.py -h` 查看使用帮助


