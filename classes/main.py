from classes.cp import ContaPoupanca
from classes.cc import ContaCorrente

cp = ContaPoupanca(1111,2222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(10)

print('########################')
print()

cc = ContaCorrente(1111, 3333, 0, 500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)