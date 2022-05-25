class Builder(object):
    def __inti__(self, type):
        self.query = ''
        self.fileds = []
        self.tags = []
        


    def select(self
        , qselect
        , qfrom
        , qwhere
        , qgroup
        , qhaving
        ):
        self.tags.append('SELECT')