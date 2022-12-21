"""
    public
    protected
    private
"""


class Computer:
    def __init__(self, cpu, memory, hdd):
        self.__cpu = cpu  # private
        self._memory = memory  # protected
        self.hdd = hdd  # public

    def print_computer(self):
        print('CPU: {} Mhz,\nMemory: {} Mb,\nHDD: {} GB'.format(
            self.__cpu,
            self._memory,
            self.hdd
        ))

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, cpu):
        if cpu < 0:
            raise ValueError(f"Incorrect value {cpu}")

        self.__cpu = cpu


comp = Computer(2300, 16000, 2000)
comp.print_computer()
print(dir(comp))
print(comp._Computer__cpu)
print(comp._memory)
print(comp.hdd)
print(comp.cpu)
comp.cpu = 4545442
