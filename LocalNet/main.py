from data import Data
from server import Server
from router import Router


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Раз", sv_to.get_ip()))
sv_from2.send_data(Data("Два", sv_to.get_ip()))
sv_to.send_data(Data("Три", sv_from.get_ip()))
router.send_data()
print(sv_from.get_data())
print(sv_to.get_data())
