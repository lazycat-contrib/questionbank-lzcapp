"""Startup sequencing only; no credential logging or fixed-sleep readiness."""
import asyncio
import os
import subprocess
import sys
import time
import urllib.request

os.chdir('/app')
sys.path.insert(0, '/app')

async def wait_database():
    from sqlalchemy import text
    from sqlalchemy.ext.asyncio import create_async_engine
    engine = create_async_engine(os.environ['DB_URL'], pool_pre_ping=True)
    try:
        for attempt in range(90):
            try:
                async with engine.connect() as connection:
                    await connection.execute(text('SELECT 1'))
                return
            except Exception:
                if attempt == 89:
                    raise SystemExit('Database readiness timed out; credentials omitted.')
                await asyncio.sleep(2)
    finally:
        await engine.dispose()

mode = sys.argv[1]
if mode == 'backend':
    asyncio.run(wait_database())
    # Migration errors must prevent API startup. Avoid subprocess output exposing DB URLs.
    result = subprocess.run(['alembic', 'upgrade', 'head'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode:
        raise SystemExit('Database migration failed; API startup aborted.')
    os.execvp('fastapi', ['fastapi', 'run', 'app/main.py', '--host', '0.0.0.0', '--port', '8000'])
elif mode == 'worker':
    for attempt in range(150):
        try:
            with urllib.request.urlopen('http://backend:8000/openapi.json', timeout=3) as response:
                if response.status == 200:
                    break
        except Exception:
            pass
        if attempt == 149:
            raise SystemExit('Backend readiness timed out; worker startup aborted.')
        time.sleep(2)
    os.execvp('python', ['python', '-m', 'app.worker'])
else:
    raise SystemExit('Unknown startup role')
