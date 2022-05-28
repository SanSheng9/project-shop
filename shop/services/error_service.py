
OK = 0

URL_NOT_FOUND = 11
METHOD_NOT_ALLOWED = 12
FORBIDDEN = 13
INTERNAL_SERVER_ERROR = 14
NO_DB_CONNECTION = 15
AUTHORISATION_REQUIRED = 16
FIELD_REQUIRED = 17
INVALID_PHONE_NUMBER = 18
BAD_JSON = 19
DB_ERROR = 20
CANNOT_SEND_SMS = 21
BAD_TEMP_AUTH_TOKEN = 22
BAD_COOKIE = 23
PAYMENT_FAILED = 24
CARD_NOT_FOUND = 25
IMAGE_SAVING_ERROR = 26
SEND_PUSH_FAILED = 27
USER_NOT_FOUND = 28
CUSTOMER_REGISTRATION_REQUIRED = 29
EXECUTOR_REGISTRATION_REQUIRED = 30
ORDER_IS_ALREADY_VERIFIED = 31
BAD_IMAGE_ID = 32
BAD_CITY = 33
USER_ALREADY_REGISTERED = 34
BAD_OBJECT_ID = 35
CUSTOMER_AUTH_REQUIRED = 36
EXECUTOR_AUTH_REQUIRED = 37
ORDER_PRICE_MUST_BE_HIGHER = 38
ORDER_NOT_FOUND = 39
PAYMENT_FAILED_WITH_DESCRIPTION = 40
EXECUTOR_VERIFICATION_REQUIRED = 41
REVIEW_FORBIDDEN = 42
MULTIPLE_RESPONSES = 43
NEGATIVE_BALANCE = 44
NO_SUCH_QUESTION_TYPE = 45
WRONG_SEARCH_QUERY_CATEGORY = 46
NO_SUCH_PAYMENT_TYPE = 48
BAD_CATEGORY_ORDER_LIST = 49
BAD_REASON_LIST = 50
ORDER_CANNOT_BE_EDITED = 51
ORDER_PRICE_CUSTOMER_NOT_HAVE_ENOUGH_MONEY = 52
RATION_NOT_FOUND = 53
ORDER_CANNOT_BE_ABORTED = 54
MULTIPLE_EVENTS = 55
ORDER_CANNOT_BE_CHANGED = 56
UPDATE_NEEDED = 57
ORDER_CANNOT_BE_CREATED = 58

WRONG_TEMP_PASSWORD = 1001
WRONG_TEMP_TOKEN = 1002
WRONG_PASSWORD = 1003
WRONG_TOKEN = 1004
TEMP_SESSION_NOT_ACTIVE = 1005
TEMP_SESSION_NOT_FOUND = 1006
BAD_AGE = 1150

USER_BANNED = 2003
EXECUTOR_BANNED = 2004

CUSTOMER_PROFILE_EDITING_RESTRICTIONS = 3001
NO_EXECUTORS_AVAILABLE_FOR_ORDER = 3002
BAD_TELEGRAM_COMMAND = 3003
ORDER_IS_NOT_ON_MODERATION = 3004

exception_codes_dict = {
    URL_NOT_FOUND: ('Указанный метод не найден', 404),
    METHOD_NOT_ALLOWED: ('Указанный метод не найден', 405),
    FORBIDDEN: ('Доступ запрещен', 403),
    INTERNAL_SERVER_ERROR: ('Неизвестная ошибка', 500),
    NO_DB_CONNECTION: ('Нет соединения с базой данных', 500),
    AUTHORISATION_REQUIRED: ('Вы не авторизованы', 401),
    FIELD_REQUIRED: ('Не заполнено необходимое поле', 400),
    INVALID_PHONE_NUMBER: ('Неверный номер телефона', 400),
    BAD_JSON: ('Неверный json', 400),
    DB_ERROR: ('Неизвестная ошибка базы данных', 500),
    CANNOT_SEND_SMS: ('Ошибка при отправке смс', 500),
    BAD_TEMP_AUTH_TOKEN: ('Вы не находитесь в процессе подтверждения телефона', 403),
    BAD_COOKIE: ('Невозможно декодировать cookie', 403),
    PAYMENT_FAILED: ('Платеж не выполнен', 400),
    CARD_NOT_FOUND: ('Выбранная карта не найдена', 404),
    IMAGE_SAVING_ERROR: ('Ошибка при сохранении изображения', 500),
    SEND_PUSH_FAILED: ('Ошибка при отправке push-сообщения', 500),
    USER_NOT_FOUND: ('Пользователь не найден', 404),
    CUSTOMER_REGISTRATION_REQUIRED: ('Вы не зарегистрированы как заказчик', 403),
    EXECUTOR_REGISTRATION_REQUIRED: ('Вы не зарегистрированы как исполнитель', 403),
    ORDER_IS_ALREADY_VERIFIED: ('Заказ не нуждается в верификации', 403),
    BAD_IMAGE_ID: ('Указанный аватар не найден', 404),
    BAD_CITY: ('Указанный город не найден', 404),
    USER_ALREADY_REGISTERED: ('Пользователь уже зарегистрирован', 403),
    BAD_OBJECT_ID: ("Объект с указанным id не найден", 404),
    CUSTOMER_AUTH_REQUIRED: ('Вы не авторизированы как заказчик', 403),
    EXECUTOR_AUTH_REQUIRED: ('Вы не авторизированы как исполнитель', 403),
    ORDER_PRICE_MUST_BE_HIGHER: ('Стоимость заказа должна быть выше {:d} руб.', 403),
    ORDER_NOT_FOUND: ('Указанный заказ не найден', 404),
    PAYMENT_FAILED_WITH_DESCRIPTION: ('Платеж не выполнен: {:s}', 403),
    EXECUTOR_VERIFICATION_REQUIRED: ('Вы не верифицированы', 403),
    REVIEW_FORBIDDEN: ('Вы не можете оставить отзыв на данный заказ', 403),
    MULTIPLE_RESPONSES: ('Вы уже откликались на данный заказ', 403),
    NEGATIVE_BALANCE: ('Недостаточно средств для создания отклика. Пополните счет.', 403),
    NO_SUCH_QUESTION_TYPE: ('Неверный тип доп. вопроса', 400),
    WRONG_SEARCH_QUERY_CATEGORY: ('Указанный поисковый запрос не принадлежит указанной категории', 400),
    NO_SUCH_PAYMENT_TYPE: ('Неверный тип рассчета', 400),
    BAD_CATEGORY_ORDER_LIST: ('Неверный список категорий', 400),
    BAD_REASON_LIST: ('Неверный список причин невзятия заказа в работу', 400),
    ORDER_CANNOT_BE_EDITED: ('Вы не можете редактировать данный заказ', 403),
    ORDER_PRICE_CUSTOMER_NOT_HAVE_ENOUGH_MONEY: ('Стоимость заказа больше, чем у клиента есть на балансе {:d} руб.', 403),
    RATION_NOT_FOUND: ('На этот день не назначен рацион', 404),
    MULTIPLE_EVENTS: ('Вы уже установили рацион на этот день', 403),
    ORDER_CANNOT_BE_CREATED: ('Вы уже запланировали рацион на этот день', 403),

    WRONG_TEMP_PASSWORD: ('Неверный пароль', 403),
    WRONG_TEMP_TOKEN: ('Доступ запрещен', 403),
    WRONG_PASSWORD: ('Неверный пароль', 403),
    WRONG_TOKEN: ('Доступ запрещен', 403),
    TEMP_SESSION_NOT_ACTIVE: ('Время ожидания авторизации истекло', 403),
    TEMP_SESSION_NOT_FOUND: ('Вы не находитесь в процессе подтверждения телефона', 403),
    BAD_AGE: ('Пользователь сервиса должен быть старше 18 лет', 403),

    USER_BANNED: ('Ваш аккаунт заблокирован', 403),
    EXECUTOR_BANNED: ('Аккаунт исполнителя заблокирован', 403),

    CUSTOMER_PROFILE_EDITING_RESTRICTIONS: ('Так как Вы являетесь исполнителем, Вам недоступны для редактирования следующие поля:\nИмя и фамилия\nДень рождения', 422),
    NO_EXECUTORS_AVAILABLE_FOR_ORDER: ('Невозможно создать заказ, так как по близости от указанного Вами адреса нет ни одного специалиста, способного его выполнить.', 418),
    BAD_TELEGRAM_COMMAND: ('Неверная команда бота telegram', 400),
    ORDER_IS_NOT_ON_MODERATION: ('Заказ не находится на модерации', 403),
    ORDER_CANNOT_BE_ABORTED: ('Заказ не может быть отменён', 403),
    ORDER_CANNOT_BE_CHANGED: ('Заказ не может сменить статус', 403),
    UPDATE_NEEDED: ('Пожалуйста, обновите приложение, данный метод больше не поддерживается', 403),
}


class ErrorException(Exception):
    def __init__(self, error_code, extra=None, params=None):
        (message, http_code) = exception_codes_dict[error_code]
        if params is not None:
            message = message.format(*params)
        super().__init__(message)
        self.error_code = error_code
        self.message = message
        self.http_code = http_code
        self.extra = extra

    def to_dict(self):
        return {
            'errorCode': self.error_code,
            'description': self.message,
            'httpCode': self.http_code,
            'extra': self.extra,
        }
