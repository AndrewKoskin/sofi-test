from framework.api.client.http.http_client import APIClient


def create(*, data: dict, expected_status: int = 201) -> dict:
    client = APIClient()
    return client.post_json(path="/users", json=data, expected_status=expected_status)


def get_user_by_id(*, user_id: int, expected_status: int = 200) -> dict:
    client = APIClient()
    return client.get_json(path=f"users/{user_id}", expected_status=expected_status)
