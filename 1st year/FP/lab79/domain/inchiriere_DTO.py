"""
@@@ Vintila Radu @@@
"""


class inchiriere_dto:
    def __init__(self, cid, fid, incid):
        """
        Initializare client-inchiriere DTO
        :param cid: string (client ID)
        :param fid: string (film ID)
        :param incid: string (inchiriere ID)
        """
        self.__cid = cid
        self.__fid = fid
        self.__incid = incid
        self.__status = "Inchiriat"

    def get_cid(self):
        return self.__cid

    def get_fid(self):
        return self.__fid

    def get_incid(self):
        return self.__incid

    def get_status(self):
        return self.__status

    def set_status(self):
        self.__status = "Returnat"
