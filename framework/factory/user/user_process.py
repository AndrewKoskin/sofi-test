import allure

from framework.api.handler.http.user import user as user_handler
from framework.models.user import User, UserCreate


class UserProcess:
    @staticmethod
    def create_user(*, user: UserCreate, serialize: bool = True, expected_status: int = 201) -> User | dict:
        with allure.step(f"Создание пользователя {user=}"):
            response = user_handler.create(data=user.model_dump(mode="json"), expected_status=expected_status)

            if serialize:
                return User.model_validate(obj=response)
            else:
                return response

    @staticmethod
    def get_user_by_id(*, user_id: int, serialize: bool = True, expected_status: int = 200) -> User | dict:
        with allure.step(f"Получение пользователя по id: {user_id=}"):
            response = user_handler.get_user_by_id(user_id=user_id, expected_status=expected_status)

            if serialize:
                return User.model_validate(obj=response)
            else:
                return response
