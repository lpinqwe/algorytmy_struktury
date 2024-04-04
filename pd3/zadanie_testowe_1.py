#elegancko z kormena by walawaladar

class merge_sort_arrayyayay:
    buf=0
    p_def=0
    r_def=0
    def place_data_to_buf(self,data):
        self.buf=data
        self.r_def=len(data) - 1
        self.p_def=0
    def merge_sort(self,A:buf, p:p_def, r:r_def):
        if p < r:
            q = (p + r) // 2
            self.merge_sort(A, p, q)
            self.merge_sort(A, q + 1, r)

            print(f"{A[p:q+1], A[q+1:r+1]}")

            self.merge(A, p, q, r)


    def merge(self,A, p, q, r):
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
        for k in range(p, r + 1):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
    def sorter(self):
        self.merge_sort(self.buf,self.p_def,self.r_def)
    def read_std_in(self):
        buf = input().strip()
        buf=buf.split(" ")

        buf = [int(elem) for elem in buf]
        self.place_data_to_buf(buf)
        return self.buf

sorterere = merge_sort_arrayyayay()
sorterere.read_std_in()
#sorterere.place_data_to_buf([101, 6 ,28])
#sorterere.place_data_to_buf()
sorterere.sorter()
#print(sorterere.buf)