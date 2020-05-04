# Django-Basic


I used both local js/css and a CDN - Content Delivery Network


for local:

<u>SETTINGS.PY</u>

STATIC_URL = '/static/' #FOR CSS AND JS

MEDIA_URL = '/images/' #FOR IMAGE

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


<u>FOR Datepicker (local)</u>

<link rel="stylesheet" type="text/css" href="{% static 'css/jquery-ui.min.css' %}">
		<!--JQuery-->
		<script src="{% static 'js/jQuery-3.5.0.min.js' %}"></script>
		<!--JQuery UI-->
		<script src="{% static 'js/jquery-ui.min.js' %}"></script>


<u>for Timepicker(CDN)</u>

Business as usual no need for {%%}


