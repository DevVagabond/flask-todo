from pydantic import BaseModel, ValidationError, validator
import enum


class StatusEnum(enum.Enum):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    ARCHIVED = 'archived'
    PENDING = 'pending'
    COMPLETED = 'completed'


class TaskModel(BaseModel):
    taskId: str
    title: str
    description: str
    status: str

    @validator('title')
    def validate_title(cls, v):
        if len(v) < 3:
            raise ValueError('Title must be at least 3 characters long')
        return v

    @validator('description')
    def validate_description(cls, v):
        if len(v) < 10:
            raise ValueError('Description must be at least 10 characters long')
        return v

    @validator('status')
    def validate_status(cls, v):
        if v not in [e.value for e in StatusEnum]:
            raise ValueError('Status must be one of the following: {}'.format(
                ', '.join([e.value for e in StatusEnum])
            ))
        return v
