# Sora Search API V1 (This is the test version 1 of the product, more convenient and improved versions will be released soon)

Sora Search API is a REST API for searching anime by frames, using the third-party API trace.moe.

## Functionality

- **Anime recognition by frame:** The API takes an image and returns information about the anime using the external API trace.moe.
- **REST API:** Implemented using FastAPI.
- **Integration with trace.moe:** Send an image to get search results.


## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/saykachi/Sora-Search-API.git
    cd Sora-Search-API
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Project launch

Start a server using Uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at http://0.0.0.0:8000

# Using the API

## Endpoint for searching anime

- URL: /search
- Method: POST
- Parameters:
  image (file): An image (JPEG or PNG formats) with a frame from an anime.

## Example request using curl:

```bash
curl -X POST "http://0.0.0.0:8000/search" -F "image=@path_to_your_image.jpg"
```

## Sample answer:

```bash
{
  "result": [
    {
      "anilist": 12345,
      "filename": "example.jpg",
      "episode": 1,
      "from": 10.5,
      "to": 12.0,
      "similarity": 0.9876,
      "video": "https://example.com/video.mp4",
      "image": "https://example.com/image.jpg"
    }
  ]
}
```

## Author: Saykachi Version: 1a Date: 02/21/2025
