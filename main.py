from deta import Deta
from fastapi import FastAPI


deta = Deta('c0vijxjf_9e2oyhDqFh12kgaMQ9UfjDcxi7h6MBmi')
db = deta.Base('program_koperasi')
db.put({'key': 'access', 'status': False})
app = FastAPI()


@app.get('/get_access')
def get_access():
    return db.get('access')


@app.post('/toggle_access/{open}/12457')
def toogle_acces(open: bool):
    return db.put({'key': 'access', 'status': open})
