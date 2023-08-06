from flask import Blueprint
from zou.app.utils.api import configure_api_from_blueprint

from .resources import (
    DesktopLoginsResource,
    NewPersonResource,
    PresenceLogsResource,
    TimeSpentsResource,
    TimeSpentMonthResource,
    TimeSpentYearResource
)

routes = [
    ("/data/persons/new", NewPersonResource),
    ("/data/persons/<person_id>/desktop-login-logs", DesktopLoginsResource),
    ("/data/persons/presence-logs/<month_date>", PresenceLogsResource),
    ("/data/persons/<person_id>/time-spents/<date>", TimeSpentsResource),
    ("/data/persons/time-spents/month-table/<year>", TimeSpentYearResource),
    ("/data/persons/time-spents/day-table/<year>/<month>", TimeSpentMonthResource)
]

blueprint = Blueprint("persons", "persons")
api = configure_api_from_blueprint(blueprint, routes)
