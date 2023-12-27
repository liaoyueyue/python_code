# 某学院举办的“大学好声音” 歌手大赛中，有10位评审嘉宾，对每一位选手进行打分。成绩统计规则是：评分大于等于65，且小于等于95分才是有效打分，在有效打分中去掉一个最高分，去掉一个最低分之后，取平均分，保留两位小数。请编写程序，进行成绩统计。
# 输入：根据提示，依次输入10个嘉宾的评分，输出：选手的最终得分，例如10个评分是：65, 75, 80, 83, 78, 91, 92, 88, 96 ,80，去掉无效得分96后，去掉最高分92，去掉最低分65，再取平均分，保留两位小数，结果是：82.14分。

scores = input("请输入10个嘉宾的评分，用逗号隔开：").split(',')
valid_scores = [int(score) for score in scores if 65 <= int(score) <= 95]
valid_scores.sort()
valid_scores = valid_scores[1:-1]
average_score = round(sum(valid_scores) / len(valid_scores), 2)
print(f"选手的最终得分是：{average_score}分")
