# 学生成绩管理系统

一个基于Flask的学生成绩管理系统，支持学生信息管理、成绩录入和导出等功能。

## 功能特性

- 🔐 用户注册和登录（学生/教师角色）
- 👥 学生信息管理
- 📊 成绩录入和计算
- 📁 文件上传功能
- 📈 成绩导出（Excel格式）
- 🎨 现代化的用户界面

## 技术栈

- **后端**: Flask, SQLAlchemy, Flask-Migrate
- **前端**: HTML, CSS, JavaScript
- **数据库**: SQLite
- **文件处理**: openpyxl

## 快速开始

### 环境要求

- Python 3.7+
- pip

### 安装步骤

1. 克隆项目
```bash
git clone https://github.com/你的用户名/front_end.git
cd front_end
```

2. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 初始化数据库
```bash
flask db upgrade
```

5. 运行应用
```bash
python app.py
```

应用将在 `http://localhost:5000` 启动。

## 项目结构

```
front_end/
├── app.py                 # 主应用文件
├── requirements.txt       # 依赖列表
├── baoyan_rules.md       # 保研规则说明
├── html_files/           # HTML模板文件
│   ├── login.html
│   ├── register.html
│   ├── stu_page.html
│   └── ...
├── static/              # 静态文件
│   ├── styles/         # CSS样式文件
│   └── uploads/        # 上传文件目录
├── migrations/         # 数据库迁移文件
└── instance/          # 数据库文件（生产环境）
```

## 使用说明

### 教师功能
- 登录后可以查看所有学生信息
- 录入和编辑学生成绩
- 导出学生成绩表

### 学生功能
- 注册和登录
- 查看个人信息和成绩
- 上传相关证明文件

## 贡献

欢迎提交Issue和Pull Request来帮助改进这个项目！

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。
