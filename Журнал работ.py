from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)


@app.route("/")
def work_log():
    db_session.global_init("db/mars.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    # for job in db_sess.query(Jobs).all():
    #     jobs.append((job.job, job.team_leader, job.work_size, job.collaborators, job.is_finished))
    return render_template("jobs_list.html", jobs=jobs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
