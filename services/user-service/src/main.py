from fastapi import FastAPI, HTTPException

app = FastAPI()

# In-memory database for user management
users = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to the User Management Service!"}

@app.get("/users")
def get_users():
    return {"users": list(users.values())}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users")
def create_user(user_id: int, name: str, email: str):
    if user_id in users:
        raise HTTPException(status_code=400, detail="User ID already exists")
    users[user_id] = {"id": user_id, "name": name, "email": email}
    return {"message": "User created successfully"}

@app.put("/users/{user_id}")
def update_user(user_id: int, name: str = None, email: str = None):
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if name:
        user["name"] = name
    if email:
        user["email"] = email
    return {"message": "User updated successfully"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": "User deleted successfully"}
