from PIL import Image
import numpy as np
import cv2
import os

class DummyDataGenerator:
    def __init__(self, set_mb: int):
        self.set_mb = set_mb

    def generate_text_file(self, file_name):
        """지정한 크기의 텍스트 파일을 생성"""
        size_in_bytes = self.set_mb * 1024 * 1024
        with open(file_name, 'w') as f:
            f.write('0' * size_in_bytes)
        print(f"텍스트 파일 {file_name} ({self.set_mb}MB) 생성 완료")

    def generate_image_file(self, file_name, width, height):
        """지정한 크기의 이미지 파일을 빠르게 생성"""
        target_size_in_bytes = self.set_mb * 1024 * 1024
        
        img_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
        img = Image.fromarray(img_data, 'RGB')

        img.save(file_name, quality=100)

        current_size = os.path.getsize(file_name)
        if current_size < target_size_in_bytes:
            with open(file_name, 'ab') as f:
                f.write(b'\0' * (target_size_in_bytes - current_size))

        print(f"이미지 파일 {file_name} ({self.set_mb}MB) 생성 완료 (실제 크기: {os.path.getsize(file_name) / (1024 * 1024):.2f}MB)")

    def generate_video_file(self, file_name, width, height, duration_in_seconds):
        """지정한 크기의 동영상 파일을 빠르게 생성"""
        target_size_in_bytes = self.set_mb * 1024 * 1024

        frame_count = int(duration_in_seconds * 30)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        video = cv2.VideoWriter(file_name, fourcc, 30, (width, height))

        for _ in range(frame_count):
            img_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
            video.write(img_data)

        video.release()

        current_size = os.path.getsize(file_name)
        if current_size < target_size_in_bytes:
            with open(file_name, 'ab') as f:
                f.write(b'\0' * (target_size_in_bytes - current_size))

        print(f"동영상 파일 {file_name} ({self.set_mb}MB) 생성 완료 (실제 크기: {os.path.getsize(file_name) / (1024 * 1024):.2f}MB)")
