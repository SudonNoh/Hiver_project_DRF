from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from authentication.models import User
from brand.models import Brand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('Start Brand and User setting')
        # 3
        Brand.objects.create(
            brand="Nike", 
            brand_address="서울 강남구 테헤란로 152 강남파이낸스센터 30층",
            brand_type="Brand",
            brand_phone_number="080-022-0182",
            brand_email="service@nike.co.kr",
            brand_homepage="https://www.nike.com/kr/ko_kr/",
            brand_description="나이키의 모든 것, 나이키 공식 온라인스토어",
            )
        
        # 4
        Brand.objects.create(
            brand="Adidas", 
            brand_address="서울특별시 서초구 서초대로 74길 4, 삼성생명 서초타워 23층 (06620)",
            brand_type="Brand",
            brand_phone_number="1588-8241",
            brand_email="adiclub_korea@adidas.com",
            brand_homepage="https://shop.adidas.co.kr/",
            brand_description="아디다스 인기상품. 한정상품, 신상품 정보. 멤버십혜택",
            )
        
        # 5
        Brand.objects.create(
            brand="맨인스토어", 
            brand_address="02262 서울특별시 중랑구 신내역로 111",
            brand_type="Shopping_mall",
            brand_phone_number="02-6205-1035",
            brand_email="manin-store@naver.com",
            brand_homepage="https://maninstore.co.kr/",
            brand_description=
            """
            좋은 품질의 원단 사용과 최고의 가성비 SNS 인기 남성의류 쇼핑몰!! 
            믿고 살수 있는 자체제작&셀렉 쇼핑몰 맨인스토어
            """,
            )
        
        # 6
        Brand.objects.create(
            brand="모노포스", 
            brand_address="47213 부산광역시 부산진구 중앙대로 913 (양정동) 5층",
            brand_type="Shopping_mall",
            brand_phone_number="070-7362-1658",
            brand_email="monoforce@naver.com",
            brand_homepage="https://www.monoforce.co.kr/",
            brand_description=
            """
            20대 남성의류 쇼핑몰, 유니크, 하이퀄리티, 직수입 남성의류 편집쇼핑몰, 
            무료배송, 당일발송, 남자반바지, 남자슬랙스, 맨투맨, 니트, 후드, 점퍼,
            패딩, 가디건, 면바지, 셔츠, 신발, 모자, 벨트
            """,
            )

        pw = 'test1234'
        usernames = [
            "admin1", 
            "admin2", 
            "nike_master", 
            "nike_vendor", 
            "adidas_master", 
            "adidas_vendor",
            "mainstore_master",
            "mainstore_vendor",
            "monoforce_master",
            "monoforce_vendor",
            "customer1",
            "customer2",
            "customer3",
            "customer4",
            "customer5",
            "customer6",
            "customer7",
            "customer8",
            "customer9",
            "customer10",
            ]
            
        # site 관리자 1
        User.objects.create_user(
            username="admin1",
            email="admin1@test.com",
            password='test1234',
            phone_number="001-0000-0000",
            brand=Brand.objects.get(id=1),
            is_staff=True
        )
        
        # site 관리자 2
        User.objects.create_user(
            username="admin2",
            email="admin2@test.com",
            password='test1234',
            phone_number="002-0000-0000",
            brand=Brand.objects.get(id=1),
            is_staff=True
        )
        
        # nike 마스터 운영자
        User.objects.create_user(
            username="nike_master",
            email="nike_master@test.com",
            password=pw,
            phone_number="000-0001-0001",
            brand=Brand.objects.get(id=3),
        )
        
        # nike 일반 운영자
        User.objects.create_user(
            username="nike_vendor",
            email="nike_vendor@test.com",
            password=pw,
            phone_number="000-0001-0002",
            brand=Brand.objects.get(id=3),
        )
        
        # adidas 마스터 운영자
        User.objects.create_user(
            username="adidas_master",
            email="adidas_master@test.com",
            password=pw,
            phone_number="000-0002-0001",
            brand=Brand.objects.get(id=4),
        )
        
        # adidas 일반 운영자
        User.objects.create_user(
            username="adidas_vendor",
            email="adidas_vendor@test.com",
            password=pw,
            phone_number="000-0002-0002",
            brand=Brand.objects.get(id=4),
        )
        
        # mainstore 마스터 운영자
        User.objects.create_user(
            username="mainstore_master",
            email="mainstore_master@test.com",
            password=pw,
            phone_number="000-0003-0001",
            brand=Brand.objects.get(id=5),
        )
        
        # mainstore 일반 운영자
        User.objects.create_user(
            username="mainstore_vendor",
            email="mainstore_vendor@test.com",
            password=pw,
            phone_number="000-0003-0002",
            brand=Brand.objects.get(id=5),
        )
        
        # monoforce 마스터 운영자
        User.objects.create_user(
            username="monoforce_master",
            email="monoforce_master@test.com",
            password=pw,
            phone_number="000-0004-0001",
            brand=Brand.objects.get(id=6),
        )
        
        # monoforce 일반 운영자
        User.objects.create_user(
            username="monoforce_vendor",
            email="monoforce_vendor@test.com",
            password=pw,
            phone_number="000-0004-0002",
            brand=Brand.objects.get(id=6),
        )
        
        # customer 1 - 10
        for i in range(10):
            num = str(i+1)
            User.objects.create_user(
                username="customer"+ num,
                email="customer"+ num +"@test.com",
                password=pw,
                phone_number="010-0000-000"+num,
            )
            
        
        for name in usernames:
            user = User.objects.get(username = name)
            if user.brand.brand == 'Admin':
                group = Group.objects.get(name="site_admin")
                
            elif user.brand.brand == "customer":
                if int(name[-1]) < 6:
                    group = Group.objects.get(name="membership_customer")
                else:
                    group = Group.objects.get(name="general_customer")
            
            elif name[-6:] == 'master':
                group = Group.objects.get(name="master_vendor")
                
            elif name[-6:] == "vendor":
                group = Group.objects.get(name="general_vendor")
                
            user.groups.add(group)
            print('user.name : ', user.username,'\nuser.group : ', user.groups.values(), '\nuser.brand : ', user.brand.brand)
            user.save()
            
        print('finished setting')