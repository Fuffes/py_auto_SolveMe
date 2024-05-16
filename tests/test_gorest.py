import requests
from src.base_class.response import Response
from configuration import BASE_URL
from src.pydantic_schemas.user import User


def test_get_data(get_users):
    data = Response(get_users)
    data.assert_status_code(200).validate(User)


# {'meta':
#      {'pagination':
#           {'total': 2735,
#            'pages': 274,
#            'page': 1,
#            'limit': 10,
#            'links': {'previous': None, 'current': 'https://gorest.co.in/public/v1/users?page=1', 'next': 'https://gorest.co.in/public/v1/users?page=2'}}},
#  'data': [
#      {'id': 6888703, 'name': 'Charuchandra Ahuja', 'email': 'ahuja_charuchandra@ortiz.example', 'gender': 'female', 'status': 'active'},
#      {'id': 6888702, 'name': 'Akroor Guha LLD', 'email': 'lld_akroor_guha@dooley.example', 'gender': 'male', 'status': 'inactive'},
#      {'id': 6888701, 'name': 'The Hon. Eshita Desai', 'email': 'the_desai_hon_eshita@collier.test', 'gender': 'male', 'status': 'active'},
#      {'id': 6888700, 'name': 'Sloka Bandopadhyay', 'email': 'bandopadhyay_sloka@bogan-streich.example', 'gender': 'male', 'status': 'active'},
#      {'id': 6888698, 'name': 'Param Tandon', 'email': 'param_tandon@ward.test', 'gender': 'female', 'status': 'active'},
#      {'id': 6888697, 'name': 'Geeta Tagore MD', 'email': 'tagore_md_geeta@brekke.example', 'gender': 'male', 'status': 'active'},
#      {'id': 6888696, 'name': 'Amrita Mukhopadhyay', 'email': 'mukhopadhyay_amrita@lehner.test', 'gender': 'female', 'status': 'inactive'},
#      {'id': 6888695, 'name': 'Vidhur Patel', 'email': 'patel_vidhur@hettinger.test', 'gender': 'male', 'status': 'inactive'},
#      {'id': 6888694, 'name': 'Shwet Gupta', 'email': 'gupta_shwet@luettgen.example', 'gender': 'female', 'status': 'inactive'},
#      {'id': 6888693, 'name': 'Manikya Asan', 'email': 'manikya_asan@boehm.test', 'gender': 'male', 'status': 'inactive'}]}
