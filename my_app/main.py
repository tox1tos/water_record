import uvicorn
from my_app.setup.setup import setup_app  

if __name__ == "__main__":
    app = setup_app()
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
    )

import sys
from pathlib import Path

# Добавляем путь к проекту в PYTHONPATH
sys.path.append(str(Path(__file__).parent))