class Config:

    def __init__(self, *args, **kwargs):
        self.disp_min = 0
        self.disp_max = 15
        self.disp_scale = 16
        self.ignore_border = 18
        self.d_range = range(self.disp_min, self.disp_max+1)

        