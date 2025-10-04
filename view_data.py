#!/usr/bin/env python3
"""
数据库查看脚本
用于在 Render 上查看用户数据
"""
import os
from app import app, db, User

def view_all_users():
    """查看所有用户数据"""
    with app.app_context():
        print("=" * 50)
        print("用户数据查询结果")
        print("=" * 50)
        
        # 获取所有用户
        users = User.query.all()
        
        if not users:
            print("❌ 数据库中没有用户数据")
            return
        
        print(f"📊 总用户数: {len(users)}")
        print()
        
        for i, user in enumerate(users, 1):
            print(f"👤 用户 {i}:")
            print(f"   ID: {user.id}")
            print(f"   用户名: {user.username}")
            print(f"   角色: {user.role}")
            print(f"   姓名: {user.full_name or '未填写'}")
            print(f"   学号: {user.student_id or '未填写'}")
            print(f"   专业: {user.major or '未填写'}")
            print(f"   综合成绩: {user.final_score or 0}")
            print(f"   学业成绩: {user.academic_score or 0}")
            print(f"   学术专长成绩: {user.academic_talent_score or 0}")
            print(f"   综合表现成绩: {user.comprehensive_score or 0}")
            print(f"   注册时间: {user.id}")  # 简单用ID作为注册顺序
            print("-" * 30)

def view_students_only():
    """只查看学生用户"""
    with app.app_context():
        students = User.query.filter_by(role='student').all()
        
        print("=" * 50)
        print("学生用户数据")
        print("=" * 50)
        
        if not students:
            print("❌ 没有学生用户")
            return
        
        print(f"📊 学生总数: {len(students)}")
        print()
        
        for i, student in enumerate(students, 1):
            print(f"🎓 学生 {i}:")
            print(f"   用户名: {student.username}")
            print(f"   姓名: {student.full_name or '未填写'}")
            print(f"   学号: {student.student_id or '未填写'}")
            print(f"   专业: {student.major or '未填写'}")
            print(f"   综合成绩: {student.final_score or 0}")
            print("-" * 30)

def view_teachers_only():
    """只查看教师用户"""
    with app.app_context():
        teachers = User.query.filter_by(role='teacher').all()
        
        print("=" * 50)
        print("教师用户数据")
        print("=" * 50)
        
        if not teachers:
            print("❌ 没有教师用户")
            return
        
        print(f"📊 教师总数: {len(teachers)}")
        print()
        
        for i, teacher in enumerate(teachers, 1):
            print(f"👨‍🏫 教师 {i}:")
            print(f"   用户名: {teacher.username}")
            print(f"   姓名: {teacher.full_name or '未填写'}")
            print("-" * 30)

if __name__ == '__main__':
    print("选择查看方式:")
    print("1. 查看所有用户")
    print("2. 只查看学生")
    print("3. 只查看教师")
    
    choice = input("请输入选择 (1-3): ").strip()
    
    if choice == '1':
        view_all_users()
    elif choice == '2':
        view_students_only()
    elif choice == '3':
        view_teachers_only()
    else:
        print("❌ 无效选择")
