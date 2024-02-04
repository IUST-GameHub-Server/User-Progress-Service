from ..DataLayer.DataAccess import DataAccess
from types import SimpleNamespace
import json

class UserProgressLogic:
    def setup_player(user_info):
        user= json.loads(user_info, object_hook=lambda d: SimpleNamespace(**d))
        return json.dumps({'result' : DataAccess.setup_player(user.email)})
    
    def update_player_progress(user_info):
        user= json.loads(user_info, object_hook=lambda d: SimpleNamespace(**d))
        DataAccess.set_player_level(user.email, user.level)
        DataAccess.set_point(user.email, user.point)
        DataAccess.set_user_rating(user.email, user.rating)

        result={
            'level':DataAccess.get_player_level(user.email)[0],
            'point':DataAccess.get_point(user.email)[0],
            'rating':DataAccess.get_user_rating(user.email)[0]
        }
        return json.dumps(result)
    
    def get_player_progress(user_info):
        user= json.loads(user_info, object_hook=lambda d: SimpleNamespace(**d))
        result={
            'level':DataAccess.get_player_level(user.email)[0],
            'point':DataAccess.get_point(user.email)[0],
            'rating':DataAccess.get_user_rating(user.email)[0]
        }
        return json.dumps(result)

