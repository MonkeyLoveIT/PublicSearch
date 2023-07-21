from django.urls import path, include
from api.views import BookListCreateView, BookDetailView, import_data
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API 文档",
        default_version='v1',
        description="API 接口文档",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)


urlpatterns = [
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # 其他 URL 配置
    path('api/', include([
        path('books/', BookListCreateView.as_view(), name='book-list-create'),
        path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
        path('import', import_data, name='import-data'),  # 添加导入数据的URL映射
    ])),
]
