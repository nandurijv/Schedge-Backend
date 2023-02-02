from app import app

@app.route('/schedule')
def schedule():
    return "This is schedules page"