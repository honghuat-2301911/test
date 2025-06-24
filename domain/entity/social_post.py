"""Module defining social media domain entities."""

from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Post:
    """Represents a social media post.
    
    Attributes:
        post_id: Unique identifier for the post
        user: Author of the post
        content: Text content of the post
        created_at: Timestamp of post creation
        image_url: Optional URL for post image
        likes: Number of likes (default 0)
        comments: List of associated comments
    """
    post_id: int
    user: str
    content: str
    created_at: str
    image_url: Optional[str] = None
    likes: int = 0
    comments: List['Comment'] = field(default_factory=list)

@dataclass
class Comment:
    """Represents a comment on a social media post.
    
    Attributes:
        comment_id: Unique identifier for the comment
        post_id: ID of the parent post
        user: Author of the comment
        content: Text content of the comment
        created_at: Timestamp of comment creation
    """
    comment_id: int
    post_id: int
    user: str
    content: str
    created_at: str
