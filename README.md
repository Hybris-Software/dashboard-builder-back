# OUTDATED DOCUMENTATION

# Django template documentation

## 1 - Authentication

This app uses `django-rest-knox` for rest framework token authentication.

This app provides all the basic user management features: login, registration, logout, password change, password reset, and email confirmation.

In models.py is the basic user template that can be customized by adding or removing fields. It is set up to accept multiple types of users. The user type is defined by the `Type` enum within the `User` model.

The username can contain only lowercase english letters, numbers and `. + - _`.

### 1.1 - Features

**OTP**

TBD

**Token**

TBD

**Registration**

Registration is set up for different types of users. There is a serializer for each user; the appropriate one is chosen based on the `userType` field. This behavior is defined by the `get_serializer_class` function in `RegisterView`, to add a new user type you must create the new serializer by extending `GenericRegisterSerializer` and add it to `get_serializer_class`.

If you add new fields to the `User` model you must also add it to the serializer for registration: the `General` one if the field is required for anyone, otherwise only in the specific serializer.

**Login**

The login can be done with username, password or both; it is set via `AUTHENTICATION_METHOD` in `authentication/settings.py`.

You can also choose to require an OTP at login. If `AUTHENTICATION_LOGIN_OTP` in `authentication/settings.py` is set to false, the login call returns the authentication token directly; conversely, the response contains a temporary token and an OTP is emailed, sending both to the confirmation url will get the authentication token.

**User info**

The endpoint for requesting user information returns everything except protected fields (`password`) or for Django's internal use (such as `is_superuser`). This behavior is defined by `UserSerializer`.

### 1.2 - Endpoints

**TBD**

### 1.3 - Settings

| Name                                | Default    | Notes                                       |
| ----------------------------------- | ---------- | ------------------------------------------- |
| AUTHENTICATION_METHOD               | email      | Login with email and/or username            |
| AUTHENTICATION_SIGNED_TOKEN_MAX_AGE | 30 minutes | Max age for token signed via TokenManager   |
| AUTHENTICATION_LOGIN_OTP            | True       | If the user should provide an OTP to log in |
| AUTHENTICATION_OTP_DURATION         | 10 minutes | The duration of an OTP                      |

## 2 - Job

Job posting and application submission.

Offers are added via Django's admin panel; there are no endpoints to add them.

### 2.1 - Dependencies

- generic_celery for sending email. Can be replaced with django's `send_mail` function in `views.py`

### 2.2 - Customization

All the models can be updated freely (remember to `makemigrations`), the serializers will require the correct fields automatically.

The email template can be updated too. It is placed in the `templates` folder.

**Settings:**

| Name                           | Default      | Notes                                                             |
| ------------------------------ | ------------ | ----------------------------------------------------------------- |
| JOB_APPLICATION_EMAIL_RECEIVER | EMAIL_SENDER | The email address that receives the new application notifications |
| JOB_APPLICATION_EMAIL_SENDER   | EMAIL_SENDER | The application notification's sender address                     |

### 2.3 - Endpoints

#### 2.3.1 - Show offer info

```
GET offers/<int:id>/

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "jobName": "Tet",
    "visible": true,
    "creationDate": "2022-09-17",
    "expireDate": "2022-09-17",
    "shortDescription": "asfsdafasdfsad",
    "longDescription": "asdfasdfsd",
    "location": "asdfsa",
    "specialist": "sadfsad",
    "jobType": "asdfsadf",
    "contactPerson": "asdfas",
    "phone": "sdfasdfsadfsadfs",
    "email": "sdiufhiuyg@no.it"
}
```

#### 2.3.2 - Show offer list

```
GET offers/?limit=5&page=1

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "jobName": "Tet",
            "visible": true,
            "creationDate": "2022-09-17",
            "expireDate": "2022-09-17",
            "shortDescription": "asfsdafasdfsad",
            "longDescription": "asdfasdfsd",
            "location": "asdfsa",
            "specialist": "sadfsad",
            "jobType": "asdfsadf",
            "contactPerson": "asdfas",
            "phone": "sdfasdfsadfsadfs",
            "email": "sdiufhiuyg@no.it"
        }
    ]
}
```

#### 2.3.3 - Send application

```
POST applications/

HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "submissionDate": "2022-09-17T07:23:03.630163Z",
    "firstName": "asdfsadf",
    "lastName": "uhuhiuboh",
    "email": "hihyugboiuh@no.ut",
    "country": "uihliuhuu",
    "phone": "23874283",
    "cv": "http://localhost:8000/media/outrun-wallpaper-2880x1800.jpg",
    "coverLetter": "iuhgyuiughyuh",
    "skillsLevels": "khuygyiuhuyg",
    "workChangeStatus": true,
    "vatStatus": true,
    "hoursPerDay": 1,
    "jobOffer": 1
}
```

## 3 - Generic Celery

### 3.1 - Configuration

| Name                  | Default value |
| --------------------- | ------------- |
| CELERY_BROKER_URL     | REDIS_URL     |
| CELERY_RESULT_BACKEND | REDIS_URL     |

## 5 - FAQ

A simple app that allows backoffice users to add FAQs and anonymous users to retrieve them.

There is not an endpoint to create FAQs so it has to be done in the Django Admin panel.

### 5.1 - Endpoints

#### 5.1.1 - Get FAQs

```
GET /

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "question": "Testquestion",
        "answer": "Hello folks!"
    }
]
```

## 6 - Reviews

A simple app that allows backoffice users to add reviews and anonymous users to retrieve them.

There is not an endpoint to create reviews so it has to be done in the Django Admin panel.

### 6.1 - Endpoints

#### 6.1.1 - Get reviews (with optional tag filter)

```
GET /?tag=nope

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "name": "Riccardo Tornesello",
        "photo": "http://localhost:8000/media/reviews/outrun-wallpaper-3840x2160.jpg",
        "message": "It works!",
        "stars": 5,
        "tag": "nope"
    }
]
```

# Environment variables

## Generic (Required)

| Name                 | Default value for dev | Default value | Notes                       |
| -------------------- | --------------------- | ------------- | --------------------------- |
| SECRET_KEY           | django-insecure       |               |                             |
| PROJECT_NAME         | djangoapp             |               | Used sometimes for prefixes |
| DEBUG                | True                  | False         |                             |
| ALLOWED_HOSTS        | \*                    |               |                             |
| ADMIN_PANEL          |                       | True          |                             |
| CORS_ALLOWED_ORIGINS | \*                    |               |                             |
| CSRF_TRUSTED_ORIGINS | \*                    |               |                             |

## Database (Required)

| Name        | Default value for dev | Default value |
| ----------- | --------------------- | ------------- |
| DB_HOST     | database              |               |
| DB_PORT     | 5432                  |               |
| DB_DB       | app_db                |               |
| DB_USER     | app_db                |               |
| DB_PASSWORD | app_db                |               |
| DB_SSL      |                       | False         |

## Default redis database

| Name      | Default value for dev | Default value |
| --------- | --------------------- | ------------- |
| REDIS_URL | redis://redis:6379/0  |               |

## MinIO

| Name                              | Default value                      |
| --------------------------------- | ---------------------------------- |
| MINIO_ENDPOINT                    |                                    |
| MINIO_EXTERNAL_ENDPOINT           | MINIO_ENDPOINT                     |
| MINIO_USE_HTTPS                   | True                               |
| MINIO_EXTERNAL_ENDPOINT_USE_HTTPS | MINIO_USE_HTTPS                    |
| MINIO_ACCESS_KEY                  |                                    |
| MINIO_SECRET_KEY                  |                                    |
| MINIO_MEDIA_FILES_BUCKET          | _PROJECT_NAME_-media-files-bucket  |
| MINIO_STATIC_FILES_BUCKET         | _PROJECT_NAME_-static-files-bucket |
| MINIO_EXTRA_PRIVATE_BUCKETS       |                                    |
| MINIO_EXTRA_PUBLIC_BUCKETS        |                                    |

## Email

| Name                | Default value |
| ------------------- | ------------- |
| EMAIL_HOST          |               |
| EMAIL_HOST_PASSWORD |               |
| EMAIL_HOST_USER     |               |
| EMAIL_PORT          |               |
| EMAIL_USE_TLS       | False         |
| EMAIL_USE_SSL       | False         |
| EMAIL_SENDER        |               |

## Contact form

| Name                       | Default value |
| -------------------------- | ------------- |
| CONTACTFORM_EMAIL_RECEIVER | EMAIL_SENDER  |

## Channels

| Name               | Default value |
| ------------------ | ------------- |
| CHANNELS_REDIS_URL | REDIS_URL     |
