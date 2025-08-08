import sys,os
from dotenv import load_dotenv

load_dotenv()
PORT = int(os.getenv('PORT', '5000'))

# run without the lib
HOME  = os.getcwd().replace('/notebooks', '/src')
new_path = f"{HOME}" 
if new_path not in sys.path:
    sys.path.append(new_path)

# change dir
os.chdir(HOME)