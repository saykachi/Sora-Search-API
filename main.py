"""
Runs a REST API using FastAPI.
Contains routes for searching anime by frame.

Sora Search API creator: @saykachii

"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from model import predict_anime
from config import TRACE_MOE_API_URL

# Create an instance of the FastAPI application
app = FastAPI(
    title="Sora Search API",
    description="API for searching anime by frames",
    version="1.0"
)

@app.post("/search", summary="Search anime by image")
async def search_anime(image: UploadFile = File(...)):
    """
    Endpoint for searching anime by uploaded image.
    
    Accepts:
      - image (file): Image (JPEG or PNG)
    
    Returns:
      JSON with search results.
    """
    # Check that the image format is supported
    if image.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Unsupported image format. Use JPEG or PNG.")
    
    try:
        # Read image content
        image_data = await image.read()
        # Call a function to predict anime from an image
        result = predict_anime(image_data)
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while processing image: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    # Starting the Uvicorn server for development
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
