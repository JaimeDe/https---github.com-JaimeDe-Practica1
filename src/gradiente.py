import sys

class gradiente:

    def __init__(self,ax,ay,alfa,it,tol):
        self.archivox=ax
        self.archivoy=ay
        self.alfa=float(alfa)
        self.iteraciones=float(it)
        self.tolerancia=float(tol)
        self.matrizx = []
        self.matrizy = []
        self.thetas = []
        self.thetastemp = []
        self.m=0		
        self.n=0        
        
    def imprimir(self):
        print ('matriz x:')
        print (self.matrizx)
        print ('matriz y:')
        print (self.matrizy)
        print ('m:',self.m)        
        print ('tetha:')
        print (self.thetas)
        print ('n:',self.n)
		

    def cargararchivoy(self):
        archy=open(self.archivoy,'r')
        linea=archy.readline().rstrip('\n')
        while linea!="":
            self.m=self.m+1
            lineafloat=float(linea)
            self.matrizy.append(lineafloat)
            linea=archy.readline().rstrip('\n')            
        archy.close()
                   

    def cargararchivox(self):        
        archx=open(self.archivox,'r')
        linea=archx.readline().rstrip('\n')
        while linea!="":            
            vectorstring=linea.split(",")
            vectorfloat=[]
            for l in vectorstring:
                vectorfloat.append(float(l))
            self.matrizx.append(vectorfloat)
            linea=archx.readline().rstrip('\n')
        archx.close()
		
         
    def calcular_htheta(self,listavarx):
        htheta=0
        cont=0
        for theta in self.thetas:
            htheta=htheta+(theta*listavarx[cont])
            cont=cont+1
        return htheta
		
    def costo(self):
        sum=0
        i=1
        while i<=self.m:		
            sum=sum+pow((self.calcular_htheta(self.matrizx[(i-1)])-self.matrizy[(i-1)]),2)
            i=i+1
        sum=sum*(1/(2*self.m))
        return sum

    def sumatoria(self,j):
        sum=0
        i=1
        while i<=self.m:			
            sum=sum+(self.calcular_htheta(self.matrizx[(i-1)])-self.matrizy[(i-1)])*self.matrizx[i-1][j]
            i=i+1
        return sum
		
    def calcular_theta(self,alfa,j):
        theta_j=0
        costo=0
        costo=(alfa*(1/self.m)*self.sumatoria(j))
        theta_j=self.thetas[j]-costo
        self.costo()        
        return theta_j
		
  
    def set(self):
        self.n=len(self.matrizx[0])
        c=0
        while(c<self.n):
            self.thetas.append(0)
            self.thetastemp.append(0)
            c=c+1
            
    def nuevo_thetas(self):
        j=0
        while (j<=self.n-1):
            self.thetastemp[j]=self.thetas[j]-((self.alfa/self.m)*self.sumatoria(j))
            j=j+1
            
    def copiaraTheta(self):
        c=0
        for l in self.thetastemp:
            self.thetas[c]=l
            c=c+1 
    def imprimirsalida(self):
        salida=[]
        c=0
        for l in self.thetas:
            salida.append("t"+str(c)+"="+str(l))
            c=c+1
        print("respueta: ",salida)
    
    def ciclo(self):
        f=open('costo.txt','w')
        cont=0
        #inicializar thetas(se inicializan a 0)
        self.set()
        #costo inicial
        costo1=-1
        costo2=self.costo() 
        f.write(""+str(costo2)+"\n")		
        while (cont<self.iteraciones) and abs(costo1-costo2)>self.tolerancia:
            costo1=costo2
            #calcular nuevos valores para theta           
            self.nuevo_thetas()
            self.copiaraTheta()
            #costo            
            costo2=self.costo()                                    
            print("costo: ",costo2)
            f.write(""+str(costo2)+"\n")
            cont=cont+1
            print(cont)
        self.imprimirsalida()
        f.close()
      
     
			
    def calcular(self):
        self.cargararchivox()
        self.cargararchivoy()
        #self.set()
        #self.imprimir()
        self.ciclo()
        
        
	
if len(sys.argv)!=6:
    print ('Error numero de parametros incorrecto')
else:
    g=gradiente(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
    g.calcular()



  
