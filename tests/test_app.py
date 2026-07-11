from fastapi.testclient import TestClient

from src.app import activities, app


def test_unregister_participant_from_activity():
    with TestClient(app) as client:
        activity_name = "Chess Club"
        email = "teststudent@mergington.edu"

        activity = activities[activity_name]
        if email in activity["participants"]:
            activity["participants"].remove(email)

        signup_response = client.post(
            f"/activities/{activity_name}/signup?email={email}"
        )
        assert signup_response.status_code == 200
        assert email in activity["participants"]

        unregister_response = client.delete(
            f"/activities/{activity_name}/participants/{email}"
        )
        assert unregister_response.status_code == 200
        assert email not in activity["participants"]
