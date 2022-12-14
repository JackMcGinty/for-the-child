

# we need this for firebase
import firebase_admin
from firebase_admin import credentials
import os
from firebase_admin import firestore

""" Class holding the functions we need to talk to the database """
class DatabaseConnection:
    def __init__(self):
        self.db = self.connect_firestore()

    def connect_firestore(self):
        """ Returns a connection to the database """
        """ Puts the high score into the database """
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "memorize-your-colors-highscore-firebase-adminsdk-qzc53-9608cf9bbe.json"
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {
                'projectId': 'memorize-your-colors-highscore',
            })
        db = firestore.client()
        return db
    
    def push_highscore(self, score: int):
        """ put the score into the database """
        data = {"score": score}
        self.db.collection("high-score").document("5Iga6ibZEzRhZ2LUXVk8").set(data)

    def pull_highscore(self) -> int:
        """ get the high score from the database """
        result = self.db.collection("high-score").document("5Iga6ibZEzRhZ2LUXVk8").get()
        if result.exists:
            return result.to_dict()["score"]
        else:
            return 0
