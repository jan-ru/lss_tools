# run.py
import uvicorn

if __name__ == "__main__":
    port = 8000
    print(f"Serving on http://localhost:{port}")
    print("Available routes:")
    print(f"  - PyScript Console: http://localhost:{port}/")
    print(f"  - Sum Calculator: http://localhost:{port}/calculator")
    print("Press CTRL+C to stop the server")
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)
