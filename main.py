import uvicorn
from fastapi import FastAPI


async def intersection(x:int, y:int, w:int, h:int) -> tuple:
    """Функция для вычисления прямоугольника, образованного A и B.

    Прямоугольник A (0, 0, 1000, 500)
    x: x0, прямоугольник B
    y: y0, прямоугольник B
    w: ширина прямоугольника B
    h: высота прямоугольника B
    """

    # Пересечение с прямоугольником A
    new_left_x = max(0, x)
    new_right_x = min(1000, x + w)
    new_left_y = max(0, y)
    new_right_y = min(500, y + h)

    # Существует ли пересечение
    if new_left_x < new_right_x and new_left_y < new_right_y:
        return (
            new_left_x,
            new_left_y,
            new_right_x - new_left_x,
            new_right_y - new_left_y
        )
    else:
        return None


def create_fastapi_app():
    app = FastAPI()

    @app.get("/intersection")
    async def get_intersection(x:int, y:int, w:int, h:int):
        result = await intersection(x, y, w, h)
        return result

    return app


app = create_fastapi_app()
if __name__ == '__main__':
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000,
    )