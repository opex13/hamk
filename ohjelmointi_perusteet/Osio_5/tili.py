class tili:
    saldo = 0
    
    def __init__(self):
        self.saldo = 0
        
    def talleta(self, paljonko):
        self.saldo = self.saldo + paljonko
        print("tilille talletettu",paljonko,"saldo on", self.saldo)
    
    def nosta(self, paljonko):
        if(paljonko > self.saldo):
            print("ei ole katetta")
        else:
            self.saldo = self.saldo - paljonko  
            print("nostettu",paljonko,"jäljellä oleva saldo on",self.saldo)
        
    def tiliote(self):
        print(self.saldo)
        
    def korkoa(self, korkoTaso):
        self.saldo = self.saldo*(1+(korkoTaso/100))
        
        #kaava [P(1+i)n]-P (Jossa P=pääoma, i=nimellinen vuosittainen korko prosentteina ja n=korkojaksojen määrä)
    def korkoaKorolle(self, i, n):
        print("Korkoa korolle olisi",round((self.saldo*(1+i/100)**n)-self.saldo,2),"€")