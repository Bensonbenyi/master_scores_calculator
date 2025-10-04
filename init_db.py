#!/usr/bin/env python3
"""
数据库初始化脚本
在 Render 部署时自动运行
"""
import os
from app import app, db

def init_database():
    """初始化数据库"""
    with app.app_context():
        # 创建所有表
        db.create_all()
        print("数据库表创建成功！")
        
        # 检查是否有用户数据
        from app import User
        user_count = User.query.count()
        print(f"当前用户数量: {user_count}")

if __name__ == '__main__':
    init_database()
