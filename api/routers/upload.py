from fastapi import APIRouter, File, UploadFile
import boto3
from botocore.exceptions import NoCredentialsError
import faker
import datetime
import os

# Constants from environment variables
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
BUCKET_NAME = os.environ.get("BUCKET_NAME")
REGION_NAME = os.environ.get("REGION_NAME")

FILE_PATH = "fotos/"

# S3 connect
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION_NAME,
)

upload_router = APIRouter()


def genera_aleatorio():
    fake = faker.Faker()

    numbers = fake.unique.random_int()
    return numbers


# @upload_router.post("/file")
# def upload_file(file: bytes = File()):
#     return {"file_size": len(file)}

# @upload_router.post("/file")
# def upload_uploadfile1(file: UploadFile):
#     return {
#         "filename": file.filename,
#         "content_type": file.content_type,
#         }

# @upload_router.post("/file")
# def upload_uploadfile(file: UploadFile):
#     with open("image/image.png", "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     return {
#         "filename": file.filename,
#         }


@upload_router.post("/file")
async def upload_uploadfile(file: UploadFile = File(...)):
    # with open(file_name, "wb") as buffer:
    #     shutil.copyfileobj(file.file, buffer)
    try:
        if file.content_type.startswith("image"):
            file_name = (
                FILE_PATH
                + str(genera_aleatorio())
                + str(datetime.datetime.now())
                .replace(" ", "")
                .replace(":", "")
                .replace(".", "")
                + "-"  + str(file.filename)
            )
            print("*" * 20)
            print(f"filename:  {file_name}")
            print("+" * 20)
            print(f"file.filename: {file.filename}")
            s3.upload_fileobj(
                file.file, BUCKET_NAME, file_name, ExtraArgs={"ACL": "public-read"}
            )
            url_image = f"https://{BUCKET_NAME}.s3.{REGION_NAME}.amazonaws.com/{file_name}"

            return {"message": "Archivo subido exitosamente", "filename": url_image}
        else:
            return {"message": "El archivo no es una imagen válida"}
    except NoCredentialsError:
        return {"message": "Credenciales de AWS no válidas"}
    except Exception as e:
        return {"message": str(e)}
