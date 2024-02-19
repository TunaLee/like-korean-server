import os
import csv
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from like_korean.apps.nationalities.models import Nationality

class Command(BaseCommand):
    help = 'Load nationality data from CSV file'

    # ALLOWED_IMAGE_EXTENSIONS = ['gif', 'jpg', 'jpeg', 'png', 'bmp']

    # def handle(self, *args, **kwargs):
    #     # CSV 파일의 경로
    #     filename = 'like_korean/data/nationalities.csv'
    #
    #     with open(filename, 'r', encoding='utf-8-sig') as file:
    #         reader = csv.DictReader(file)
    #         for row in reader:
    #             # 이미지 파일이 존재하는 경우에만 업로드
    #             image_path = f'data/{row["code"]}'
    #             image_file = None
    #             for extension in self.ALLOWED_IMAGE_EXTENSIONS:
    #                 if os.path.exists(f'{image_path}.{extension}'):
    #                     image_file = ImageFile(open(f'{image_path}.{extension}', 'rb'))
    #                     break
    #
    #             # 모델 필드에 직접 데이터 입력
    #             nationality, created = Nationality.objects.get_or_create(
    #                 code=row['code'],
    #                 name=row['name'],
    #                 eng_name=row['eng_name'],
    #             )
    #
    #             # 이미지 파일이 존재하는 경우에만 이미지 필드 업로드
    #             if image_file:
    #                 nationality.image = image_file
    #                 nationality.save()
    #
    #             if created:
    #                 self.stdout.write(self.style.SUCCESS(f'Created Nationality: {nationality}'))
    #             else:
    #                 self.stdout.write(self.style.WARNING(f'Nationality already exists: {nationality}'))

    def handle(self, *args, **kwargs):
        # CSV 파일의 경로
        filename = 'like_korean/data/nationalities.csv'

        with open(filename, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:

                # 모델 필드에 직접 데이터 입력
                nationality, created = Nationality.objects.get_or_create(
                    code=row['code'],
                    name=row['name'],
                    eng_name=row['eng_name'],
                    image_url=f'https://like-korean.s3.ap-northeast-2.amazonaws.com/media/Nationality/{row["code"]}'
                )


                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created Nationality: {nationality}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Nationality already exists: {nationality}'))
