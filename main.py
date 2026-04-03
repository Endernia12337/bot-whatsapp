import schedule
import sender
import os
import dotenv

dotenv.load_dotenv(r"C:\Users\RT\Desktop\trabalhos\codigos em andamento\autoenvzap\.env.config")

while True:
    schedule.every().day.at(os.getenv("horario")).do(sender.send())