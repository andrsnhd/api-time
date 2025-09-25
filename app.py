from fastapi import FastAPI, Query
from datetime import datetime, timedelta, timezone

app = FastAPI(title="API Hora Local", description="Retorna a hora local baseada no GMT informado.")

@app.get("/hora")
async def get_local_time(gmt: int = Query(..., description="Deslocamento em horas do GMT, ex: -3 para GMT-3")):
    try:
        # Cria timezone com base no GMT informado
        tz = timezone(timedelta(hours=gmt))
        agora = datetime.now(tz)
        return {
            "gmt": f"GMT{gmt:+d}",
            "hora_local": agora.strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        return {"erro": str(e)}
