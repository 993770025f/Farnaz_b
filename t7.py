
def A(a,b):
    def b_m_m(a,b):
        while b!=0:
            a,b = b , a%b
        return a
    def k_m_m(a,b):
        return (a*b // b_m_m(a,b))
    print('B_m_m:',b_m_m(a,b))
    print("K_m_m:",k_m_m(6,15))
A(6,15)
