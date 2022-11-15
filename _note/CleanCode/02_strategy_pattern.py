# 전략 패턴
# https://www.youtube.com/watch?v=63miHKtooo4&ab_channel=%EC%98%A4%EB%8A%98%EC%BD%94%EB%94%A9
# https://www.youtube.com/watch?v=vNsZXC3VgUA&ab_channel=%EC%9A%B0%EC%95%84%ED%95%9CTech

########################################################################
# 잘못된 방법(?)
########################################################################

from abc import ABCMeta, abstractmethod


class WalkingRobot:
  def display(self):
    print('걷기 로봇')

  def move(self):
    print('걸어서 배달합니다. 삐-빅')


class RunningRobot:
  def display(self):
    print('뛰기 로봇')

  def move(self):
    print('뛰어서 배달합니다. 삐-빅')


class Service:
  def execute(self):
    robot1 = WalkingRobot()
    robot2 = RunningRobot()

    robot1.move()
    robot2.move()

Service().execute()

########################################################################
# 상속을 이용한 로봇 설계
print();print()
########################################################################

class Robot(metaclass=ABCMeta):

  @abstractmethod
  def display(self):
    raise NotImplementedError()

  @abstractmethod
  def move(self):
    raise NotImplementedError()


class WalkingRobot(Robot):

  def display(self):
    print('걷기 로봇')

  def move(self):
    print('걸어서 배달합니다. 삐-빅')


class RunningRobot(Robot):

  def display(self):
    print('뛰기 로봇')

  def move(self):
    print('뛰어서 배달합니다. 삐-빅')


class FlyRobot(Robot):

  def display(self):
    print('날기 로봇')

  def move(self):
    print('날아서 배달합니다. 삐-빅')

class Service:
  def execute(self):
    robot1 = WalkingRobot()
    robot2 = RunningRobot()
    robot3 = FlyRobot()

    robot1.move()
    robot2.move()
    robot3.move()


Service().execute()


########################################################################
# 전략패턴을 이용한 로봇 설계
print();print()
########################################################################
class MoveStrategy:  # Interface 역할
  def move(self):
    pass


class Walk(MoveStrategy):
  def move(self):
    print('걸어서 배달합니다. 삐-빅')


class Run(MoveStrategy):
  def move(self):
    print('뛰어서 배달합니다. 삐-빅')


class Fly(MoveStrategy):
  def move(self):
    print('날아서 배달합니다. 삐-빅')


class TemperatureStrategy: # Interface 역할
  def temperature(self):
    pass


class Cold(TemperatureStrategy):
  def temperature(self):
    print('차갑습니다. 삐-빅')


class Warm(TemperatureStrategy):
  def temperature(self):
    print('따뜻합니다. 삐-빅')


class Hot(TemperatureStrategy):
  def temperature(self):
    print('뜨겁습니다. 삐-빅')


class SpeakStrategy:  # Interface 역할
  def speak(self):
    pass


class Korean(SpeakStrategy):
  def speak(self):
    print('한국말 좀 함; 삐-빅')


class English(SpeakStrategy):
  def speak(self):
    print('영어 좀 함; 삐-빅')


class Robot:
  __move_strategy: MoveStrategy = None
  __temperature_strategy: TemperatureStrategy = None
  __speak_strategy: SpeakStrategy = None

  def __init__(
    self,
    move_strategy: MoveStrategy,
    temperature_strategy: TemperatureStrategy,
    speak_strategy: SpeakStrategy,
  ):
    self.__move_strategy = move_strategy
    self.__temperature_strategy = temperature_strategy
    self.__speak_strategy = speak_strategy

  def move(self):
    self.__move_strategy.move()

  def temperature(self):
    self.__temperature_strategy.temperature()

  def speak(self):
    self.__speak_strategy.speak()

  # setter 를 설정해둠으로써, 객체 생성 후 전략을 변경가능하도록 하자.
  def set_move_strategy(self, move_strategy):
    self.__move_strategy = move_strategy

  def set_temperature_strategy(self, temperature_strategy):
    self.__temperature_strategy = temperature_strategy

  def set_speak_strategy(self, speak_strategy):
    self.__speak_strategy = speak_strategy


class Service:

  def execute(self):
    robot = Robot(Walk(), Cold(), Korean())

    # Walk, Cold
    robot.move()
    robot.temperature()

    # Fly, Cold
    robot.set_move_strategy(Fly())
    robot.move()
    robot.temperature()

    # Fly, Hot
    robot.set_temperature_strategy(Hot())
    robot.move()
    robot.temperature()


Service().execute()
