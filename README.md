
## Interaction schemas

<img src="readme_images/image1.png"/>
<img src="readme_images/image2.png"/>


## Database Models

```python
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(25), nullable=False, unique=True, index=True)
    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False, index=True)
    text = Column(String(200))
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    user = relationship("User", back_populates="posts")
    time_create = Column(DateTime, index=True, default=lambda: datetime.utcnow())
```

### What is `relationship` vs `ForeignKey`?

|Concept|Description|
|---|---|
|`ForeignKey`|A **column-level constraint** in the database. It links one table to another via a primary key.|
|`relationship`|A **SQLAlchemy ORM feature**. Used to define object-level access between related models in Python. Enables you to do things like `user.posts` or `post.user`.|

---

## Endpoint Parameters Validation

FastAPI allows validation of input data using `Query`, `Path`, and `Body`.

### Query Parameters

Used for values **not included in the path**, e.g.:

```python
@router.get("/")
def get_user(user_id: int = Query(..., ge=0)):
    ...
```

### Path Parameters

Used for values **included in the URL path**, e.g.:

```python
@router.delete("/{user_id}")
def delete_user(user_id: int = Path(..., ge=0)):
    ...
```

### Common Validation Options

|Parameter|Description|
|---|---|
|`ge=10`|Greater than or equal to 10|
|`gt=0`|Greater than 0|
|`le=100`|Less than or equal to 100|
|`lt=50`|Less than 50|
|`min_length=3`|Minimum string length = 3|
|`max_length=100`|Maximum string length = 100|
|`regex="^abc"`|Must match this regular expression|
