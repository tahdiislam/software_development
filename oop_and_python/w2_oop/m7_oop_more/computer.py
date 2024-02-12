class CPU:
    def __init__(self, core) -> None:
        self.core = core


class RAM:
    def __init__(self, size) -> None:
        self.size = size


class SSD:
    def __init__(self, capacity) -> None:
        self.capacity = capacity


class Computer:
    def __init__(self, core, ram_size, ssd_capacity) -> None:
        self.brand = "Dell"
        self.cpu = CPU(core)
        self.ram = RAM(ram_size)
        self.ssd = SSD(ssd_capacity)

    def __repr__(self) -> str:
        return f"pc has {self.cpu.core} core's, {self.ram.size} gb ram and {self.ssd.capacity} gb ssd"


my_pc = Computer(8, 8, 256)
print(my_pc)
