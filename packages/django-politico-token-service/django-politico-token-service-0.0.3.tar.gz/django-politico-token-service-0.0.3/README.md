![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# django-politico-token-service

An authentication scheme for apps and APIs.

### Quickstart

1. Install the app.

  ```
  $ pip install django-politico-token-service
  ```

2. Add the app to your Django project and configure settings.

  ```python
  INSTALLED_APPS = [
      # ...
      'rest_framework',
      'tokenservice',
  ]
  ```

3. Create a DRF APIView in your app using the included token authentication class like this:

  ```python
  from rest_framework.permissions import IsAuthenticated
  from rest_framework.response import Response
  from rest_framework.views import APIView
  from tokenservice.authentication import TokenAuthentication

  class YourAPIView(APIView):
      authentication_classes = (
          TokenAuthentication,
      )
      permission_classes = (
          IsAuthenticated,
      )

      def get(self, request, format=None):
          return Response('GET request')

      def post(self, request, format=None):
          return Response('POST request')

  # Alternatively, you can use the TokenAuthedAPIView.
  from tokenservice.views import TokenAuthedAPIView

  class YourAPIView(TokenAuthedAPIView):
    def get(self, request, format=None):
      return Response('GET request')
  ```



4. Create an app in the tokenservice admin and use the generated token to authenticate your fetch requests like this (Note the format of the Authorization header, "Token" + whitespace + your token):

  ```javascript
  fetch('./your/api/endpoint/', {
    method: 'GET',
    headers: {
      Authorization: `Token ${YOUR_APP_TOKEN_HERE}`,
      'Content-Type': 'application/json',
    },
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
  });
  ```

5. API ALL THE THINGS!


### Developing

##### Running a development server

Developing python files? Move into example directory and run the development server with pipenv.

  ```
  $ cd example
  $ pipenv run python manage.py runserver
  ```


##### Setting up a PostgreSQL database

1. Run the make command to setup a fresh database.

  ```
  $ make database
  ```

2. Add a connection URL to the `.env` file.

  ```
  DATABASE_URL="postgres://localhost:5432/tokenservice"
  ```

3. Run migrations from the example app.

  ```
  $ cd example
  $ pipenv run python manage.py migrate
  ```

##### Testing

```
$ python example/manage.py test
```
