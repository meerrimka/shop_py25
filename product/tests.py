from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from product.models import Category, Product
from rest_framework_simplejwt.views import TokenObtainPairView
from product.views import CategoryAPIView, ProductModelViewSet
from django.contrib.auth import get_user_model

User = get_user_model()

class CategoryTest(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.setup_category()
        self.setup_user()
        self.access_token = self.setup_user_token()

    def setup_user_token(self):
        data = {'email':"test@test.com", 'password': '12345'}
        request = self.factory.post('api/v1/account/login/', data)
        view = TokenObtainPairView.as_view()
        response = view(request)

        return response.data['access']


    @staticmethod
    def setup_category():
        category = [
            Category(title='c1'),
            Category(title='c2'),
            Category(title='c3'),
        ]
        Category.objects.bulk_create(category)
         

    def test_get_category(self):
        request = self.factory.get('api/v1/product/category/')
        view = CategoryAPIView.as_view({'get':'list'})
        response = view(request)
        assert response.status_code == 200
        assert len(response.data) == 3
        assert response.data[0]['title'] =='c1'

    def setup_user(self):
        self.user = User.objects.create_user(
            email = "test@test.com",
            password = '12345', 
            is_active = True
        )

    def test_post_category(self):
        data = {'title': 'c4'}
        request = self.factory.post('api/v1/product/category/',
        data)
        force_authenticate(request, self.user)
        view = CategoryAPIView.as_view({'post': 'create'})
        response = view(request)

        assert response.status_code == 201
        assert Category.objects.filter(title='c4').exists()

    def test_post_product(self):
        image = open('/home/meerim/Desktop/py25/django/shop/media/products/test.png', 'rb')
        data = {
            # 'owner': self.user.id,
            'category': Category.objects.first(),
            'title': 'test_product',
            'price': 20,
            'aomunt': 10,
            'image': image
        }


        request = self.factory.post('api/v1/product/modelviewset_crud/', data, HTTP_AUTHORIZATION='Bearer '+ self.access_token)

        force_authenticate(request, self.user)
        view = ProductModelViewSet.as_view({'post':'create'})
        response = view(request)

        assert response.status_code == 201
        assert Product.objects.filter(title='test_product').exists()