from django.core.management.base import BaseCommand
from product.models import Category, SubCategory


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Category_list = {
            "아웃터": [
                "재킷", 
                "점퍼",
                "블레이저",
                "베스트",
                "가디건",
                "수트",
                "코트",
                "롱패딩",
                "숏패딩",
                "패딩조끼",
                "기타"
            ],
            "상의": [
                "반팔티",
                "7부티",
                "긴팔티",
                "민소매",
                "맨투맨",
                "후드티",
                "집업",
                "니트",
                "기타"
            ],
            "셔츠": [
                "기본",
                "체크",
                "스트라이프",
                "데님",
                "헨리넥",
                "차이나",
                "반팔",
                "기타"
            ],
            "바지": [
                "슬렉스",
                "면바지",
                "청바지",
                "반바지",
                "트레이닝",
                "조거팬츠",
                "기타"
            ]
        }
        
        for category in Category_list:
            Category.objects.create(category=category)
            print("\n\n CATEGORY : ", category, "\n\n")
            
            for subcategory in Category_list[category]:
                print("SubCategory : ", subcategory)
                SubCategory.objects.create(
                    category=Category.objects.get(category=category), 
                    subcategory=subcategory
                )
            