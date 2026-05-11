from fastapi import FastAPI, UploadFile, File
from fastapi import File
app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "File Upload API",
        "usage": "Send a POST request to /uploadfile/ with a file"
    }


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:

        filename = file.filename

        content = await file.read()
        with open(filename, "wb") as f:
            f.write(content)

        return {
            "message": f"File uploaded successfully!",
            "original_filename": filename,  # This will be the user's filename
            "saved_as": filename
        }
    except Exception as e:
        return {"error": str(e)}