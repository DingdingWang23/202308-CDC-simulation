import os
input_folder = r"C:\\Users\\丁丁\\Desktop\\report"

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(input_folder, filename)
        print(filename)

        score_3 = 0
        score_4 = 0
        score_5 = 0
        with open(filepath, 'r', encoding='gbk') as file:
            content = file.read()
            print(content)
            task_1 = content.split("对延安精神的理解：")[0]
            others = content.split("对延安精神的理解：")[1]
            task_3 = others.split("联系实际的内容：")[0]
            others_1 = others.split("联系实际的内容：")[1]
            task_4 = others_1.split("提到了延安的史实：")[0]
            others_2 = others_1.split("提到了延安的史实：")[1]
            task_2_1 = others_2.split("提到了延安的著作：")[0]
            others_3 = others_2.split("提到了延安的著作：")[1]
            task_2_2 = others_3.split("与延安精神相关的其他角度包括：")[0]
            task_5 = others_3.split("与延安精神相关的其他角度包括：")[1]

        if "无" in task_2_1:
            score_2_1 = 0
        elif "2." in task_2_1:
            score_2_1 = 2
        else:
            score_2_1 = 1

        if "无" in task_2_2:
            score_2_2 = 0
        else:
            score_2_2 = task_2_2.count("《")
            if score_2_2 > 2:
                score_2_2 = 2

        lines = task_3.split("\n")
        for line in lines:
            if len(line) > 4 and "未提及" not in line and "没有提及" not in line and " 无" not in line and " -" not in line and "|  |" not in line :
                score_3 += 1

        lines = task_4.split("\n")
        for line in lines:
            if len(line) > 4 and "未提及" not in line and "没有提及" not in line and " 无" not in line and " -" not in line and "|  |" not in line :
                score_4 += 1

        if "无" in task_5:
            score_5 = 0
        else:
            score_5 = (1+task_5.count("；"))*0.5

        with open(filepath, 'a') as f:
            f.write("\n")

            f.write("\n")
            f.write("延安精神的史实得分：")
            f.write(str(score_2_1))
            f.write("\n")
            f.write("延安精神的著作得分：")
            f.write(str(score_2_2))
            f.write("\n")
            f.write("延安精神的理解得分：")
            f.write(str(score_3))
            f.write("\n")
            f.write("延安精神的联系实际得分：")
            f.write(str(score_4))
            f.write("\n")
            f.write("延安精神的其他角度得分：")
            f.write(str(score_5))
            f.write("\n")

            f.write("总得分：")
            f.write(str(score_2_1+score_2_2+score_3+score_4+score_5))
            f.write("\n")
