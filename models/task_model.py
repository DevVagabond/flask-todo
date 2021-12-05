import enum


class StatusEnum(enum.Enum):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    ARCHIVED = 'archived'
    PENDING = 'pending'
    COMPLETED = 'completed'
