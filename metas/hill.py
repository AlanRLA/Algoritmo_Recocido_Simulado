import numpy as np
from matplotlib import pyplot

class Hillclimbing:
    
    def __init__(self, objetivo, limites, step_size, n_iter):
         
        """
        """   
        self.objetivo = objetivo
        self.limites = limites
        self.step_size = step_size
        self.n_iter = n_iter

    def solve(self):
        
        soluciones=[]
        solucion = np.random.uniform(low=self.limites[0], high=self.limites[1])
        eval = self.objetivo(solucion)
        print("Solucion inicial = ", solucion,eval)
        soluciones.append(solucion)

        for i in range(self.n_iter):
            vecino = np.random.uniform(low=self.limites[0], high=self.limites[1])
            eval_v = self.objetivo(vecino)
            if eval_v <= eval:
                solucion, eval = vecino, eval_v
                soluciones.append(solucion)
                print(str(i)+".-x="+str(solucion)+" f(x)= "+str(eval))
        return (solucion,eval,soluciones)
        
    def show(self):
    
        """ 
        """
        best, best_eval, solucines = self.solve()
        print("!Done")
        print("BEST = " ,best,best_eval)
        x_inputs = np.arange(self.limites[0],self.limites[1],0.1)
        y_inputs = [self.objetivo(x) for x in x_inputs]
        pyplot.plot(x_inputs,y_inputs,'--')
        pyplot.plot(solucines,[self.objetivo(x) for x in solucines], 'o', color="black")
        pyplot.show()
        
    def solve_sa(self):
        solutions = []
        solution = np.random.uniform(low=self.limites[0], high=self.limites[1])
        print(solution)
        solution_eval = self.objetivo(solution)
        solutions.append(solution)
        temperatura = solution_eval * 0.4
       
        while temperatura >= 0.1:
            for _ in range(self.n_iter):
                candidato =  np.random.uniform(low=self.limites[0], high=self.limites[1])
                candidato_eval = self.objetivo(candidato)
                delta =  candidato_eval - solution_eval
                
                if np.random.uniform(low=0.0, high=1.0, size=None) <= np.power(np.e,(-delta/temperatura)) or delta < 0:
                    solution, solution_eval = candidato, candidato_eval
                    solutions.append(solution)
    
            temperatura = temperatura * np.random.uniform(low=0.8, high=0.99, size=None)
        return [solution, solution_eval, solutions]

    def show_sa(self):
    
        """ 
        """
        best, solution_eval, solutions = self.solve_sa()
        print("!Done")
        print("BEST = " ,best,solution_eval)
        x_inputs = np.arange(self.limites[0],self.limites[1],0.1)
        y_inputs = [self.objetivo(x) for x in x_inputs]
        pyplot.plot(x_inputs,y_inputs,'--')
        pyplot.plot(solutions,[self.objetivo(x) for x in solutions], 'o', color="black")
        pyplot.show()
