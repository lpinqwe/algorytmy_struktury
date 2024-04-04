
class merge_sort_arrayyayay:
    buf = [0]
    dict_z_rozkazami = {}
    min_n = 0
    najwieksza_l_rozk=0
    def liczenie_rozkazow(self):

        for i in self.buf:
            if i in self.dict_z_rozkazami:
                self.dict_z_rozkazami[i] = self.dict_z_rozkazami[i] + 1
            else:
                self.dict_z_rozkazami[i] = 1

    def liczenie_cykli(self):
        min=0
        max_rozk=0
        for i in self.dict_z_rozkazami.values():
            min+=i
            if(i>max_rozk):
                max_rozk=i
        print(max_rozk+(max_rozk-1)*int(self.min_n))

    def place_data_to_buf(self, data):
        self.min_n = data[0]
        self.buf = data[1:]

    def read_std_in(self):
        buf = input().strip()
        buf = buf.split(" ")

        self.place_data_to_buf(buf)
        return self.buf


sorterere = merge_sort_arrayyayay()
sorterere.read_std_in()
#sorterere.place_data_to_buf([1, "C", "C", "A"])
sorterere.liczenie_rozkazow()
sorterere.liczenie_cykli()
# sorterere.place_data_to_buf()
