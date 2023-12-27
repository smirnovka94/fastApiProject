from dotenv import load_dotenv
import os

# BASE_DIR = Path(__file__).resolve().parent.parent
# env_path = BASE_DIR / '.env'
load_dotenv()
# DB_USER = os.getenv('DB_USER')
# DB_PASS = os.getenv('DB_PASS')
# DB_HOST = os.getenv('DB_HOST')
DB_POSTGRES = os.getenv('DB_POSTGRES')
