class ApiError(Exception):
    def __init__(self, *args, message: str, secret_message: str = None):
        super().__init__(*args)
        self.message = message
        self.secret_message = secret_message

    @staticmethod
    def bad_request(message: str):
        return ApiError(message=message)

    @staticmethod
    def unregistered():
        return ApiError(message="Вы не зарегистрированы или пока не прошли модерацию")

    @staticmethod
    def validation_error(message: str = "Ошибка валидации"):
        return ApiError(message=message)

    @staticmethod
    def internal_error(secret_message: str = None):
        return ApiError(message="Что-то пошло не так", secret_message=secret_message)

    @staticmethod
    def no_permission():
        return ApiError(message="Недостаточно прав")
