import base64
import hashlib
import hmac
import logging
import os
import time
from typing import Optional

from configs import zerix_config
from extensions.ext_storage import storage

IMAGE_EXTENSIONS = ["jpg", "jpeg", "png", "webp", "gif", "svg"]
IMAGE_EXTENSIONS.extend([ext.upper() for ext in IMAGE_EXTENSIONS])


class UploadFileParser:
    @classmethod
    def get_image_data(cls, upload_file, force_url: bool = False) -> Optional[str]:
        if not upload_file:
            return None

        if upload_file.extension not in IMAGE_EXTENSIONS:
            return None

        if zerix_config.MULTIMODAL_SEND_IMAGE_FORMAT == "url" or force_url:
            return cls.get_signed_temp_image_url(upload_file.id)
        else:
            # get image file base64
            try:
                data = storage.load(upload_file.key)
            except FileNotFoundError:
                logging.error(f"File not found: {upload_file.key}")
                return None

            encoded_string = base64.b64encode(data).decode("utf-8")
            return f"data:{upload_file.mime_type};base64,{encoded_string}"

    @classmethod
    def get_signed_temp_image_url(cls, upload_file_id) -> str:
        """
        get signed url from upload file

        :param upload_file: UploadFile object
        :return:
        """
        base_url = zerix_config.FILES_URL
        image_preview_url = f"{base_url}/files/{upload_file_id}/image-preview"
        return image_preview_url

    @classmethod
    def verify_image_file_signature(cls, upload_file_id: str, timestamp: str, nonce: str, sign: str) -> bool:
        """
        verify signature

        :param upload_file_id: file id
        :param timestamp: timestamp
        :param nonce: nonce
        :param sign: signature
        :return:
        """
        data_to_sign = f"image-preview|{upload_file_id}|{timestamp}|{nonce}"
        secret_key = zerix_config.SECRET_KEY.encode()
        recalculated_sign = hmac.new(secret_key, data_to_sign.encode(), hashlib.sha256).digest()
        recalculated_encoded_sign = base64.urlsafe_b64encode(recalculated_sign).decode()

        # verify signature
        if sign != recalculated_encoded_sign:
            return False

        current_time = int(time.time())
        return current_time - int(timestamp) <= zerix_config.FILES_ACCESS_TIMEOUT
