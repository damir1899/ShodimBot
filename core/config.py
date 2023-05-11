from os import getenv
from dotenv import load_dotenv
load_dotenv()

TOKEN = getenv("TOKEN")
ADMIN = getenv("ADMIN_USER")

PGHOST = getenv("PGHOST")
PGDATABASE = getenv("PGDATABASE")
PGUSER = getenv("PGUSER")
PGPASSWORD = getenv("PGPASSWORD")
PGPORT = getenv("PGPORT")

PARS_URL = getenv('URL')
PARS_DOMAIN = getenv('DOMAIN')
HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
}

IMAGE = [
    'source/image/img1.jpg',
    'source/image/img2.jpg',
    'source/image/img3.jpg',
    'source/image/img4.jpeg',
    'source/image/img5.jpg',
    'source/image/img6.jpg',
    'source/image/img7.jpg',
]