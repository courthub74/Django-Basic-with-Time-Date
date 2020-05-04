# Django-Basic


I used both local js/css and a CDN - Content Delivery Network


for local:

SETTINGS.PY

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/' #FOR CSS AND JS

MEDIA_URL = '/images/' #FOR IMAGE

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


FOR Datepicker (local)

<link rel="stylesheet" type="text/css" href="{% static 'css/jquery-ui.min.css' %}">
		<!--JQuery-->
		<script src="{% static 'js/jQuery-3.5.0.min.js' %}"></script>
		<!--JQuery UI-->
		<script src="{% static 'js/jquery-ui.min.js' %}"></script>


for Timepicker(CDN)

Business as usual no need for {%%}


