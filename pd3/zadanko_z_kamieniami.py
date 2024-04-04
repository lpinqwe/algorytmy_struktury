class niszczyciel_materjalu_budowlanego:
    buf = []
    p_def = 0
    r_def = 0
    final_wigth=0
    def place_data_to_buf(self, data):
        self.buf = data
        self.r_def = len(data) - 1
        self.p_def = 0
        self.new_buf=[]
    def merge_sort(self, A: buf, p: p_def, r: r_def):
        if p < r:
            q = (p + r) // 2
            self.merge_sort(A, p, q)
            self.merge_sort(A, q + 1, r)
            if (len(A[p:q + 1]) == 1 and len(A[q + 1:r + 1]) == 1):
                #print(f"przed{A[p:q + 1], A[q + 1:r + 1]}")
                if (A[p:q + 1][0] > A[q + 1:r + 1][0]):
                    #print(f"przed {A[p:q + 1][0]}")
                    buf = A[p:q + 1][0] - A[q + 1:r + 1][0]
                    A[p:q + 1] = [buf]
                    #self.new_buf.append(buf)
                    #print(A[p:q + 1][0])
                    A[q + 1:r + 1]=[0]
                    #print(f"gra {A[p:q + 1][0]}")
                else:
                    #print("else")
                    #print(f"przed {A[p:q + 1][0]}")
                    buf = A[q + 1:r + 1][0] - A[p:q + 1][0]
                    A[q + 1:r + 1] = [buf]
                    #self.new_buf.append(buf)

                    #print(A[p:q + 1][0])
                    A[p:q + 1]=[0]
                    #print(f"gra {A[p:q + 1][0]}")
                #print(f"po________{A[p:q + 1], A[q + 1:r + 1]}")
            #print(f"array2_ = {self.new_buf.sort()}, len2= {len(self.new_buf)}")

            self.merge(A, p, q, r)
    def sorter(self):
        while len(self.buf)!=1:
            self.buf.sort()
            self.merge_sort(self.buf, self.p_def, self.r_def)
            self.buf.reverse()
            self.buf=self.buf[:self.buf.index(0)]
            #print(f"array__ = {self.buf}, len== {len(self.buf)}")
            self.place_data_to_buf(self.buf)
        self.final_wigth=self.buf[0]
        return self.buf[0]



    def merge(self, A, p, q, r):
        n1 = q - p + 1
        n2 = r - q
        L = [0] * (n1 + 1)
        R = [0] * (n2 + 1)

        for i in range(n1):
            L[i] = A[p + i]
        for j in range(n2):
            R[j] = A[q + j + 1]

        L[n1] = float('inf')
        R[n2] = float('inf')

        i = 0
        j = 0
        #print(f"merge {L,R}")
        for k in range(p, r + 1):
            if L[i] <= R[j]:

                #print(f"<=   L=={L[i]}, R=={R[j]}")
                """    
                if(R[j]!=float('inf')):
                    buf=R[j]-L[i]
                    L[i]=0
                    R[j]=buf
                """
                A[k] = L[i]
                i += 1
            else:
                #print(f">=    L=={L[i]}, R=={R[j]}")
                """
                if(L[j]!=float('inf')):
                    buf =  L[i]-R[j]
                    L[i] = buf
                    R[j] = 0
                """
                A[k] = R[j]
                j += 1


    def read_std_in(self):
        buf = input().strip()
        buf = buf.split(" ")

        buf = [int(elem) for elem in buf]
        self.place_data_to_buf(buf)
        return self.buf

    def hunger_game(self):
        None


sorterere = niszczyciel_materjalu_budowlanego()
sorterere.read_std_in()
#[ 145,209 ,263 ,158, 7 ,185, 111, 104 ,171, 281, 152, 158, 234 ,119, 283]
#sorterere.place_data_to_buf([192, 40, 289, 208, 91, 176, 249, 118, 259, 220, 118, 177, 169])
#sorterere.place_data_to_buf()
sorterere.sorter()
print(sorterere.final_wigth)
