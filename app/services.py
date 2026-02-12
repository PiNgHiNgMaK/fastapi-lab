from fastapi import HTTPException
from .repositories import ITaskRepository
from .models import TaskCreate, Task


class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_all()

    def create_task(self, task_in: TaskCreate):
        # Validation: ตรวจสอบว่ามี Task ที่ชื่อซ้ำอยู่หรือไม่
        existing_task = self.repo.get_by_title(task_in.title)
        if existing_task:
            raise HTTPException(
                status_code=400, 
                detail=f"Task with title '{task_in.title}' already exists"
            )
        return self.repo.create(task_in)
    
    def complete_task(self, task_id: int) -> Task:
        """Mark a task as complete"""
        task = self.repo.get_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        
        # สร้าง updated task โดยเปลี่ยน completed เป็น True
        updated_task = Task(
            id=task.id,
            title=task.title,
            description=task.description,
            completed=True
        )
        return self.repo.update(updated_task)
