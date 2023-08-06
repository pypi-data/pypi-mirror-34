from CheKnife.security import DjangoDatabaseSettings

store = DjangoDatabaseSettings('/tmp/django.test')
print(store.settings('db3'))
