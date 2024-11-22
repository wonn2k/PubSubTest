import firebase_admin
import os
from firebase_admin import credentials
from firebase_admin import db

import setenv


class FBupdater:
    def __init__(self):
        self.cred = credentials.Certificate(os.getenv('FIREBASE_CREDENTIALS'))
        firebase_admin.initialize_app(self.cred, {
            'databaseURL': os.getenv('FIREBASE_DBM_URL')
        })

    def update_from_IoT(self, building_id_value, id_value, ewt_num, ewt_cur, dt=None):
        reststr = "buildings/"
        reststr = reststr + str(building_id_value) + "/restaurant_list/" + str(id_value) + "/"
        print(reststr)
        ref = db.reference(reststr)
        ref.update(
            {
                "ewt_num": ewt_num,
                "ewt_cur": ewt_cur,
            }
        )

    def update_from_local(self, building_id_value, id_value, ewt_avg):
        reststr = "buildings/"
        reststr = reststr + str(building_id_value) + "/restaurant_list/" + str(id_value) + "/"
        ref = db.reference(reststr)
        ref.update(
            {
                "ewt_avg": ewt_avg
            }

        )



if __name__ == '__main__':
    setenv.setEnv()
    updater = FBupdater()
    updater.update_from_IoT(0, 0, 20, 20)
    updater.update_from_local(0, 0, 18)