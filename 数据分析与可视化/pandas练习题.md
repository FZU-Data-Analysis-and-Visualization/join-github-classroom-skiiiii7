### 一、基础创建与查看

1. 导入 pandas，用字典创建 DataFrame：

   name: Tom, Jerry, Mike

   score: 85, 92, 78

   gender: 男，女，男


   

2. 查看上述 DataFrame 的前 1 行、形状、列名、数据类型。

   

3. 用列表创建 DataFrame：

   data = [[1, "A"], [2, "B"], [3, "C"]]

   列名设为 id、tag

   

### 二、列与行操作

1. 选取 score 和 gender 两列。

   

2. 选取索引 0、2 的行。

   

3. 筛选 score>80 的行。

   

4. 新增一列 grade：score≥90 为优秀，否则为良好。

   

5. 删除 gender 列。

   

### 三、缺失值

1. 创建含缺失值的 DataFrame：

   data = {"x":[1, None, 3], "y":[None, 5, 6]}

   检测缺失值并统计每列缺失数量。

   

2. 用 0 填充缺失值；删除含缺失值的行。

   

### 四、分组聚合

1. 按 gender 分组，求 score 的均值和最大值。

   

2. 按 gender 分组，统计每组人数。

   

### 五、排序与去重

1. 按 score 升序排序。

   

2. 给 DataFrame 添加一行重复数据（如 Tom,85, 男），去重。

   

### 六、合并与拼接

1. 横向合并：

   df1 = pd.DataFrame ({"id":[1,2], "name":["X","Y"]})

   df2 = pd.DataFrame ({"id":[1,2], "age":[20,30]})

   按 id 合并。

   

2. 纵向拼接：

   df_a = pd.DataFrame ({"val":[1,2]})

   df_b = pd.DataFrame ({"val":[3,4]})

   拼接后重置索引。

   

### 七、时间处理

1. 创建时间列：["2025-01-01","2025-01-02","2025-01-03"]，转为 datetime 格式。

   

2. 提取时间列的月份、星期。

   

### 八、高级操作

1. 对 score 列做标准化（(值 - 均值)/ 标准差）。

   

2. 用透视表：行是 gender，值是 score，聚合函数为中位数。