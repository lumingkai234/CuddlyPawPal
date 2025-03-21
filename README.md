# CuddlyPawPal

CuddlyPawPal 是一款 AI 玩偶的后端服务项目，支持玩偶通过 4G 网络与服务器交互，实现语音上传、语音转文本、大模型问答以及文本转语音的完整流程。该项目主要用于景区景点的讲解服务。

---

## 项目目录结构

```
CuddlyPawPal/
├── manage.py
├── CuddlyPawPal/
│   ├── __init__.py
│   ├── settings.py          # 项目配置
│   ├── urls.py              # 全局路由
│   ├── wsgi.py              # WSGI 入口
│   └── asgi.py              # ASGI 入口
├── api/                     # 核心 API 应用
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py            # 数据模型
│   ├── views.py             # 视图逻辑
│   ├── urls.py              # 应用路由
│   ├── serializers.py       # 序列化器
│   └── services/            # 服务逻辑（语音转文本、大模型、TTS）
│       ├── __init__.py
│       ├── speech_to_text.py
│       ├── text_to_speech.py
│       └── large_model.py
├── media/                   # 存储上传的音频文件
├── static/                  # 静态文件（如前端资源）
└── templates/               # 模板文件（如管理后台扩展）
```

---

## **项目目录说明与代码规范**

### **1. 项目根目录**
#### **`manage.py`**
- **功能**：Django 项目的管理脚本，用于运行服务器、迁移数据库等。
- **无需修改**，保持默认即可。

---

### **2. CuddlyPawPal**
#### **`__init__.py`**
- **功能**：标识该目录为 Python 包。
- **无需修改**，保持为空即可。

#### **`settings.py`**
- **功能**：项目的全局配置文件。
- **编写建议**：
  - 使用环境变量管理敏感信息（如 `SECRET_KEY`、数据库配置）。
  - 配置静态文件和媒体文件路径。
  - 确保 `INSTALLED_APPS` 包含所有必要的应用。
- **代码规范**：
  ```python
  import os
  from pathlib import Path

  BASE_DIR = Path(__file__).resolve().parent.parent

  SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-default-secret-key')

  DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

  ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',')
  ```

#### **`urls.py`**
- **功能**：全局路由配置。
- **编写建议**：
  - 将应用的路由通过 `include` 引入，保持文件简洁。
- **代码规范**：
  ```python
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/', include('api.urls')),  # 引入 API 应用的路由
  ]
  ```

#### **`wsgi.py` 和 `asgi.py`**
- **功能**：项目的 WSGI 和 ASGI 入口文件。
- **无需修改**，保持默认即可。

---

### **3. `api/`**
#### **`__init__.py`**
- **功能**：标识该目录为 Python 包。
- **无需修改**，保持为空即可。

#### **`admin.py`**
- **功能**：注册模型到 Django 管理后台。
- **编写建议**：
  - 注册所有需要在后台管理的模型。
- **代码规范**：
  ```python
  from django.contrib import admin
  from .models import TouristSpot

  @admin.register(TouristSpot)
  class TouristSpotAdmin(admin.ModelAdmin):
      list_display = ('name', 'created_at')
      search_fields = ('name',)
  ```

#### **`apps.py`**
- **功能**：应用的配置文件。
- **无需修改**，保持默认即可。

#### **`models.py`**
- **功能**：定义数据库模型。
- **编写建议**：
  - 使用清晰的字段命名。
  - 添加 `__str__` 方法，便于调试。
- **代码规范**：
  ```python
  from django.db import models

  class TouristSpot(models.Model):
      name = models.CharField(max_length=100)
      description = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return self.name
  ```

#### **`views.py`**
- **功能**：处理 API 请求。
- **编写建议**：
  - 使用 Django REST Framework 的 `APIView` 或 `ViewSet`。
  - 遵循单一职责原则，每个视图只处理一个功能。
- **代码规范**：
  ```python
  from rest_framework.views import APIView
  from rest_framework.response import Response

  class AudioProcessingView(APIView):
      def post(self, request):
          # 处理音频上传和处理逻辑
          return Response({"message": "success"})
  ```

#### **`urls.py`**
- **功能**：定义应用的路由。
- **编写建议**：
  - 使用清晰的路由命名。
- **代码规范**：
  ```python
  from django.urls import path
  from .views import AudioProcessingView

  urlpatterns = [
      path('process-audio/', AudioProcessingView.as_view(), name='process-audio'),
  ]
  ```

#### **`serializers.py`**
- **功能**：定义数据的序列化和反序列化逻辑。
- **编写建议**：
  - 使用 DRF 的 `Serializer` 或 `ModelSerializer`。
- **代码规范**：
  ```python
  from rest_framework import serializers
  from .models import TouristSpot

  class TouristSpotSerializer(serializers.ModelSerializer):
      class Meta:
          model = TouristSpot
          fields = '__all__'
  ```

#### **`services/`**
- **功能**：封装业务逻辑（如语音转文本、大模型问答、文本转语音）。
- **编写建议**：
  - 每个服务逻辑独立为一个文件，便于维护和扩展。

##### **`speech_to_text.py`**
- **功能**：实现语音转文本逻辑。
- **代码规范**：
  ```python
  def speech_to_text(audio_path):
      # 调用语音识别服务
      return "转好的文本"
  ```

##### **`text_to_speech.py`**
- **功能**：实现文本转语音逻辑。
- **代码规范**：
  ```python
  def text_to_speech(text):
      # 调用 TTS 服务
      return "audio_response.wav"
  ```

##### **`large_model.py`**
- **功能**：实现大模型问答逻辑。
- **代码规范**：
  ```python
  def ask_large_model(text):
      # 调用大模型 API
      return "大模型的回答"
  ```

---

### **4. `media/`**
- **功能**：存储上传的音频文件。
- **建议**：配置 `settings.py` 中的 `MEDIA_URL` 和 `MEDIA_ROOT`。

---

### **5. `static/`**
- **功能**：存储静态文件（如 CSS、JS）。
- **建议**：运行 `python manage.py collectstatic` 收集静态文件。

---

### **6. `templates/`**
- **功能**：存储 HTML 模板文件。
- **建议**：用于扩展 Django 管理后台或其他前端页面。

---

## **代码规范总结**
1. **命名规范**：
   - 变量、函数：使用小写字母和下划线（如 `audio_file`）。
   - 类名：使用大驼峰命名法（如 `AudioProcessingView`）。

2. **注释规范**：
   - 使用清晰的注释解释复杂逻辑。
   - 函数和类添加 docstring。

3. **代码格式**：
   - 遵循 PEP 8 规范。
   - 使用工具（如 `black` 或 `flake8`）自动格式化代码。

4. **模块化设计**：
   - 将业务逻辑封装到 `services/` 中，保持视图文件简洁。

---

## 环境配置

### **依赖安装**
1. 创建虚拟环境（推荐使用 Conda 或 venv）：
   ```bash
   conda create --name cuddlypawpal python=3.11
   conda activate cuddlypawpal
   ```
2. 安装依赖：
   ```bash
   pip install django djangorestframework requests
   ```

---

### **运行项目**
1. 迁移数据库：
   ```bash
   python manage.py migrate
   ```
2. 启动开发服务器：
   ```bash
   python manage.py runserver
   ```

---

## API 路由

| 路由                | 方法 | 描述                     |
|---------------------|------|--------------------------|
| `/api/process-audio/` | POST | 上传音频并返回语音回答   |
