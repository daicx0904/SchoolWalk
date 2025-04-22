INSTALLED_APPS = [
    'api.apps.ApiConfig',  # 注册应用
    'django.contrib.gis'
]
TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'frontend/assets')],  # 前端模板路径
    }
]
