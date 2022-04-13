class LCG:
  a = 672257317069504227  # "乘数"
  b = 7382843889490547368  # "增量"
  m = 9223372036854775783  # "模数"
  def __init__(self, seed):
    self.state = seed  # "种子"
  def next(self):
    self.state = (self.state * self.a + self.b) % self.m
    return self.state
gen = LCG(123)  # seed = 123
print gen.next()  # 第一个生成值
print gen.next()  # 第二个生成值
print gen.next()  # 第三个生成值
# 7060145557346585242
# 3490819368718893392
# 6200546448603839134
