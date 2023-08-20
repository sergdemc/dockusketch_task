from fastapi import FastAPI, Request

from .custom_logging import setup_logging

logger = setup_logging()

app = FastAPI()

logger.info("Application started")


jobs = {
    0: "Space Archaeologist",
    1: "Virtual Reality Designer",
    2: "Ethical Hacker",
    3: "Robotics Engineer",
    4: "Food Scientist",
    5: "Bioinformatics Specialist",
    6: "Nanomedicine Researcher",
    7: "AI Ethics Consultant",
    8: "Exo-Planet Tour Guide",
    9: "Oceanographer"
}


@app.get("/")
def root():
    return "Everybody be cool"


@app.get("/jobs/{job_id}")
def get_your_job(job_id: int):
    key = job_id % 10
    return f"Your job is: {jobs[key]}"


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url.path} "
                f"from {request.client.host}")
    response = await call_next(request)
    return response


@app.middleware("http")
async def log_response(request: Request, call_next):
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response


@app.exception_handler(Exception)
async def log_errors(request: Request, exc: Exception):
    logger.error(f"Error: {exc}")
    return {"Error": f"{exc}"}
