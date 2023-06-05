from fastapi import FastAPI
import uvicorn
from routers import Oauth
app = FastAPI()


app.include_router(Oauth.router)


uvicorn.run(app)

