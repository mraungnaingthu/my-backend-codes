from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if username == "root" and password == "admin123":
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid username or password"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)