import seaborn as sns

sns.set_style("whitegrid")
tips = sns.load_dataset("tips") #载入自带数据集
#研究三个变量之间的关系,是否抽烟与日期为分类变量,消费是连续变量
#结论发现吸烟者在周末消费明显大于不吸烟的人
ax = sns.boxplot(x="day", y="total_bill", hue="smoker",data=tips, palette="Set3")