import allure
from hamcrest import assert_that, has_entries

from framework.factory.user.user_process import UserProcess
from framework.models.user import UserCreate


@allure.feature("Тестирование менеджмента пользователей")
class TestUser:
    @allure.title("Создание валидного пользователя")
    @allure.link("https://link-to-some-ticket.com")
    def test_create_user(self, valid_user: UserCreate):
        with allure.step("Создание пользователя"):
            created_user = UserProcess.create_user(user=valid_user)

            assert_that(
                created_user.model_dump(),
                has_entries(**valid_user.model_dump()),
                "В итоговом пользователе не совпадают поля с пользователем из запроса",
            )

        with allure.step("Поиск и проверка пользователя"):
            found_user = UserProcess.get_user_by_id(user_id=created_user.id)

            # assert тоже можно применять, он более примитивен и не так кррасиво показывает ошибки в аллюре
            # Также в идеале применять один подход на проекте (или хотя бы один подход в рамках одного файла)
            # Поэтому лучше выбрать, что использовать сразу. assert синтаксис легкий, поэтому дальше используем hamcrest
            assert found_user == valid_user, "Созданный пользователь в ручке поиска не совпадает с создаваемым"
