from app.db.session import Session
from app.models.lift import Lift
from app.shared.lift_service import LiftService


def main():
    session = Session()

    try:
        lift_service = LiftService()
        lifts = lift_service.fetch_lifts()

        for lift in lifts:
            new_lift = Lift(
                name=lift['name'],
                status=lift['status'],
                kind=lift['kind'],
                season=lift['season'],
                last_updated=lift['last_updated']
            )

            session.add(new_lift)
            session.commit()
    finally:
        session.close()


main()
