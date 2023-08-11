# trans_script
Some transform script for team


## excel2jsonl.py
命令行输入 即可快速将 表格excel 转换成 标准交付格式jsonl

>1. 使用方法：`python excel2jsonl.py example.xlsx -n prompt reference`
>2. `example.xlsx` 替换成自己的文件
>3. `-n` 参数后填写自己需要保留的列名
>4. 最后会在当前目录下生成`example.jsonl`

可以输入 `python excel2jsonl.py -h` 查看使用帮助


## jsonl2excel.py
命令行输入 即可快速将 标准数据格式jsonl 转换成 表格excel

>1. 使用方法`python jsonl2excel.py example.jsonl -n prompt response -index 0`
>2. `example.jsonl`替换成自己的文件
>3. `-n`参数后填写需要保留的字段
>4. `-index` option:1/0 表示是否需要保存自动生成的idx
>5. 最后会在当前目录下生成`example.xlsx`

可以输入`python jsonl2excel.py -h`查看使用帮助