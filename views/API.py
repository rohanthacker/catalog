from views.category import CategoryListView
from flask.json import jsonify
from models.session import session
from models.main import Category, Item


class APIView(CategoryListView):
    def dispatch_request(self):
        payload = [obj.serialize() for obj in self.get_objects()]
        return jsonify(payload)
