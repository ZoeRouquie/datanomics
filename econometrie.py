from random import uniform
import matplotlib.pyplot as plt

v = 100
t = 10
c = 10
m = 1
n = 2
benchmark = c + t 


def tarification(p_concu):
    return (p_concu+t+c)/2


    
def __main__():
    p_a =  uniform(c,v)
    p_b = uniform(c,v)
    prix_a = [p_a]
    prix_b = [p_b]
    for _ in range(20):
        p_a = tarification(p_b)
        p_b = tarification(p_a)
        prix_a.append(p_a)
        prix_b.append(p_b)
    plt.plot(prix_a, label='Prix A', marker='o')
    plt.plot(prix_b, label='Prix B', marker='x')
    plt.axhline(y=20, color='red', linestyle='--', label='Benchmark')
    plt.title("Évolution des prix")
    plt.xlabel("Itération")
    plt.ylabel("Prix")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    __main__()
        

        
        
    
    