from core.app import create_app
from config import settings

from core.exceptions import NonAuthenticatedException

app = create_app()

# Add routes on primary application level.


@app.get("/test-api")
def test_api ():
    raise NonAuthenticatedException
    return { "Hello": "world" }

# attic-otel: logging, tracing, RED metrics, /health. Last in the module so the
# routes above are registered before the SDK instruments the app.
from attic_otel import init_observability  # noqa: E402

init_observability(app, service_name="fastapi-boilterplate")
