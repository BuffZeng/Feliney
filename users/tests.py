
from django.test import TestCase
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.models import User
from datetime import datetime
from users.models import UserProfile
from users.models import CatPhotos
from cats.models import CatProfile


class Coms(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.login_url = reverse('users:login')
        self.catadd_url= reverse('users:add_cat')
        self.all_coments_url = reverse('users:all_coments')
        self.logout_url=reverse('users:user_logout')
        self.landing_url=reverse('users:home_page')
        self.register_url = reverse('users:register')
        self.newmail_url= reverse('users:draftnew')
        self.test_user = User.objects.create(username='John_White')
        self.test_user.set_password('Pass@123')
        self.test_user.save() 
        cat1=CatProfile.objects.create(breed='Persian cat', price_range=400-800,description='The Persian Cat is a long-haired breed originating in Iran. The Persian was bred in Iran, where the feline community has achieved the highest international recognition for the Persian breed. Today, the Persian Cat has come to be very popular in Iran. During the 1970s, the population of the Persian was considered to be small and the Persian was used in commercial animal rearing for its fur.')
        cat1.save()
        catphoto1=CatPhotos.objects.create(uid=1,uploaddate=datetime.now(),description="All of you")
        catphoto1.save()
        self.userprof=UserProfile.objects.create(user=self.test_user,user_type='Cat Owner',name='Rohan T',member_since=datetime.now(),email_id='rohant@gmail.com',picture=None,breeds='Sphynx',about_me='Im Spent')
        self.userprof.save()
        self.user={'username':'John_White','password':'Pass@123'}
        return super().setUp()


class Accesscheck(Coms):
    def test_viewlogin(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'users/login.html')
    def test_loginactual(self):
        response = self.client.post(self.login_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)
    def test_withoutuser(self):
        response = self.client.post(self.login_url,{'password':'Passo'},format='text/html')
        self.assertEqual(response.status_code,200)

class Punchout(Coms):
    def test_canlogout(self):
        response = self.client.post(self.logout_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)

class Registerrela(Coms):
    def test_viewreg(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'users/register.html')

class Landingchec(Coms):
    def test_landingcheck(self):
        response = self.client.get(self.landing_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'users/index.html')

class CatAddchec(Coms):
    def test_CatAddchec(self):
        response = self.client.get(self.catadd_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'users/add_cat.html')

class Newmailchec(Coms):
    def test_Usercreation(self):
        testuser=UserProfile.objects.get(uid=1)
        namo=testuser.name
        self.assertEqual(namo,'Rohan T')

class Photosmodelchec(Coms):
    def testnewphoto(self):
        testphoto=CatPhotos.objects.get(pid=1)
        users_id=UserProfile.objects.get(pk=1)
        self.assertEqual(testphoto.uid,users_id.uid)

class NewMailCheck(Coms):
    def test_Newmailchec(self):
        login = self.client.login(username='John_White', password='Pass@123')
        response = self.client.get(self.newmail_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'users/draft_new.html')


class AllComentchec(Coms):
    def test_Allcommento(self):
        login = self.client.login(username='John_White', password='Pass@123')
        response = self.client.get(self.all_coments_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'users/all_comments.html')






