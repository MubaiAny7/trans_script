import random
import argparse
import jsonlines
from datetime import datetime,timedelta



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="随机选择每日吵架倒霉蛋")
    parser.add_argument("nums",type=int,default=6,help="倒霉蛋个数")
    args = parser.parse_args()
    
    today = datetime.now().date()
    tomorrow = today + timedelta(days=4)
    seed_value = int(tomorrow.strftime('%Y%m%d')) + 10086
    random.seed(seed_value)
    print(f"日期:{tomorrow}")
    print(f"倒霉蛋个数:{args.nums}")
    temp = {"date":str(tomorrow),"nums":args.nums,"seed":seed_value}
    
    rand_list = [ "毕月安",
            "黄昊",
            "胡青云",
            "凌晓盈",
            "李梦飞",
            "李英如",
            "王佳琛",
            "王佳鹏",
            "王思瑜",
            "杨华",
            "张夏葳",
            "陈陆",
            "张颖",
    ]
    g = jsonlines.open("./checker_by_date.jsonl",'a')
    
    rand = list(random.sample(rand_list[:11],args.nums))
    temp["倒霉蛋"] = rand
    g.write(temp)
    print(f"{tomorrow} 的{args.nums}个倒霉蛋为"," ".join(rand),"恭喜!")
    