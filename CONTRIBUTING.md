# 贡献指南 Contributing Guide

感谢你对这个项目的兴趣！我们欢迎任何形式的贡献。

## 如何贡献

### 报告问题 Bug Reports
如果你发现了bug，请：
1. 检查是否已有相同的issue
2. 创建新的issue，详细描述问题
3. 包含重现步骤和环境信息

### 功能建议 Feature Requests
如果你有新功能的想法：
1. 创建issue描述你的建议
2. 解释为什么这个功能有用
3. 提供可能的实现方案

### 代码贡献 Code Contributions
1. Fork这个仓库
2. 创建你的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的改动 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建Pull Request

### 开发环境设置
```bash
# 克隆仓库
git clone https://github.com/Bensonbenyi/master_scores_calculator.git
cd master_scores_calculator

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 运行应用
python app.py
```

### 代码规范
- 遵循PEP 8 Python代码规范
- 添加适当的注释和文档字符串
- 保持代码简洁易读
- 使用有意义的变量和函数名
- 每个函数不超过50行代码
- 添加类型提示（推荐）

### 测试要求
- 新功能必须包含相应的测试用例
- 测试覆盖率应保持在80%以上
- 运行测试：`python -m pytest tests/`

### 数据库迁移
- 修改模型后需要创建迁移文件
- 使用命令：`flask db migrate -m "描述变更"`
- 应用迁移：`flask db upgrade`

### 提交信息格式
- 使用清晰的提交信息
- 中英文均可
- 格式：`类型: 简短描述`

示例：
- `feat: 添加学生成绩导出功能`
- `fix: 修复登录页面样式问题`
- `docs: 更新README文档`

## 行为准则

请保持友好和专业的态度。我们致力于为每个人创造一个开放和包容的环境。

## 问题和支持

如果你有任何问题，可以：
- 创建GitHub Issue
- 查看现有的Issues和Pull Requests

再次感谢你的贡献！
