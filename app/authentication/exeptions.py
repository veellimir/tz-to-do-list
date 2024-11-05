from fastapi import HTTPException, status

UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь существует"
)

IncorrectUsernameOrPswException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Неверная логин или пароль'
)