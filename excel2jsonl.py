import jsonlines
import pandas as pd
import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="excel转jsonl脚本")
    parser.add_argument("inputfile", type=str, help="输入文件名")
    # parser.add_argument("" ,type=str, help="Output file to save result")
    parser.add_argument("-n" ,type=str, default=["prompt","response"], nargs="+",help="需要保存的列名 以空格做间隔 默认是prompt+response")

    args = parser.parse_args()
    f = pd.read_excel(args.inputfile)

    df = pd.DataFrame(f,columns = args.n)
    need = df.to_dict(orient="records")
    g = jsonlines.open(f"{args.inputfile.split('.')[0]}.jsonl","w")
    for i in need:
        g.write(i)
