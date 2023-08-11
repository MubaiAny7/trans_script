import jsonlines
import pandas as pd
import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="jsonl转excel脚本")
    parser.add_argument("inputfile", type=str, help="要转换的jsonl文件")
    parser.add_argument("-n", type=str, nargs="+", default=["prompt",'response'], help="需要保存到表格的字段 以空格做间隔 默认是prompt+response")
    parser.add_argument("-index", type=int, default=True, help="表格是否要保留自动生成的idx 默认保留")
    args = parser.parse_args()
    
    f = jsonlines.open(args.inputfile)
    
    df = pd.DataFrame(f)
    need = pd.DataFrame(df,columns=args.n)
    need.to_excel(f"{args.inputfile.split('.')[0]}.xlsx",index=True if args.index==1 else False)
    